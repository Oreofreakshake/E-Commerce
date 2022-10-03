from django.shortcuts import render

from .models import Product

# Create your views here.


def product_view(request):
    obj = Product.objects.get(id=1)
    context = {"object": obj}
    return render(request, "products/products.html", context)
