from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def t(request):
    #return HttpResponse("<p>Hello</p>")
    return render(request,'app1/index.html')