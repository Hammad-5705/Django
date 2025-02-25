from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


# Create your views here.
def shop_home(request):
    return render(request,"Alpino_Store/home.html")

def about(request):
    return HttpResponse("about")
    
def contact(request):
    return HttpResponse("contact")
    
def tracker():
    return HttpResponse("tracker")

def search(request):
    return HttpResponse("request")

def product_view(request):
    return HttpResponse("product view")
    
def checkout(request):
    return HttpResponse("checkout")

#Task to view models on Home page
def task01(request):  
    products = Product.objects.all()  
    data = {"products": products}
    return render(request, "task01.html", data)  
