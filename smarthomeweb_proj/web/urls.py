from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path("showtemps/", views.display_temps),
    path("sensors/", views.display_sensors),
    path("showtemps/<str:temp_id>/", views.tempdetails, name="temp_detail"),
    path('sensors/editsensor/<str:sensor_id>/', views.edit_sensor_details)
]