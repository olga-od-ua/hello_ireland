from django.shortcuts import render

from products.models import ProductReview, Product

# Create your views here.
""" A view to render the About Us page """

def about(request):
    reviews = ProductReview.objects.all()

    context = {
        'reviews': reviews,
    }

    return render(request, "about/about_us.html", context)
