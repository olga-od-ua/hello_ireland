from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from datetime import datetime
from django.contrib.auth.models import User

from .models import Product, Category, ProductReview
from .forms import ProductForm, ProductReviewForm
from favourites.models import FavouriteProductsList, FavouriteProduct


# Create your views here.
def all_products(request):
    """ A view too return all products, their sorting and search results """

    products = Product.objects.all()

    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, "products/products.html", context)


def product_details(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    
    fav = bool

    if request.user.is_authenticated:
        favourites, created = FavouriteProductsList.objects.get_or_create(user=request.user)
        if FavouriteProduct.objects.filter(favourites=favourites, product=product).exists():
            fav = True

    reviews_count = ProductReview.objects.filter(product=product).count()
    context = {
        'product': product,
        'reviews_count': reviews_count,
        'fav': fav,
    }

    return render(request, 'products/product_details.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'You are not authorised to perform this action.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_details', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'You are not authorised to perform this action.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_details', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'You are not authorised to perform this action.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, f'"{product.name}" deleted!')
    return redirect(reverse('products'))


def add_review(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        form = ProductReviewForm(request.POST)

        if form.is_valid():
            form = ProductReviewForm(request.POST)
            review = form.save(commit=False)
            review.user_name = request.user
            review.product = product
            review.save()
            messages.success(request, f'Review successfully submitted for {product.name}')
            return redirect(reverse('product_details', args=[product.id]))
        else:
            messages.error(request, 'Ensure the form is valid.')
    else:
        form = ProductReviewForm()
        messages.info(request, f'You are reviewing {product.name}')

    template = 'products/add_review.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def delete_review(request, product_id):
    """ Delete a review the logged in user submitted"""
    review = get_object_or_404(ProductReview, pk=product_id)
    review.delete()
    messages.success(request, f'Review deleted!')
    return redirect(reverse('product_details', args=[review.product.id]))
