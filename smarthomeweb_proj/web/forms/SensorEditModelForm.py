from django.forms import ModelForm
from web.models import Sensor

class SensorEditModelForm(ModelForm):
    class Meta:
        model = Sensor
        fields = "__all__"

    