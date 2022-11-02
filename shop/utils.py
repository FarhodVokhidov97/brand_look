from .models import *
from cart.forms import *


class DataMixin:
    paginate_by = 30

    def get_user_context(self, **kwargs):
        context = kwargs
        context['cart_product_form'] = CartAddProductForm()
        if 'cat_selected' not in context:
            context['cat_selected'] = None
        return context



