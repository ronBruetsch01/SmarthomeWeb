from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Sensor, Werte
from web.forms.TempsFilterForm import TempsFilterForm
# from web.forms.HumidsFilterForm import HumidsFilterForm
from web.forms.SensorCreateEditModelForm import SensorCreateEditModelForm
from django.db.models import Max, Min
from datetime import datetime, timedelta


def index(request):
    # return HttpResponse("Hello, world. You're at the web app.")
    return render(request, 'web/index.html')


def display_sensors(request):
    queryset = Sensor.objects.all()
    return render(request, "web/sensors.html", {"sensorlist": list(queryset)})


def tempdetails(request, temp_id):
    print(temp_id + "tempdetails")
    queryset = Sensor.objects.get(pk=temp_id)
    return HttpResponse(f"""Tempdetails for Sensor-ID {temp_id}:
                         {queryset.sen_raum}, 
                         {queryset.sen_ip},
                         {queryset.sen_code}""")


def edit_sensor_details(request, sensor_id):
    sensor = Sensor.objects.get(pk=sensor_id)

    if request.method == "POST":
        print("GET")
        form = SensorCreateEditModelForm(request.POST, instance=sensor)
        if form.is_valid():
            form.save()
            return redirect("/web/sensors/")
    else:
        print("GET")
        print(sensor_id)
        form = SensorCreateEditModelForm(instance=sensor)
        print(sensor)
        return render(request, "web/sensor_edit.html", {"form": form})

def display_temps(request):
    print("display_temps")
    if request.method == "POST":
        form = TempsFilterForm(request.POST)
        print("display_temps")
        print(form)

        if form.is_valid():
            print(form.cleaned_data)
            lowerVal = form.cleaned_data["lowerVal"]
            if lowerVal is None:
                lowerVal = Werte.objects.aggregate(Min('temperatur'))["temperatur__min"]
                print(lowerVal)
            
            upperVal = form.cleaned_data["upperVal"]
            if upperVal is None:
                upperVal = Werte.objects.aggregate(Max('temperatur'))["temperatur__max"]
                print(upperVal)
                        
            # if upperVal is None:
                # upperVal = Werte.ob
            vonDate = form.cleaned_data["vonDate"]
            bisDate = form.cleaned_data["bisDate"]
            print(f"{lowerVal}, {upperVal}, {vonDate}, {bisDate}")
            # queryset = Werte.objects.filter(temperatur__lte = form.cleaned_data["upperVal"])
            # queryset = Werte.objects.filter(temperatur__range = (lowerVal, upperVal))
            queryset = Werte.objects.filter(datum__gte = vonDate, datum__lte = (bisDate + timedelta(days=1)),
                                            temperatur__lte = upperVal, temperatur__gte = lowerVal)
            
            
            return render(request, "web/temps.html", {"name": "Berg", "tempslist": list(queryset), "form": form})
        else:
            return HttpResponse(f"Error! {form.errors}")
    else:
        print("GET")
        form = TempsFilterForm()
        form.lowerVal = 4
        queryset = Werte.objects.all()
        tempListe = list(queryset)
        #print(dict(queryset))
        return render(request, "web/temps.html", {"form": form, "tempslist": tempListe})

    

