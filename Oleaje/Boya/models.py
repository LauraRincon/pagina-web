from django.db import models

class Boya(models.Model):
    date = models.DateField()
    hour = models.TimeField()
    Hs = models.IntegerField()
    Tm02 = models.IntegerField()
    Tp = models.IntegerField()
    Tz = models.IntegerField()
    Hm0 = models.IntegerField()
    Hmax = models.IntegerField()
    H1_10 = models.IntegerField()
