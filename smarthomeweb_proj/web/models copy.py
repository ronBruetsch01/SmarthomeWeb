from django.db import models

# Create your models here.
class TempValue(models.Model):
    tempValue = models.DecimalField(max_digits=3, decimal_places=1)
    sensorip = models.CharField(max_length=15)
    timestamp = models.DateTimeField()

class Tblklimawert(models.Model):
    kwid = models.AutoField(primary_key=True)
    temp = models.FloatField(blank=True, null=True)
    lfeuchte = models.FloatField(blank=True, null=True)
    druck = models.FloatField(blank=True, null=True)
    ppmco2 = models.FloatField(blank=True, null=True)
    zeitpunkt = models.DateTimeField(blank=True, null=True)
    fksensid = models.ForeignKey('Tblsensor', models.DO_NOTHING, db_column='fksensid')

    class Meta:
        managed = False
        db_table = 'tblklimawert'


class Tblsensor(models.Model):
    sensid = models.IntegerField(primary_key=True)
    ipadresse = models.CharField(max_length=100, blank=True, null=True)
    standort = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tblsensor'