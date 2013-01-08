from bs4 import BeautifulSoup
from decimal import Decimal, InvalidOperation
from django.core.management.base import BaseCommand
from django.utils.http import urlquote_plus
from optparse import make_option
from setscrape.models import Sector, Symbol, Stock
import datetime
import re
import urllib2
import os
import time


DELAY = 6


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
                    make_option('--sector', action='store'),
                    make_option('--numdays', action='store'))
            
    def handle(self, *args, **options):
        if not options or not options.get('numdays'):
            numdays = 1
        else:
            numdays = options['numdays']
            
        if options.get('sector'):
            sector = Sector.objects.get(name=options['sector'])
            symbols = sector.symbols.all()
        else:
            if not args:
                symbols = Symbol.objects.exclude(stocks__isnull=True)
            else:
                args = map(lambda s: s.upper(), args)
                symbols = Symbol.objects.filter(symbol__in=args)
        
        for symbol in symbols:
            save_symbol(symbol, numdays)
            time.sleep(DELAY)
            
            
def save_symbol(symbol, num_days):
    url = 'http://www.settrade.com/C04_02_stock_historical_p1.jsp' + \
          '?txtSymbol=%s&selectPage=2&max=%s' % (urlquote_plus(symbol.symbol), num_days)
    
    for i in xrange(5):
        try:
            html = urllib2.urlopen(url).read()
            break
        except:
            if i == 4:
                print '----- %s -----' % symbol.symbol
                return
        time.sleep(DELAY)
    
    soup = BeautifulSoup(html, from_encoding='tis-620')
    div = soup('div', style='width:720px;margin:0px auto;border-bottom:2px solid #EEE;')[0]
    for row in div('div', attrs={'class': re.compile('^tablecolor')}):
        data = {'symbol': symbol}
        # replace thousand seperated.
        columns = [c.text.replace(',', '') for c in row('div')[:-1]]
        data['date'] = datetime.datetime.strptime(columns[0], '%d/%m/%y').date()
        try:
            Stock.objects.get(**data)
        except Stock.DoesNotExist:
            try:
                data['open_price'] = Decimal(columns[1])
                data['high_price'] = Decimal(columns[2])
                data['low_price'] = Decimal(columns[3])
                data['avg_price'] = Decimal(columns[4])
                data['close_price'] = Decimal(columns[5])
                data['price_change'] = Decimal(columns[6])
                data['percent_change'] = float(columns[7])
                data['volume'] = float(columns[8])
                data['value'] = Decimal(columns[9])
                data['set_index'] = float(columns[10])
                data['set_index_change'] = float(columns[11])
                Stock.objects.create(**data)
            except InvalidOperation:
                print 'error on %s (%s)' % (symbol.symbol, columns[0])
