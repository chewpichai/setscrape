# coding=utf8>
from bs4 import BeautifulSoup
from decimal import Decimal, InvalidOperation
from django.core.management.base import BaseCommand
from django.utils.http import urlquote_plus
from setscrape.models import Symbol, FinancialData
import datetime
import os
import re
import string
import urllib2


class Command(BaseCommand):
    def handle(self, *args, **options):
        for symbol in Symbol.objects.filter(symbol__gt='F'):
            print '----- %s -----' % symbol.symbol
            url = 'http://www.set.or.th/set/companyhighlight.do?symbol=%s' % urlquote_plus(symbol.symbol)
            html = urllib2.urlopen(url).read()
            soup = BeautifulSoup(html, from_encoding='tis-620')
            tr = soup(text='(Unit: M.Baht)')[0].parent.parent.find_next_sibling('tr')
            table = soup(text='(Unit: M.Baht)')[0].parent.parent.parent
            for i, row in enumerate(table('tr', align='right')):
                if i in (0, 8): continue
            
                name = row('td')[0].text
                for j, td in enumerate(tr('td')):
                    try:
                        date = datetime.datetime.strptime(td.contents[0].contents[2].strip(), '%d/%m/%Y').date()
                        try:
                            value = Decimal(row('td')[j].text.replace(',', ''))
                        except InvalidOperation:
                            value = None
                        FinancialData.objects.get_or_create(symbol=symbol, date=date, name=name, name_th=name, value=value)
                    except (ValueError, IndexError):
                        pass
    
