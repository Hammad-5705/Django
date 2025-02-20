from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Blog_Home(request):
    return render(request,"Blog/home.html")