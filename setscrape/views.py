from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from setscrape.models import Symbol, Stock
from setscrape import api


def get_api(request):
    method = request.GET.get('method')
    if method:
        return getattr(api, method)(request)
    return HttpResponseNotFound()


def get_index(request):
    symbols = Symbol.objects.exclude(stocks__isnull=True)
    return render(request, 'setscrape/index.html', locals())


def get_symbol(request, symbol):
    symbol = get_object_or_404(Symbol, symbol=symbol.upper())
    return render(request, 'setscrape/symbol.html', locals())
