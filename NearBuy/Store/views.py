from django.shortcuts import render
from Product.models import Product
# Create your views here.
def home(request):
    products = Product.objects.all().filter(is_available=True)
    return render(request,'Store/home.html',{'products':products})
