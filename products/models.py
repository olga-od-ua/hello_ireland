""" A Module for models related to products"""
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """ A Class for Product Category """
    class Meta:
        """ A Meta Class to customise Category fields """
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """ A Product Model for manipulating data
    related to a single product """
    category = models.ForeignKey('Category', null=True,
                                 blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    location = models.CharField(max_length=254)
    description = models.TextField()
    has_frame_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2,
                                 null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def calc_rating(self):
        total = sum([int(review.rating) for review in self.reviews.all()])

        if self.reviews.count() > 0:
            return total / self.reviews.count()
        else:
            return 0


class ProductReview(models.Model):
    """ A model for mainaining a signle product review data """
    product = models.ForeignKey(Product, related_name='reviews',
                                on_delete=models.CASCADE)
    user_name = models.ForeignKey(User, related_name='reviews',
                                  on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=3, decimal_places=2,
                                 null=True, blank=True)
    review_message = models.TextField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.product.name, self.user_name)
