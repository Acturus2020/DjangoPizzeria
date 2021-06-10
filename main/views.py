from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza
# Create your views here.

def index(request):
    Pizzas = Pizza.objects.all()
    return render(request,'main/index.html', {'Pizzas': Pizzas})

def about(request):
    # return HttpResponse('<h4>Page about us<h4>')
    return render(request, 'main/about.html')