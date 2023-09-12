from django.http import JsonResponse
#..>python -m pip install djangorestframework
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Werte
from .serializers import WerteSerializer, SensorSerializer
from rest_framework import generics

@api_view(["GET"])
def readAll(request):
    allewerte = Werte.objects.all()
    ser = WerteSerializer(allewerte, many=True)
    return Response(ser.data)

@api_view(["GET"])
def rest_home(request, *args, **kwargs):
    if request.method == "GET":
        model = Werte.objects.all().order_by("?").first()
        return Response(model)


@api_view(["GET"]) # DRF-Method
def apiDescription(request):

    urls = {
        "Create":"/create/",
        "ReadAll":"/readall/",
        "ReadById":"/readbyid/<str:werte_id>/",
        "Update":"/update/",
        "Delete":"/delete/<str:pk>/",
        "Details":"/details/<str:pk>/"
    }

    return Response(urls)


@api_view(["GET"])
def readById(request, werte_id):
    einWerteSatz = Werte.objects.get(id=werte_id)
    ser = WerteSerializer(einWerteSatz, many=False)
    return Response(ser.data)

@api_view(["POST"])
def create(request):
    ser = WerteSerializer(data=request.data)
    if ser.is_valid():
        ser.save()
    return Response(ser.data)

@api_view(["POST"])
def update(request, werte_id):
    werte = Werte.objects.get(id=werte_id)
    ser = WerteSerializer(instance=werte, data=request.data)
    
    if ser.is_valid():
        ser.save()

    return Response(ser.data)

@api_view(["DELETE"])
def delete(request, werte_id):
    werte = Werte.objects.get(id=werte_id)
    werte.delete()

    return Response(f"{werte.id}  wurde gelöscht.")

