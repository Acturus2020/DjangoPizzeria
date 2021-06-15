from django.urls import path
from django.conf.urls import url
from . import views
from .views import PizzaView, PizzaDetailView

urlpatterns = [
    path('', views.index, name='home'),
    path('sorted', views.sorted, name='sorted'),
    path('filtered', views.filtered, name='filtered'),
    url(r'^pizzas/$', PizzaView.as_view()),
    url(r'^pizzas/(?P<pizza_id>\w+)/', PizzaDetailView.as_view()),
]
