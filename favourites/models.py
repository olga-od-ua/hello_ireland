""" A Module for Models related to
the Favourites app """
from django.db import models
from django.contrib.auth.models import User
from products.models import Product


# Create your models here.
class FavouriteProductsList(models.Model):
    """
    This model represents a list of
    favourite products of a given user.
    """

    user = models.OneToOneField(
        User,
        null=False,
        blank=False,
        related_name='favourites',
        on_delete=models.CASCADE)

    products = models.ManyToManyField(
        Product,
        default="",
        through='FavouriteProduct')

    def __str__(self):
        return f'Favourite products ({self.user})'


class FavouriteProduct(models.Model):
    """
    This model defines a single product
    added by a particular user to their
    Favourite Products list.
    """

    favourites = models.ForeignKey(
        FavouriteProductsList,
        null=False,
        blank=False,
        related_name='favourite_products',
        on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product,
        null=False,
        blank=False,
        related_name='favourite_product',
        on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name
