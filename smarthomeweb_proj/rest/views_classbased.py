from django.http import JsonResponse
#..>python -m pip install djangorestframework
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Werte, Sensor
from .serializers import WerteSerializer, SensorSerializer
from rest_framework import generics

class WerteListAPIView(generics.ListAPIView):
    queryset = Werte.objects.all()
    serializer_class = WerteSerializer

class WertDetailRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Werte.objects.all()
    serializer_class = WerteSerializer

class WerteListCreateAPIView(generics.ListCreateAPIView):
    queryset = Werte.objects.all()
    serializer_class = WerteSerializer

    def perform_create(self, serializer):
        serializer.save()

class WertCreateAPIView(generics.CreateAPIView):
    queryset = Werte.objects.all()
    serializer_class = WerteSerializer

class SensorCreateAPIView(generics.CreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def perform_create(self, serializer):
        return serializer.save()

class WertUpdateAPIView(generics.UpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class WertDeleteAPIView(generics.DestroyAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)





