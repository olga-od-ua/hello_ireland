from django.shortcuts import render

# Create your views here.
""" A view to render the About Us page """

def about(request):
    return render(request, "about/about_us.html")
