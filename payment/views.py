from django.shortcuts import render, redirect
from cart.cart import Cart
from payment.forms import ShippingForm, PaymentForm
from payment.models import ShippingAddress, Order, OrderItem
from django.contrib.auth.models import User
from django.contrib import messages
from store.models import Product


def process_order(request):
    if request.POST:
        cart = Cart(request)
        cart_products = cart.get_prods
        quantities = cart.get_quants
        totals = cart.cart_total()
        # get billing info from last page
        payment_form = PaymentForm(request.POST or None)
        # get shipiping data
        my_shipping = request.session.get("my_shipping")
        # gather order information
        full_name = my_shipping["shipping_full_name"]
        email = my_shipping["shipping_email"]
        # create shipping address from session info
        shipping_address = f"{my_shipping['shipping_address1']}\n{my_shipping['shipping_address2']}\n{my_shipping['shipping_city']}\n{my_shipping['shipping_state']}\n{my_shipping['shipping_zipcode']}\n{my_shipping['shipping_country']}"
        amount_paid = totals
        user = None

        if request.user.is_authenticated:
            # logged in
            user = request.user
            # Create an order
            create_order = Order(
                user=user,
                full_name=full_name,
                email=email,
                shipping_address=shipping_address,
                amount_paid=amount_paid,
            )
            create_order.save()

            # add order items
            order_id = create_order.pk
            for product in cart_products():
                product_id = product.id
                if product.is_sale:
                    price = product.sale_price
                else:
                    price = product.price

                for key, value in quantities().items():
                    if int(key) == product_id:
                        create_order_item = OrderItem(
                            order_id=order_id,
                            product_id=product_id,
                            user=user,
                            quantity=value,
                            price=price * value,
                        )
                        create_order_item.save()  # ✅ FIXED LINE
            # delete our cart
            for key in list(request.session.keys()):
                if key == "session_key":
                    # delete the key
                    del request.session[key]

            messages.success(request, "Order Placed!")
            return redirect("home")

        else:
            # not logged in
            create_order = Order(
                user=user,
                full_name=full_name,
                email=email,
                shipping_address=shipping_address,
                amount_paid=amount_paid,
            )
            create_order.save()

            order_id = create_order.pk
            for product in cart_products():
                product_id = product.id
                if product.is_sale:
                    price = product.sale_price
                else:
                    price = product.price

                for key, value in quantities().items():
                    if int(key) == product_id:
                        create_order_item = OrderItem(
                            order_id=order_id,
                            product_id=product_id,
                            quantity=value,
                            price=price * value,
                        )
                        create_order_item.save()
            for key in list(request.session.keys()):
                if key == "session_key":
                    # delete the key
                    del request.session[key]
        messages.success(request, "Order Placed!")
        return redirect("home")

    else:
        messages.success(request, "Access Denied")
        return redirect("home")


# def process_order(request):
#     if request.POST:
#         cart = Cart(request)
#         cart_products = cart.get_prods
#         quantities = cart.get_quants
#         totals = cart.cart_total()
#         # get billing info from last page
#         payment_form = PaymentForm(request.POST or None)
#         # get shipiping data
#         my_shipping = request.session.get('my_shipping')
#         # gather order information
#         full_name = my_shipping['shipping_full_name']
#         email = my_shipping['shipping_email']
#         # create shipping address from session info
#         shipping_address = f"{my_shipping['shipping_address1']}\n{my_shipping['shipping_address2']}\n{my_shipping['shipping_city']}\n{my_shipping['shipping_state']}\n{my_shipping['shipping_zipcode']}\n{my_shipping['shipping_country']}"
#         amount_paid = totals


#         if request.user.is_authenticated:
#             # loggrd in
#             user = request.user
#             # Create an order
#             create_order = Order(user=user, full_name=full_name,email=email, shipping_address=shipping_address, amount_paid=amount_paid)
#             create_order.save()

#             # add order items
#             # get order id
#             order_id = create_order.pk
#             # get product info
#             for product in cart_products():
#                 # get product id
#                 product_id = product.id
#                 # get product price
#                 if product.is_sale:
#                     price = product.sale_price
#                 else:
#                     price = product.price

#                 # get quantity
#                 for key,value in quantities().items():
#                     if int(key) == product_id:
#                         # create order item
#                         create_order_item = OrderItem(order_id=order_id, product_id=product_id, user=user, quantity=value, price=price)
#                         create_order.save()


#             messages.success(request, "Order Placed!")
#             return redirect('home')

#         else:
#             # not logged
#             # create order
#             create_order = Order(user=user, full_name=full_name,email=email, shipping_address=shipping_address, amount_paid=amount_paid)
#             create_order.save()

