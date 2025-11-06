from django.urls import path

from . import views

urlpatterns = [
    path("luke_skywalker/", views.get_luke_info),
]
