from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza
from django.views.generic import TemplateView
# Create your views here.


def index(request):
    Pizzas = Pizza.objects.all()
    return render(request, 'main/index.html', {'Pizzas': Pizzas})


def sorted(request):
    Pizzas = Pizza.objects.order_by('-name')
    return render(request, 'main/sorted.html', {'Pizzas': Pizzas})


def filtered(request):
    Pizzas = Pizza.objects.filter(name__contains='pizza')
    return render(request, 'main/filtered.html', {'Pizzas': Pizzas})


class BasePizzaTemplate(TemplateView):
    def get_context_data(self, **kwargs):
        create_pizza = self.request.GET.get('create_pizza') == "yes"
        if create_pizza:
            Pizza.objects.create(
                name='new pizza',
                price=123
            )
