from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path("showtemps/", views.display_temps),
    path("showpress/", views.show_press),
    path('showhumid/', views.show_humidity),
    path("sensors/", views.display_sensors),
    path("showtemps/<str:sensor_id>/", views.sensordetail, name="temp_detail"),
    path("showpress/<str:sensor_id>/", views.sensordetail, name="press_detail"),
    path('showhumid/<str:sensor_id>/', views.sensordetail, name="humid_detail"),
    path('sensors/editsensor/<str:sensor_id>/', views.edit_sensor_details),
    path('sensors/sensor_new/', views.create_sensor),
]