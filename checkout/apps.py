""" A Module for application configuration for the Checkout app """
from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """ A Class for application configuration for the Checkout app"""
    name = 'checkout'

    def ready(self):
        import checkout.signals
