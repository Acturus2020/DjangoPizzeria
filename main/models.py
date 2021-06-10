from django.db import models

# Create your models here.


class Pizza(models.Model):
    name = models.CharField('Name of pizza', max_length=30, default='Pizza')
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Pizza'
        verbose_name_plural = "Pizzas"


class OrderPizza(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    order = models.ForeignKey("Order", on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=1)


class Order(models.Model):

    STATUS_VARIANTS= {
        ('is_pending', 'pending'),
        ('is_completed', 'completed'),
        ('is_canceled', 'canceled')
    }
    address = models.CharField(max_length=100)
    pizzas = models.ManyToManyField(Pizza, through=OrderPizza)
    status = models.CharField(max_length=30, choices=STATUS_VARIANTS)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = "Orders"

