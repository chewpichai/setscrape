# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Symbol'
        db.create_table('setscrape_symbol', (
            ('symbol', self.gf('django.db.models.fields.CharField')(max_length=10, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('name_th', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('sector', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['setscrape.Sector'])),
            ('market', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('first_trade_date', self.gf('django.db.models.fields.DateField')()),
            ('par_value', self.gf('django.db.models.fields.DecimalField')(max_digits=9, decimal_places=2)),
        ))
        db.send_create_signal('setscrape', ['Symbol'])

        # Adding model 'Sector'
        db.create_table('setscrape_sector', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, db_index=True)),
            ('name_th', self.gf('django.db.models.fields.CharField')(max_length=255, db_index=True)),
        ))
        db.send_create_signal('setscrape', ['Sector'])


    def backwards(self, orm):
        # Deleting model 'Symbol'
        db.delete_table('setscrape_symbol')

        # Deleting model 'Sector'
        db.delete_table('setscrape_sector')


    models = {
        'setscrape.sector': {
            'Meta': {'object_name': 'Sector'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '10', 'db_index': 'True'}),
            'name_th': ('django.db.models.fields.CharField', [], {'max_length': '10', 'db_index': 'True'})
        },
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
        },
        'setscrape.symbol': {
            'Meta': {'object_name': 'Symbol'},
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
