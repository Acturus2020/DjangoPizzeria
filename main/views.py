from django.shortcuts import render
from .models import Pizza
from django.views.generic import TemplateView
import requests
# Create your views here.


def index(request):
    # print(kwa)
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
        context = super().get_context_data(**kwargs)
        context['pizzas'] = Pizza.objects.all()
        create_pizza = self.request.GET.get('create_pizza') == "yes"
        if create_pizza:
            Pizza.objects.create(
                name='new pizza',
                price=123
            )
        delete_pizza = self.request.GET.get('delete_pizza') == "yes"
        if delete_pizza:
            del_pizza = Pizza.objects.all().order_by('?').first()
            del_pizza.delete()
        return context

class PizzaView(BasePizzaTemplate):
    template_name = "main/index.html"


class PizzaDetailView(TemplateView):
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pizza'] = Pizza.objects.get(id=kwargs.get('pizza_id'))
        return context
