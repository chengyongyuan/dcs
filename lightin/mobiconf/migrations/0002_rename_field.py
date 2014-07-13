# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Rename field names(lu->left...)
        db.rename_column('mobiconf_screenconf', 'lu', 'left');
        db.rename_column('mobiconf_screenconf', 'll', 'right');
        db.rename_column('mobiconf_screenconf', 'ru', 'top');
        db.rename_column('mobiconf_screenconf', 'rl', 'bottom');


    def backwards(self, orm):
        # Rename left->lu
        db.delete_table(u'mobiconf_screenconf')
        db.rename_column('mobiconf_screenconf', 'left'  , 'lu');
        db.rename_column('mobiconf_screenconf', 'right' , 'll');
        db.rename_column('mobiconf_screenconf', 'top'   , 'ru');
        db.rename_column('mobiconf_screenconf', 'bottom', 'rl');
