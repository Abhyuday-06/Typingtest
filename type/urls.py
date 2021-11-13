from django.urls import path

from . import views

appname= 'test'

urlpatterns = [
    path('', views.text_display, name = 'main'),
    ]
