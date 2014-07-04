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
        return "[name:%s, lu:%.2f, ll:.2fu, ru:%.2f, rl:%.2f]" \
               %(self.mtype, self.lu, self.ll, self.ru, self.rl)
