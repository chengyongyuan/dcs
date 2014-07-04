# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ScreenConf'
        db.create_table(u'mobiconf_screenconf', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mtype', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('lu', self.gf('django.db.models.fields.FloatField')()),
            ('ll', self.gf('django.db.models.fields.FloatField')()),
            ('ru', self.gf('django.db.models.fields.FloatField')()),
            ('rl', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'mobiconf', ['ScreenConf'])


    def backwards(self, orm):
        # Deleting model 'ScreenConf'
        db.delete_table(u'mobiconf_screenconf')


    models = {
        u'mobiconf.screenconf': {
            'Meta': {'object_name': 'ScreenConf'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'll': ('django.db.models.fields.FloatField', [], {}),
            'lu': ('django.db.models.fields.FloatField', [], {}),
            'mtype': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'rl': ('django.db.models.fields.FloatField', [], {}),
            'ru': ('django.db.models.fields.FloatField', [], {})
        }
    }

    complete_apps = ['mobiconf']