from django.contrib import admin
from .models import Pizza, Order, OrderPizza

class PizzaOrderInlineAdmin(admin.TabularInline):
    model = OrderPizza
    extra = 2

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'address', 'status']
    list_filter = ['status']
    inlines = (PizzaOrderInlineAdmin,)

# Register your models here.
admin.site.register(Pizza)
admin.site.register(Order, OrderAdmin)
