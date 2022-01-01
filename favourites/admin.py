""" A Module to register models for
the Favourites app """
from django.contrib import admin
from .models import FavouriteProductsList, FavouriteProduct


# Register your models here.
admin.site.register(FavouriteProductsList)
admin.site.register(FavouriteProduct)
