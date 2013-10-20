# coding=utf8>
from bs4 import BeautifulSoup
from decimal import Decimal
from django.core.management.base import BaseCommand
from django.utils.http import urlquote_plus
from setscrape.models import Symbol, Sector
import datetime
import urllib2


class Command(BaseCommand):
    def handle(self, *args, **options):
        for symbol in args:
            symbol = symbol.upper()
            data = {}
            data['symbol'] = symbol
            data.update(get_detail(data['symbol']))
            Symbol.objects.create(**data)
            print '--- ADDED %s ---' % symbol
                

def get_detail(symbol):
    data = {}
    url = 'http://www.set.or.th/set/companyprofile.do?symbol=%s' % urlquote_plus(symbol)
    html = urllib2.urlopen(url).read()
    soup = BeautifulSoup(html, from_encoding='tis-620')
    data['name'] = soup('td', height='18', colspan='2')[0].text
    data['market'] = soup(text='Market')[0].parent.parent.find_next_sibling('td').text
    data['sector'] = soup(text='Sector')[0].parent.parent.find_next_sibling('td').text
    data['sector'], created = Sector.objects.get_or_create(name=data['sector'])
    data['first_trade_date'] = soup(text='First Trade Date')[0].parent.parent.find_next_sibling('td').text
    data['first_trade_date'] = datetime.datetime.strptime(data['first_trade_date'], '%d %b %Y').date()
    data['par_value'] = soup(text='Par Value')[0].parent.parent.find_next_sibling('td').text
    data['par_value'] = Decimal(data['par_value'].split()[0])
    return data
