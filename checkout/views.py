from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    shopping_bag = request.session.get('shopping_bag', {})
    if not shopping_bag:
        messages.error(
            request, "There's nothing in your shopping bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51K2ka9H3lf8zmiXAyhcOjRqtfrMnxOylWxW3ofYc5Z3ODni0ApfqxVC0bMpy8uWbKnHwPuHkrxOCv0sX1TDMTPBh00Be82TPRa',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
