from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from django.shortcuts import get_object_or_404
from products.models import Product


# Create your views here.


def view_bag(request):
    """ A view that renders the shopping bag contents page """

    return render(request, 'shopping_bag/shopping_bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    shopping_bag = request.session.get('shopping_bag', {})

    if size:
        if item_id in list(shopping_bag.keys()):
            if size in shopping_bag[item_id]['items_by_size'].keys():
                shopping_bag[item_id]['items_by_size'][size] += quantity
            else:
                shopping_bag[item_id]['items_by_size'][size] = quantity
        else:
            shopping_bag[item_id] = {'items_by_size': {size: quantity}}
            messages.success(
                request, f'Added {product.name} to your shopping bag')

    else:
        if item_id in list(shopping_bag.keys()):
            shopping_bag[item_id] += quantity
        else:
            shopping_bag[item_id] = quantity

    request.session['shopping_bag'] = shopping_bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Adjust quantity of a specified product in the shopping bag """

    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    shopping_bag = request.session.get('shopping_bag', {})

    if size:
        if quantity > 0:
            shopping_bag[item_id]['items_by_size'][size] = quantity
        else:
            del shopping_bag[item_id]['items_by_size'][size]
            if not shopping_bag[item_id]['items_by_size']:
                shopping_bag.pop(item_id)
    else:
        if quantity > 0:
            shopping_bag[item_id] = quantity
        else:
            shopping_bag.pop(item_id)

    request.session['shopping_bag'] = shopping_bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """ Remove a specified item from the shopping bag """

    try:
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        shopping_bag = request.session.get('shopping_bag', {})

        if size:
            del shopping_bag[item_id]['items_by_size'][size]
            if not shopping_bag[item_id]['items_by_size']:
                shopping_bag.pop(item_id)
        else:
            shopping_bag.pop(item_id)

        request.session['shopping_bag'] = shopping_bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
