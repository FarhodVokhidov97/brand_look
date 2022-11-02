from .cart import Cart


def cart(request):
    cart = Cart(request)
    cart_products_id = []
    cart_product_number = None

    if cart:
        cart_products_id = cart.cart.keys()
        cart_products_id = list(map(lambda el: int(el), cart_products_id))
        cart_product_number = len(cart_products_id)

    context = {
        'cart': cart,
        'cart_products_id': cart_products_id,
        'cart_product_number': cart_product_number,
    }
    return context