#             # add order items
#             # get order id
#             order_id = create_order.pk
#             # get product info
#             for product in cart_products():
#                 # get product id
#                 product_id = product.id
#                 # get product price
#                 if product.is_sale:
#                     price = product.sale_price
#                 else:
#                     price = product.price

#                 # get quantity
#                 for key,value in quantities().items():
#                     if int(key) == product_id:
#                         # create order item
#                         create_order_item = OrderItem(order_id=order_id, product_id=product_id, quantity=value, price=price)
#                         create_order_item.save()


#         messages.success(request, "Order Placed!")
#         return redirect('home')


#     else:
#         messages.success(request, "Access Denied")
#         return redirect('home')

# def process_order(request):
#     if request.method == "POST":
#         cart = Cart(request)
#         cart_products = cart.get_prods()
#         quantities = cart.get_quants()
#         totals = cart.cart_total()

#         my_shipping = request.session.get('my_shipping')

#         full_name = my_shipping['shipping_full_name']
#         email = my_shipping['shipping_email']

#         shipping_address = (
#             f"{my_shipping['shipping_address1']}\n"
#             f"{my_shipping['shipping_address2']}\n"
#             f"{my_shipping['shipping_city']}\n"
#             f"{my_shipping['shipping_state']}\n"
#             f"{my_shipping['shipping_zipcode']}\n"
#             f"{my_shipping['shipping_country']}"
#         )

#         user = request.user if request.user.is_authenticated else None

#         # CREATE ORDER
#         order = Order.objects.create(
#             user=user,
#             full_name=full_name,
#             email=email,
#             shipping_address=shipping_address,
#             amount_paid=totals
#         )

#         # CREATE ORDER ITEMS
#         for product in cart_products:
#             product_id = product.id
#             price = product.sale_price if product.is_sale else product.price
#             quantity = quantities.get(str(product_id))

#             OrderItem.objects.create(
#                 order=order,
#                 product=product,
#                 user=user,
#                 quantity=quantity,
#                 price=price
#             )

#         messages.success(request, "Order Placed!")
#         return redirect('home')
#     # delete our cart
#     for key in list(request.session.keys()):
#         # delete the key
#         del request.session[key]

#     messages.error(request, "Access Denied")
#     return redirect('home')


def billing_info(request):
    if request.POST:
        cart = Cart(request)
        cart_products = cart.get_prods
        quantities = cart.get_quants
        totals = cart.cart_total()

        # create a session with shipping info
        my_shipping = request.POST
        request.session["my_shipping"] = my_shipping

        # check to see if user is logged in
        if request.user.is_authenticated:
            # get the billing form
            billing_form = PaymentForm()
            return render(
                request,
                "billing_info.html",
                {
                    "cart_products": cart_products,
                    "quantities": quantities,
                    "totals": totals,
                    "shipping_info": request.POST,
                    "billing_form": billing_form,
                },
            )
        else:
            # not logged in
            # get the billing form
            billing_form = PaymentForm()
            return render(
                request,
                "billing_info.html",
                {
                    "cart_products": cart_products,
                    "quantities": quantities,
                    "totals": totals,
                    "shipping_info": request.POST,
                    "billing_form": billing_form,
                },
            )

            pass

        shipping_form = request.POST
        return render(
            request,
            "billing_info.html",
            {
                "cart_products": cart_products,
                "quantities": quantities,
                "totals": totals,
                "shipping_form": shipping_form,
            },
        )
    else:
        messages.success(request, "Access Denied")
        return redirect("home")


def payment_success(request):
    return render(request, "payment_success.html", {})


def checkout(request):
    # get the cart
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    totals = cart.cart_total()

    if request.user.is_authenticated:
        # checkout as logged in user
        shipping_user = ShippingAddress.objects.get(user__id=request.user.id)
        shipping_form = ShippingForm(request.POST or None, instance=shipping_user)
        return render(
            request,
            "checkout.html",
            {
                "cart_products": cart_products,
                "quantities": quantities,
                "totals": totals,
                "shipping_form": shipping_form,
            },
        )
    else:
        # checkout of guest
        shipping_form = ShippingForm(request.POST or None)
        return render(
            request,
            "checkout.html",
            {
                "cart_products": cart_products,
                "quantities": quantities,
                "totals": totals,
                "shipping_form": shipping_form,
            },
        )

    return render(
        request,
        "checkout.html",
        {"cart_products": cart_products, "quantities": quantities, "totals": totals},
    )

    return render(request, "checkout.html", {})
