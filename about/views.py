""" A module for all views related to
About Us page and functionality """
from django.shortcuts import render

from products.models import ProductReview


# Create your views here.
def about(request):
    """ A view to render the About Us page """

    reviews = ProductReview.objects.all()

    context = {
        'reviews': reviews,
    }

    return render(request, "about/about_us.html", context)
