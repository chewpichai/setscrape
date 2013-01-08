from django.db import models
from django.utils.http import urlquote_plus


class Sector(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    name_th = models.CharField(max_length=255, db_index=True)
    
    class Meta:
        ordering = ['name']
    
    def __unicode__(self):
        return u'%s' % self.name


class Symbol(models.Model):
    symbol = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=255)
    name_th = models.CharField(max_length=255)
    sector = models.ForeignKey(Sector, related_name='symbols')
    market = models.CharField(max_length=10)
    first_trade_date = models.DateField()
    par_value = models.DecimalField(max_digits=9, decimal_places=2)
    
    class Meta:
        ordering = ['sector', 'symbol']
    
    def __unicode__(self):
        return u'%s (%s)' % (self.name, self.symbol)
        
    @models.permalink
    def get_absolute_url(self):
        return ('setscrape.symbol', [], {'symbol': urlquote_plus(self.symbol)})
        

class Stock(models.Model):
    symbol = models.ForeignKey(Symbol, db_column='symbol', related_name='stocks')
    date = models.DateField()
    open_price = models.DecimalField(max_digits=9, decimal_places=2)
    high_price = models.DecimalField(max_digits=9, decimal_places=2)
    low_price = models.DecimalField(max_digits=9, decimal_places=2)
    avg_price = models.DecimalField(max_digits=9, decimal_places=2)
    close_price = models.DecimalField(max_digits=9, decimal_places=2)
    price_change = models.DecimalField(max_digits=9, decimal_places=2)
    percent_change = models.FloatField()
    volume = models.FloatField()
    value = models.DecimalField(max_digits=9, decimal_places=2)
    set_index = models.FloatField()
    set_index_change = models.FloatField()
    
    class Meta:
        ordering = ['symbol', '-date']
    
    def __unicode__(self):
        return u'%s %s' % (self.symbol, self.date)
        

class FinancialData(models.Model):
    symbol = models.ForeignKey(Symbol, db_column='symbol', related_name='finances')
    date = models.DateField()
    name = models.CharField(max_length=255)
    name_th = models.CharField(max_length=255)    
    value = models.DecimalField(max_digits=11, decimal_places=2, null=True)
    
    class Meta:
        ordering = ['-date', 'id']
