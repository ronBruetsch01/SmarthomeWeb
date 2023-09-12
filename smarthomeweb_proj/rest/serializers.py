from rest_framework import serializers
from .models import Werte, Sensor


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['sen_id', 'sen_raum', 'sen_ip']


class WerteSerializer(serializers.ModelSerializer):
   sen = SensorSerializer()
   class Meta:
        model = Werte
        #fields = ['id', 'temperatur', 'sen']
        fields = "__all__"


        