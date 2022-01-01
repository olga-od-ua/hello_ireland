from django.shortcuts import (
    render,
    redirect,
    reverse,
    HttpResponseRedirect,
    get_object_or_404)
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from products.models import Product
from .models import FavouriteProductsList, FavouriteProduct


# Create your views here.
@login_required()
def favourites(request):
    """
    This view renders the user's list of
    favourite products.
    """
    favourites = None

    try:
        favourites = FavouriteProductsList.objects.get(user=request.user)
    except FavouriteProductsList.DoesNotExist:
        pass

    context = {
        'favourites': favourites,
    }

    return render(request, 'favourites/favourites.html', context)


@login_required()
def add_to_favourites(request, product_id):
    """
    This view allows users to add products to
    their list of favourite products.
    """
    product = get_object_or_404(Product, pk=product_id)

    favourites, created = FavouriteProductsList.objects.get_or_create(user=request.user)

    if FavouriteProduct.objects.filter(favourites=favourites, product=product).exists():
        messages.error(request,
                       f'"{product.name}" is already in your '
                       '"Favourites List"')
        return redirect(reverse('product_details', args=[product.id]))
    else:
        favourites.products.add(product)
        messages.success(request,
                         f'"{product.name}" added to Your Favourites! '
                         'Don\'t forget to come back for it!')
        return redirect(reverse('product_details', args=[product.id]))


@login_required()
def remove_from_favourites(request, product_id):
    """
    This view allows users to remove products from
    their list of favourite products.
    """
    product = get_object_or_404(Product, pk=product_id)

    favourites, created = FavouriteProductsList.objects.get_or_create(user=request.user)
    favourites.products.remove(product)
    messages.success(request,
                     f'"{product.name}" removed from Your Favourites.')

    return HttpResponseRedirect(request.META['HTTP_REFERER'])
