from django.urls import path

from . import views, views_classbased

urlpatterns = [
    path("rest_home/", views.rest_home, name="rest_home"),
    path("", views.apiDescription, name="indexAPIDescription"),
    path("list_all_werte/", views_classbased.WerteListAPIView.as_view()),
    path("create_wert/", views_classbased.WertCreateAPIView.as_view()),
    path("list_create_wert/", views_classbased.WerteListCreateAPIView.as_view()),
    path("retrieve_wert/<int:pk>/", views_classbased.WertDetailRetrieveAPIView.as_view()),
    path("update_wert/<int:pk>", views_classbased.WertUpdateAPIView.as_view()),
    path("delete_wert/<int:pk>", views_classbased.WertDeleteAPIView.as_view()),
    path("create_sensor/", views_classbased.SensorCreateAPIView.as_view()),
    path("readbyid/<str:werte_id>/", views.readById, name="readById"),
    path("update/<str:werte_id>/", views.update, name="update"),
    path("delete/<str:werte_id>/", views.delete, name="delete"),

]