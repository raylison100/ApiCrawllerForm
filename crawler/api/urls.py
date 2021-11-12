from django.urls import path

from . import views

urlpatterns = [
    path('job/start', views.start),
]
