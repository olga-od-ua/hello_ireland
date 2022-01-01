""" A module to contain all url patterns for About Us page """
from django.urls import path
from . import views


urlpatterns = [
    path('about/', views.about, name='about'),
]
