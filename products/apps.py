""" A Module for application configuration for the Products app """
from django.apps import AppConfig


class ProductsConfig(AppConfig):
    """ A Class for application configuration for the Products app"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'
