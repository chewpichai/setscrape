# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Stock.symbol'
        db.alter_column('setscrape_stock', 'symbol', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['setscrape.Symbol'], db_column='symbol'))
        # Adding index on 'Stock', fields ['symbol']
        db.create_index('setscrape_stock', ['symbol'])


    def backwards(self, orm):
        # Removing index on 'Stock', fields ['symbol']
        db.delete_index('setscrape_stock', ['symbol'])


        # Changing field 'Stock.symbol'
        db.alter_column('setscrape_stock', 'symbol', self.gf('django.db.models.fields.CharField')(max_length=10))

    models = {
        'setscrape.financialdata': {
            'Meta': {'ordering': "['-date']", 'object_name': 'FinancialData'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_th': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'symbol': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['setscrape.Symbol']", 'db_column': "'symbol'"}),
            'value': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '11', 'decimal_places': '2'})
        },
        'setscrape.sector': {
            'Meta': {'ordering': "['name']", 'object_name': 'Sector'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'}),
            'name_th': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'})
        },
        'setscrape.stock': {
            'Meta': {'ordering': "['symbol', '-date']", 'object_name': 'Stock'},
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
            'symbol': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['setscrape.Symbol']", 'db_column': "'symbol'"}),
            'value': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'}),
            'volume': ('django.db.models.fields.FloatField', [], {})
        },
        'setscrape.symbol': {
            'Meta': {'ordering': "['symbol']", 'object_name': 'Symbol'},
            'first_trade_date': ('django.db.models.fields.DateField', [], {}),
            'market': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'name_th': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'par_value': ('django.db.models.fields.DecimalField', [], {'max_digits': '9', 'decimal_places': '2'}),
            'sector': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['setscrape.Sector']"}),
            'symbol': ('django.db.models.fields.CharField', [], {'max_length': '10', 'primary_key': 'True'})
        }
    }

    complete_apps = ['setscrape']
