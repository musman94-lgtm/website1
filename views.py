from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def hi(request):
    return render(request,'DEMOAPP/hi.html')

def home(request):
    context = {}
    return render(request,'DEMOAPP/home.html')

def alice(request):
    context = {}
    return render(request,'DEMOAPP/alice.html')
