# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Client'
        db.create_table('money_client', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=250)),
            ('description', self.gf('django.db.models.fields.TextField')(default='', max_length=1000)),
        ))
        db.send_create_signal('money', ['Client'])

        # Adding model 'Portfolio'
        db.create_table('money_portfolio', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('client', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['money.Client'])),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=250)),
            ('description', self.gf('django.db.models.fields.TextField')(default='', max_length=1000)),
        ))
        db.send_create_signal('money', ['Portfolio'])

        # Adding model 'Currency'
        db.create_table('money_currency', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('code', self.gf('django.db.models.fields.CharField')(unique=True, max_length=3)),
            ('numeric', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('money', ['Currency'])

        # Adding model 'ExchangeRate'
        db.create_table('money_exchangerate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('from_curr', self.gf('django.db.models.fields.related.ForeignKey')(related_name='rate_from', to=orm['money.Currency'])),
            ('to_curr', self.gf('django.db.models.fields.related.ForeignKey')(related_name='rate_to', to=orm['money.Currency'])),
            ('rate', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('money', ['ExchangeRate'])

        # Adding unique constraint on 'ExchangeRate', fields ['to_curr', 'rate']
        db.create_unique('money_exchangerate', ['to_curr_id', 'rate'])

        # Adding unique constraint on 'ExchangeRate', fields ['from_curr', 'rate']
        db.create_unique('money_exchangerate', ['from_curr_id', 'rate'])

        # Adding model 'Transaction'
        db.create_table('money_transaction', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('amount', self.gf('core.utils.CurrencyField')(max_digits=8, decimal_places=2)),
            ('exchange_rate', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['money.ExchangeRate'])),
            ('portfolio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['money.Portfolio'])),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(default='', max_length=1000)),
        ))
        db.send_create_signal('money', ['Transaction'])

    def backwards(self, orm):
        # Removing unique constraint on 'ExchangeRate', fields ['from_curr', 'rate']
        db.delete_unique('money_exchangerate', ['from_curr_id', 'rate'])

        # Removing unique constraint on 'ExchangeRate', fields ['to_curr', 'rate']
        db.delete_unique('money_exchangerate', ['to_curr_id', 'rate'])

        # Deleting model 'Client'
        db.delete_table('money_client')

        # Deleting model 'Portfolio'
        db.delete_table('money_portfolio')

        # Deleting model 'Currency'
        db.delete_table('money_currency')

        # Deleting model 'ExchangeRate'
        db.delete_table('money_exchangerate')

        # Deleting model 'Transaction'
        db.delete_table('money_transaction')

    models = {
        'money.client': {
            'Meta': {'object_name': 'Client'},
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '1000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250'})
        },
        'money.currency': {
            'Meta': {'object_name': 'Currency'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '3'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'numeric': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        },
        'money.exchangerate': {
            'Meta': {'unique_together': "(('to_curr', 'rate'), ('from_curr', 'rate'))", 'object_name': 'ExchangeRate'},
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'from_curr': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rate_from'", 'to': "orm['money.Currency']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rate': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'to_curr': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rate_to'", 'to': "orm['money.Currency']"})
        },
        'money.portfolio': {
            'Meta': {'object_name': 'Portfolio'},
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['money.Client']"}),
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '1000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250'})
        },
        'money.transaction': {
            'Meta': {'ordering': "('date_added',)", 'object_name': 'Transaction'},
            'amount': ('core.utils.CurrencyField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'exchange_rate': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['money.ExchangeRate']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '1000'}),
            'portfolio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['money.Portfolio']"})
        }
    }

    complete_apps = ['money']