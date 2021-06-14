from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('sorted', views.sorted, name='sorted'),
    path('filtered', views.filtered, name='filtered'),
]