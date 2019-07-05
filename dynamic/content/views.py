from django.shortcuts import render
from .models import dynamo

# Create your views here.

def index(request):
    dest = dynamo()
    dest.name = "Mumbai"
    dest.desc = "The City That Sleeps"
    dest.price = 300
    return render(request,"index.html",{'dest1': dest})

