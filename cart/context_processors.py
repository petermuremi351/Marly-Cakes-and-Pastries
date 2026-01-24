from .cart import Cart

# create context processors so that our cart can work on all pages
def cart(request):
    # return the default data from our cart
    return {'cart': Cart(request)}