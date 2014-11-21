# coding=utf8>
from bs4 import BeautifulSoup
from decimal import Decimal, InvalidOperation
from django.core.exceptions import MultipleObjectsReturned
from django.core.management.base import BaseCommand
from django.utils.http import urlquote_plus
from setscrape.models import Symbol, FinancialData
import datetime
import os
import re
import string
import time
import urllib2


class Command(BaseCommand):
    def handle(self, *args, **options):
        symbols = []

        if args:
            args = map(lambda s: s.upper(), args)
            symbols = Symbol.objects.filter(symbol__in=args)

        if not symbols:
            symbols = Symbol.objects.exclude(stocks__isnull=True)

        for symbol in symbols:
            print '----- %s -----' % symbol.symbol
            url = 'http://www.set.or.th/set/companyhighlight.do?symbol=%s&language=en&country=US' % urlquote_plus(symbol.symbol)
            html = urllib2.urlopen(url).read()
            soup = BeautifulSoup(html, from_encoding='tis-620')

            try: table = soup(text='(Unit: M.Baht)')[0].parent.parent.parent
            except: continue

            tr = table('tr', align='center')[1]

            for i, row in enumerate(table('tr', align='right')):
                if i in (0, 8): continue

                name = row('td')[0].text

                for j, td in enumerate(tr('td')):
                    try:
                        date = datetime.datetime.strptime(td.text.strip(), '%d/%m/%Y').date()

                        try:
                            value = Decimal(row('td')[j].text.replace(',', ''))
                        except InvalidOperation:
                            value = None

                        try:
                            fs = FinancialData.objects.get(symbol=symbol, date__year=date.year, name=name)
                        except MultipleObjectsReturned:
                            FinancialData.objects.filter(symbol=symbol, date__year=date.year, name=name).delete()
                            fs = FinancialData(symbol=symbol, name=name, name_th=name)
                        except FinancialData.DoesNotExist:
                            fs = FinancialData(symbol=symbol, name=name, name_th=name)

                        fs.date = date
                        fs.value = value
                        fs.save()
                    except (ValueError, IndexError):
                        pass

            time.sleep(3)

