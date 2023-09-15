from django.forms import ModelForm
from web.models import Sensor

class SensorCreateEditModelForm(ModelForm):
    class Meta:
        model = Sensor
        fields = "__all__"

    