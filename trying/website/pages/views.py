from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(*args,**kwargs):
 return HttpResponse("<h1>hello world its workking</h1>")

def home(request):
  return render (request, 'home.html')
  

def about(request):
  return HttpResponse('about page')

def contact_us(request):
 return HttpResponse('contact_us page')

def product (request):
  return HttpResponse('product page')
