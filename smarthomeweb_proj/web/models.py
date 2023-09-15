from django.db import models
from django.utils import timezone


class Sensor(models.Model):
    sen_raum = models.CharField(max_length=45)
    sen_ip = models.CharField(max_length=45)
    sen_code = models.TextField()

  

class Werte(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.DO_NOTHING, default=1)
    luftdruck = models.FloatField()
    luftfeuchte = models.FloatField()
    temperatur = models.FloatField()
    datum = models.DateTimeField()
