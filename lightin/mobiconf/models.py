#-*- coding:utf8 -*-
from django.db import models

# Create your models here.
class ScreenConf(models.Model):
    """this model define mobile screen coordinate"""
    mtype = models.CharField(max_length=128)  #mobile type string
    left      = models.FloatField()               #left  margin
    right     = models.FloatField()               #right margin 
    top       = models.FloatField()               #top   margin
    bottom    = models.FloatField()               #bottom margin

    def __unicode__(self):
        return u"[机型:%s, 左边距:%s, 右边距:%s, 上边距:%s, 边距:%s]" \
               %(self.mtype, self.left, self.right, self.top, self.bottom)
