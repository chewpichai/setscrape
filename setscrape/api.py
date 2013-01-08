from django.http import HttpResponse
from django.utils import simplejson as json
from setscrape.models import Stock
import datetime
import decimal
import time


def encode_default(d):
    if isinstance(d, decimal.Decimal):
        return float(str(d))
    elif isinstance(d, datetime.date):
        return int(time.mktime(d.timetuple()) * 1000)
    raise TypeError
    
    
def get_stock(request):
    symbol = request.GET['symbol'].upper()
    values = ('date', 'open_price', 'high_price', 'low_price', 'close_price')
    stocks = Stock.objects.filter(symbol=symbol) \
                          .values_list(*values).order_by('date')
    data = {'name': symbol}
    data['data'] = list(stocks)
    return HttpResponse(json.dumps(data, default=encode_default),
                        content_type='application/json')
