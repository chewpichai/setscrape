# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Stock'
        db.create_table('setscrape_stock', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('symbol', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('open_price', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2)),
            ('high_price', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2)),
            ('low_price', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2)),
            ('avg_price', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2)),
            ('close_price', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2)),
            ('price_change', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2)),
            ('percent_change', self.gf('django.db.models.fields.FloatField')()),
            ('volume', self.gf('django.db.models.fields.FloatField')()),
            ('value', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2)),
            ('set_index', self.gf('django.db.models.fields.FloatField')()),
            ('set_index_change', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('setscrape', ['Stock'])


    def backwards(self, orm):
        # Deleting model 'Stock'
        db.delete_table('setscrape_stock')


    models = {
        'setscrape.stock': {
            'Meta': {'ordering': "('symbol', '-date')", 'object_name': 'Stock'},
            'avg_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'}),
            'close_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'high_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'low_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'}),
            'open_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'}),
            'percent_change': ('django.db.models.fields.FloatField', [], {}),
            'price_change': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'}),
            'set_index': ('django.db.models.fields.FloatField', [], {}),
            'set_index_change': ('django.db.models.fields.FloatField', [], {}),
            'symbol': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'value': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'}),
            'volume': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['setscrape']
