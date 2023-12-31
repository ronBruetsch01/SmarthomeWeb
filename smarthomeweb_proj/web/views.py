from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Sensor, Werte
from web.forms.TempsFilterForm import TempsFilterForm
# from web.forms.HumidsFilterForm import HumidsFilterForm
from web.forms.SensorCreateEditModelForm import SensorCreateEditModelForm
from django.db.models import Max, Min
from django.contrib.auth import authenticate
from datetime import datetime, timedelta

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is None:
            return render(request, "web/login.html")
        else:
            return redirect(index)
    else:
        return render(request, 'web/login.html')

def index(request):
    # return HttpResponse("Hello, world. You're at the web app.")
    return render(request, 'web/index.html')

def display_sensors(request):
    queryset = Sensor.objects.all()
    return render(request, "web/sensors.html", {"sensorlist": list(queryset)})

def create_sensor(request):
    
    if request.method == "POST":
        form = SensorCreateEditModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/web/sensors")
    else: 
        form = SensorCreateEditModelForm()
        return render(request, "web/sensor_edit.html", {"form": form})
    
def sensordetail(request, sensor_id):
    queryset = Sensor.objects.get(pk=sensor_id)
    print(queryset.sen_raum)
    return render(request, "web/sensorDetails.html", {"data": {"sensorId": sensor_id, "sensor": queryset}})


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
            
            
            return render(request, "web/temps.html", {"page_name": "Temperatur", "tempslist": list(queryset), "form": form})
        else:
            return HttpResponse(f"Error! {form.errors}")
    else:
        print("GET")
        form = TempsFilterForm()
        form.lowerVal = 4
        queryset = Werte.objects.all()
        tempListe = list(queryset)
        #print(dict(queryset))
        print (tempListe)
        return render(request, "web/temps.html", {"page_name": "Temperatur", "form": form, "tempslist": tempListe})

def show_press(request):
    if request.method == "POST":
        form = TempsFilterForm(request.POST) 

        if form.is_valid():
            lowerVal = form.cleaned_data["lowerVal"]
            if lowerVal is None:
                lowerVal = Werte.objects.aggregate(Min('luftdruck'))["luftdruck__min"]

            upperVal = form.cleaned_data["upperVal"]
            if upperVal is None:
                upperVal = Werte.objects.aggregate(Max('luftdruck'))["luftdruck__max"]
            
            vonDate = form.cleaned_data["vonDate"]
            bisDate = form.cleaned_data["bisDate"]

            queryset = Werte.objects.filter(datum__gte=vonDate, datum__lte=(bisDate + timedelta(days=1)),
                                            luftdruck__lte=upperVal, luftdruck__gte=lowerVal)
            
            return render(request, "web/pressure.html", {"page_name": "Luftdruck", "pressList": list(queryset), "form": form})
            
    else:
        form = TempsFilterForm()
        queryset = Werte.objects.all()
        pressList = list(queryset)
        return render(request, "web/pressure.html", {"page_name": "Luftdruck", "form": form, "pressList": pressList})
    
def show_humidity(request):
    if request.method == "POST":
        pass
    else:
        form = TempsFilterForm()
        queryset = Werte.objects.all()
        humidityList = list(queryset)
        return render(request, "web/humidity.html", {"page_name": "Luftfeuchtigkeit", "form": form, "humidityList":humidityList })