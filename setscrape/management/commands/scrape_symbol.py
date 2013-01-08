# coding=utf8>
from bs4 import BeautifulSoup
from decimal import Decimal, InvalidOperation
from django.core.management.base import BaseCommand
from django.utils.http import urlquote_plus
from setscrape.models import Symbol, Sector
import datetime
import os
import re
import string
import urllib2


PREFIXS = ['NUMBER'] + list(string.uppercase)


class Command(BaseCommand):
    def handle(self, *args, **options):
        path = os.path.join(os.path.dirname(__file__), 'prefix', '%s.html')
        for prefix in PREFIXS:
            if prefix == 'X': continue
            print '----- %s -----' % prefix
            html = open(path % prefix).read()
            soup = BeautifulSoup(html, from_encoding='tis-620')
            td = soup('td', align='right', colspan='3')[0]
            table = td.parent.parent.parent
            for tr in table('tr', valign='top'):
                data = {}
                data['symbol'] = tr('td')[0].text
                data['name_th'] = tr('td')[1].text.encode('utf8')
                data['market'] = tr('td')[2].text
                data.update(get_detail(data['symbol']))
                Symbol.objects.create(**data)
                

def get_detail(symbol):
    data = {}
    url = 'http://www.set.or.th/set/companyprofile.do?symbol=%s' % urlquote_plus(symbol)
    html = urllib2.urlopen(url).read()
    soup = BeautifulSoup(html, from_encoding='tis-620')
    data['name'] = soup('td', height='18', colspan='2')[0].text
    data['sector'] = soup(text='Sector')[0].parent.parent.find_next_sibling('td').text
    data['sector'], created = Sector.objects.get_or_create(name=data['sector'], name_th=data['sector'])
    data['first_trade_date'] = soup(text='First Trade Date')[0].parent.parent.find_next_sibling('td').text
    data['first_trade_date'] = datetime.datetime.strptime(data['first_trade_date'], '%d %b %Y').date()
    data['par_value'] = soup(text='Par Value')[0].parent.parent.find_next_sibling('td').text
    data['par_value'] = Decimal(data['par_value'].split()[0])
    return data
    
