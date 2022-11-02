from django.db import models
from shop.models import Product


DELIVERY_CHOICES = [
        ('delivery1', 'доставка по почте'),
        ('delivery2', 'доставка курьером'),
        ('delivery3', 'Адрес на доставку'),
        ]

PAY_CHOICES = [
    ('pay1', 'Оплата по карте'),
    ('pay2', 'Оплата наличными'),
]


class Order(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Name')
    last_name = models.CharField(max_length=50, verbose_name='Surname')
    email = models.EmailField(verbose_name='Email')
    address = models.CharField(max_length=250, verbose_name='address')
    phone_number = models.CharField(max_length=20, verbose_name='Phone number')
    city = models.CharField(max_length=100, verbose_name='City')
    delivery_method = models.CharField(choices=DELIVERY_CHOICES, max_length=50, default='delivery1',
                                       verbose_name='Delivery method')
    pay_method = models.CharField(choices=PAY_CHOICES, max_length=50, default='pay1', verbose_name='Pay method')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'order'
        verbose_name_plural = 'orders'

    def __str__(self):
        return f'Order {self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.PROTECT)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.id}'

    def get_cost(self):
        return self.price * self.quantity
