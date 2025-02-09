#Self created

from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Hello World<h1>")

def ab(request):
    return HttpResponse(f"about hello world".title())