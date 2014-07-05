#-*- coding:utf8 -*-
from django.db import models

# Create your models here.
class ScreenConf(models.Model):
    """this model define mobile screen coordinate"""
    mtype = models.CharField(max_length=128)  #mobile type string
    lu    = models.FloatField()               #left upper
    ll    = models.FloatField()               #left lower
    ru    = models.FloatField()               #right upper
    rl    = models.FloatField()               #right lower 

    def __unicode__(self):
        return u"[机型:%s, 左上:%s, 左下:%s, 右上:%s, 右下:%s]" \
               %(self.mtype, self.lu, self.ll, self.ru, self.rl)
