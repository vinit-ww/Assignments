from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from django.views.decorators.http import require_POST
from .models import Category,ProductCategories,Product,ProductImage,Brand
from django.contrib.auth import logout
from .cart import Cart
from .forms import CartAddProductForm

def subcategories_list(request,id=None):
    category_set=Category.objects.all()
    product=Product.objects.all()
    product_images=ProductImage.objects.all()
    product_category_set=ProductCategories.objects.all()
    instance=get_object_or_404(Category,id=id)
    context = {

        'categories':category_set,
        'product':product,
        'product_images':product_images,
        "instance": instance,
        "product_category_set": product_category_set,
    }
    return render(request, "shopify/subcategorylist.html", context)

@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/')

def products(request):
    category_set = Category.objects.all()
    product = Product.objects.all()
    product_images = ProductImage.objects.all()
    product_category_set = ProductCategories.objects.all()
    # instance = get_object_or_404(Category, id=id)
    context = {

        'categories': category_set,
        'product': product,
        'product_images': product_images,
        # "instance": instance,
        'user':request.user,
        "product_category_set": product_category_set,
    }

    return render(request, "shopify/shop.html", context)

def brands(request,id):
    b=get_object_or_404(Brand,id=id)
    product_images = ProductImage.objects.all()
    context = {

        'product_images': product_images,
        # "instance": instance,
        'brand':b,
        # 'product_category_set': product_category_set,
    }
    return render(request, "shopify/brands.html", context)


def cart_add(request, id=None):
    cart = Cart(request)
    # cart.clear()
    product = get_object_or_404(Product, id=id)
    product_image = get_object_or_404(ProductImage,id=id)
    cart.add(product,product_image)
    return redirect('shopify:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('shopify:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'shopify/cart.html', {'cart': cart})


