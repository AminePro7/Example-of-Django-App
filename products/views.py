from django.shortcuts import render
from .models import Product
def products(request):
    return render(request,'products/products.html',{'data' : Product.objects.all()})

def product(request):
    return(render(request,'products/product.html'))