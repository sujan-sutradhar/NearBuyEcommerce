from django.shortcuts import render,get_object_or_404
from Product.models import Product ,Category

# Create your views here.

def store(request,category_slug=None):
    categories = None
    products  = None
    if category_slug !=None:
         categories= get_object_or_404(Category,slug=category_slug)
         products = Product.objects.filter(category=categories,is_available=True)
         prod_count=products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        prod_count=products.count()
    categories = Category.objects.all()
    context={
        'products':products,
        'prod_count':prod_count,
        'categories':categories
        }
    
    return render(request,'Store/store.html',context)
def product_details(request,category_slug,product_slug):
     try:
          product = Product.objects.get(category__slug=category_slug,slug=product_slug)
     except Exception as e :
          raise e
     context={
          'product':product
     }
     return render(request,'Store/product_details.html',context)





