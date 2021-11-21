from django.urls import path

from . import views

urlpatterns = [
    path('job/start', views.start),
    path('healthz', views.healthz),
]
