from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from cart.forms import CartAddProductForm
from shop.models import Product
from .models import OrderItem
from .forms import OrderCreateForm
from django.views.generic import FormView
from cart.cart import Cart
from django.urls import reverse_lazy


class OrderCreate(FormView):
    template_name = 'orders/create.html'
    form_class = OrderCreateForm

    def form_valid(self, form):
        cart = Cart(self.request)
        order = form.save()
        context = {
            'cart': cart,
            'order': order
        }

        for item in cart:
            OrderItem.objects.create(order=order,
                                     product=item['product'],
                                     price=item['price'],
                                     quantity=item['quantity'])
        cart.clear()
        return render(self.request, 'orders/created.html', context)
        # {'order': order}, {'cart': cart})

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        return self.render_to_response(self.get_context_data(form=form))


    