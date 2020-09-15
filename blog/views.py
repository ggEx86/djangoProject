from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.

def home(request):
    return HttpResponse('<h1>Blog homepage</h1>')

def about(request):
    return HttpResponse('<h1>Blog about page</h1>')
