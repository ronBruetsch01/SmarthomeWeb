from django.db import models

# Create your models here.
class Sensor(models.Model):
    sen_id = models.IntegerField(primary_key=True)
    sen_raum = models.CharField(max_length=45)
    sen_ip = models.GenericIPAddressField(error_messages="IPAdress is not valid!")

    class Meta:
        managed = False
        db_table = 'sensor'


class Werte(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    sen = models.ForeignKey(Sensor, models.DO_NOTHING)
    luftdruck = models.FloatField()
    luftfeuchte = models.FloatField()
    temperatur = models.FloatField()
    datum = models.DateTimeField()
    
    def __str__(self):
        return str(self.datum)

    class Meta:
        managed = False
        db_table = 'werte'