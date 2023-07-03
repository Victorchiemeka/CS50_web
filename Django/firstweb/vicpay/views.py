from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"vicpay/index.html")

def pay(request):
    return HttpResponse("select payment method")

def greet(request,name):
    return render(request, "vicpay/greet.html", {
        "name": name.capitalize()
    })