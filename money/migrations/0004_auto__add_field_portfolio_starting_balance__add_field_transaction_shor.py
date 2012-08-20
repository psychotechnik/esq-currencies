# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Portfolio.starting_balance'
        db.add_column('money_portfolio', 'starting_balance',
                      self.gf('core.utils.CurrencyField')(null=True, max_digits=8, decimal_places=2, blank=True),
                      keep_default=False)

        # Adding field 'Transaction.short_description'
        db.add_column('money_transaction', 'short_description',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)

    def backwards(self, orm):
        # Deleting field 'Portfolio.starting_balance'
        db.delete_column('money_portfolio', 'starting_balance')

        # Deleting field 'Transaction.short_description'
        db.delete_column('money_transaction', 'short_description')

    models = {
        'money.client': {
            'Meta': {'object_name': 'Client'},
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '1000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250'})
        },
        'money.currency': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Currency'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '3'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '250'}),
            'starting_balance': ('core.utils.CurrencyField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'})
        },
        'money.transaction': {
            'Meta': {'ordering': "('portfolio__name', 'order')", 'object_name': 'Transaction'},
            'amount': ('core.utils.CurrencyField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'balance_amount': ('core.utils.CurrencyField', [], {'default': '0', 'max_digits': '8', 'decimal_places': '2'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'exchange_rate': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['money.ExchangeRate']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '1000'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'portfolio': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'transactions'", 'to': "orm['money.Portfolio']"}),
            'short_description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'})
        }
    }

    complete_apps = ['money']