""" A Module to generate url paths
related to the Products page """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_details, name='product_details'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/',
         views.delete_product,
         name='delete_product'),
    path('<int:product_id>/add_review/', views.add_review, name='add_review'),
    path('<int:product_id>/delete_review/',
         views.delete_review,
         name='delete_review'),
]
