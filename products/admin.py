""" A Module for registering models for
the Products app in the Admin panel """
from django.contrib import admin
from .models import Product, Category, ProductReview


class ProductAdmin(admin.ModelAdmin):
    """ A Class for displaying Product fields
    and ordering them by sku in the admin panel."""
    list_display = (
        'sku',
        'name',
        'location',
        'category',
        'has_frame_sizes',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    """ A Class for displaying Category fields
    in the admin panel."""
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductReview)
