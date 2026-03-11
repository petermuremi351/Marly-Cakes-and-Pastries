# from django.shortcuts import render, redirect
# from cart.cart import Cart
# from payment.forms import ShippingForm, PaymentForm
# from payment.models import ShippingAddress, Order, OrderItem
# from django.contrib.auth.models import User
# from django.contrib import messages
# from store.models import Product, Profile
# from django.http import HttpResponse
# from .utils import render_to_pdf
# import datetime

# # import some paypal staff
# from django.urls import reverse
# from paypal.standard.forms import PayPalPaymentsForm
# from django.conf import settings
# # unique user id for duplicate
# import uuid 


# def orders(request, pk):
#     if request.user.is_authenticated and request.user.is_superuser:
#         # get the order
#         order = Order.objects.get(id=pk)
#         # get the order items
#         items = OrderItem.objects.filter(order=pk)
#         if request.POST:
#             status = request.POST['shipping_status']
#             # check if true or False
#             if status == "true":
#                 # get the order
#                 order = Order.objects.filter(id=pk)
#                 # update the status
#                 now = datetime.datetime.now()
#                 order.update(shipped=True, date_shipped=now)
#             else:
#                 # get the order
#                 order = Order.objects.filter(id=pk)
#                 # update the status
#                 order.update(shipped=False)
#             messages.success(request, "shipping Status Updated")
#             return redirect('home')    
                
                    
#         return render(request, 'orders.html', {"order":order, "items":items})
#     else:
#         messages.success(request, "Access Denied")
#         return redirect("home")

    

# def unshipped_orders_pdf(request):
#     if not request.user.is_superuser:
#         return HttpResponse("Access Denied")

#     orders = Order.objects.filter(shipped=False)

#     pdf = render_to_pdf(
#         "invoices/orders_invoice.html",
#         {
#             "orders": orders,
#             "title": "UNSHIPPED ORDERS INVOICE"
#         }
#     )

#     response = HttpResponse(pdf, content_type="application/pdf")
#     response["Content-Disposition"] = "attachment; filename=unshipped_orders.pdf"
#     return response


# def shipped_orders_pdf(request):
#     if not request.user.is_superuser:
#         return HttpResponse("Access Denied")

#     orders = Order.objects.filter(shipped=True)

#     pdf = render_to_pdf(
#         "invoices/orders_invoice.html",
#         {
#             "orders": orders,
#             "title": "SHIPPED ORDERS INVOICE"
#         }
#     )

#     response = HttpResponse(pdf, content_type="application/pdf")
#     response["Content-Disposition"] = "attachment; filename=shipped_orders.pdf"
#     return response


# def not_shipped_dash(request):
#     if request.user.is_authenticated and request.user.is_superuser:
#         orders = Order.objects.filter(shipped=False)
#         if request.POST:
#             status = request.POST['shipping_status']
#             num = request.POST['num']
#             # get the Order
#             order = Order.objects.filter(id=num)
#             # grab time
#             now = datetime.datetime.now()
#             # update order
#             order.update(shipped=True, date_shipped=now)
#             messages.success(request, "shipping Status Updated")
#             return redirect('home')
#         return render(request, "not_shipped_dash.html", {"orders":orders})
#     else:
#         messages.success(request, "Access Denied")
#         return redirect("home")


# def shipped_dash(request):
#     if request.user.is_authenticated and request.user.is_superuser:
#         orders = Order.objects.filter(shipped=True)
#         if request.POST:
#             status = request.POST['shipping_status']
#             num = request.POST['num']
#             # get the Order
#             order = Order.objects.filter(id=num)
#             # grab time
#             now = datetime.datetime.now()
#             # update order
#             order.update(shipped=False, date_shipped=now)
#             messages.success(request, "shipping Status Updated")
#             return redirect('home')
#         return render(request, "shipped_dash.html", {"orders":orders})
#     else:
#         messages.success(request, "Access Denied")
#         return redirect("home")


# def process_order(request):
#     if request.POST:
#         cart = Cart(request)
#         cart_products = cart.get_prods
#         quantities = cart.get_quants
#         totals = cart.cart_total()
#         # get billing info from last page
#         payment_form = PaymentForm(request.POST or None)
#         # get shipiping data
#         my_shipping = request.session.get("my_shipping")
#         # gather order information
#         full_name = my_shipping["shipping_full_name"]
#         email = my_shipping["shipping_email"]
#         # create shipping address from session info
#         shipping_address = f"{my_shipping['shipping_address1']}\n{my_shipping['shipping_address2']}\n{my_shipping['shipping_city']}\n{my_shipping['shipping_state']}\n{my_shipping['shipping_zipcode']}\n{my_shipping['shipping_country']}"
#         amount_paid = totals
#         user = None

#         if request.user.is_authenticated:
#             # logged in
#             user = request.user
#             # Create an order
#             create_order = Order(
#                 user=user,
#                 full_name=full_name,
#                 email=email,
#                 shipping_address=shipping_address,
#                 amount_paid=amount_paid,
#             )
#             create_order.save()

#             # add order items
#             order_id = create_order.pk
#             for product in cart_products():
#                 product_id = product.id
#                 if product.is_sale:
#                     price = product.sale_price
#                 else:
#                     price = product.price

#                 for key, value in quantities().items():
#                     if int(key) == product_id:
#                         create_order_item = OrderItem(
#                             order_id=order_id,
#                             product_id=product_id,
#                             user=user,
#                             quantity=value,
#                             price=price * value,
#                         )
#                         create_order_item.save()  # ✅ FIXED LINE
#             # delete our cart
#             for key in list(request.session.keys()):
#                 if key == "session_key":
#                     # delete the key
#                     del request.session[key]

#             # delete cart from db(old cart)
#             current_user = Profile.objects.filter(user__id=request.user.id)
#             # delete shopping cart from db(od cart)
#             current_user.update(old_cart="")


                    

#             messages.success(request, "Order Placed!")
#             return redirect("home")

#         else:
#             # not logged in
#             create_order = Order(
#                 user=user,
#                 full_name=full_name,
#                 email=email,
#                 shipping_address=shipping_address,
#                 amount_paid=amount_paid,
#             )
#             create_order.save()

#             order_id = create_order.pk
#             for product in cart_products():
#                 product_id = product.id
#                 if product.is_sale:
#                     price = product.sale_price
#                 else:
#                     price = product.price

#                 for key, value in quantities().items():
#                     if int(key) == product_id:
#                         create_order_item = OrderItem(
#                             order_id=order_id,
#                             product_id=product_id,
#                             quantity=value,
#                             price=price * value,
#                         )
#                         create_order_item.save()
#             for key in list(request.session.keys()):
#                 if key == "session_key":
#                     # delete the key
#                     del request.session[key]
#         messages.success(request, "Order Placed!")
#         return redirect("home")

#     else:
#         messages.success(request, "Access Denied")
#         return redirect("home")


# def billing_info(request):
#     if request.POST:
#         cart = Cart(request)
#         cart_products = cart.get_prods
#         quantities = cart.get_quants
#         totals = cart.cart_total()

#         # create a session with shipping info
#         my_shipping = request.POST
#         request.session["my_shipping"] = my_shipping

#         # get the host
#         host = request.get_host()
#         # create invoice number
#         my_Invoice = str(uuid.uuid4())

#         # create paypal form dictionary
#         paypal_dict = {
#             'business': settings.PAYPAL_RECEIVER_EMAIL,
#             'amount': totals,
#             'item_name': 'Cake Order',
#             'no_shipping': '2',
#             'invoice': my_Invoice,
#             'currency_code': 'USD', 
#             'notify_url': 'https://{}{}'.format(host, reverse("paypal-ipn")),
#             'return_url': 'https://{}{}'.format(host, reverse("payment_success")),
#             'cancel_return': 'https://{}{}'.format(host, reverse("payment_failed")),

#         }

#         # create actual paypal button
#         paypal_form = PayPalPaymentsForm(initial=paypal_dict)


#         # check to see if user is logged in
#         if request.user.is_authenticated:
#             # get the billing form
#             billing_form = PaymentForm()
#             return render(
#                 request,
#                 "billing_info.html",
#                 {
#                     "cart_products": cart_products,
#                     "quantities": quantities,
#                     "totals": totals,
#                     "shipping_info": request.POST,
#                     "billing_form": billing_form,
#                     "paypal_form":paypal_form,
#                 },
#             )
#         else:
#             # not logged in
#             # get the billing form
#             billing_form = PaymentForm()
#             return render(
#                 request,
#                 "billing_info.html",
#                 {
#                     "cart_products": cart_products,
#                     "quantities": quantities,
#                     "totals": totals,
#                     "shipping_info": request.POST,
#                     "billing_form": billing_form,
#                     "paypal_form":paypal_form,
#                 },
#             )

#             pass

#         shipping_form = request.POST
#         return render(
#             request,
#             "billing_info.html",
#             {
#                 "cart_products": cart_products,
#                 "quantities": quantities,
#                 "totals": totals,
#                 "shipping_form": shipping_form,
#             },
#         )
#     else:
#         messages.success(request, "Access Denied")
#         return redirect("home")


# def payment_success(request):
#     return render(request, "payment_success.html", {})

# def payment_failed(request):
#     return render(request, "payment_failed.html", {})


# def checkout(request):
#     # get the cart
#     cart = Cart(request)
#     cart_products = cart.get_prods
#     quantities = cart.get_quants
#     totals = cart.cart_total()

#     if request.user.is_authenticated:
#         # checkout as logged in user
#         shipping_user = ShippingAddress.objects.get(user__id=request.user.id)
#         shipping_form = ShippingForm(request.POST or None, instance=shipping_user)
#         return render(
#             request,
#             "checkout.html",
#             {
#                 "cart_products": cart_products,
#                 "quantities": quantities,
#                 "totals": totals,
#                 "shipping_form": shipping_form,
#             },
#         )
#     else:
#         # checkout of guest
#         shipping_form = ShippingForm(request.POST or None)
#         return render(
#             request,
#             "checkout.html",
#             {
#                 "cart_products": cart_products,
#                 "quantities": quantities,
#                 "totals": totals,
#                 "shipping_form": shipping_form,
#             },
#         )

#     return render(
#         request,
#         "checkout.html",
#         {"cart_products": cart_products, "quantities": quantities, "totals": totals},
#     )

#     return render(request, "checkout.html", {})

from django.shortcuts import render, redirect
from cart.cart import Cart
from payment.forms import ShippingForm, PaymentForm
from payment.models import ShippingAddress, Order, OrderItem
from django.contrib.auth.models import User
from django.contrib import messages
from store.models import Product, Profile
import datetime

# Import Some Paypal Stuff
from django.urls import reverse
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
import uuid # unique user id for duplictate orders

# mpesa daraja
from django.http import HttpResponse
from django_daraja.mpesa.core import MpesaClient
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# # views for mpesa
# def mpesa_payment(request):
#     cl = MpesaClient()
#     # Use a Safaricom phone number that you have access to, for you to be able to view the prompt.
#     phone_number = '254708374149'
#     amount = 1
#     account_reference = 'reference'
#     transaction_desc = 'Description'
#     callback_url = 'https://api.darajambili.com/express-payment'
#     response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
#     return HttpResponse(response)
cl = MpesaClient()

def mpesa_payment(request):
    phone_number = '254708374149'  # sandbox number
    amount = 1
    account_reference = 'Order123'
    transaction_desc = 'Cake Purchase'
    callback_url = 'https://doretta-unpulverable-eldora.ngrok-free.dev/payment/callback/'

    try:
        response = cl.stk_push(
            phone_number=phone_number,
            amount=amount,
            account_reference=account_reference,
            transaction_desc=transaction_desc,
            callback_url=callback_url
        )
        return JsonResponse({"message": response.response_description})
    except Exception as e:
        return JsonResponse({"error": str(e)})

@csrf_exempt  # Daraja sends POST from outside, so CSRF is skipped
def mpesa_callback(request):
    if request.method == "POST":
        data = json.loads(request.body)
        # Here you can parse the payment result and update your order
        print("STK Push callback received:", data)
        # Example: mark order as paid
        # order = Order.objects.get(id=data['AccountReference'])
        # order.status = 'Paid'
        # order.save()
        return JsonResponse({"Result": "Success"})
    return JsonResponse({"error": "Invalid request"})

def unshipped_orders_pdf(request):
    if not request.user.is_superuser:
        return HttpResponse("Access Denied")

    orders = Order.objects.filter(shipped=False)

    pdf = render_to_pdf(
        "invoices/orders_invoice.html",
        {
            "orders": orders,
            "title": "UNSHIPPED ORDERS INVOICE"
        }
    )

    response = HttpResponse(pdf, content_type="application/pdf")
    response["Content-Disposition"] = "attachment; filename=unshipped_orders.pdf"
    return response


def shipped_orders_pdf(request):
    if not request.user.is_superuser:
        return HttpResponse("Access Denied")

    orders = Order.objects.filter(shipped=True)

    pdf = render_to_pdf(
        "invoices/orders_invoice.html",
        {
            "orders": orders,
            "title": "SHIPPED ORDERS INVOICE"
        }
    )

    response = HttpResponse(pdf, content_type="application/pdf")
    response["Content-Disposition"] = "attachment; filename=shipped_orders.pdf"
    return response

def orders(request, pk):
	if request.user.is_authenticated and request.user.is_superuser:
		# Get the order
		order = Order.objects.get(id=pk)
		# Get the order items
		items = OrderItem.objects.filter(order=pk)

		if request.POST:
			status = request.POST['shipping_status']
			# Check if true or false
			if status == "true":
				# Get the order
				order = Order.objects.filter(id=pk)
				# Update the status
				now = datetime.datetime.now()
				order.update(shipped=True, date_shipped=now)
			else:
				# Get the order
				order = Order.objects.filter(id=pk)
				# Update the status
				order.update(shipped=False)
			messages.success(request, "Shipping Status Updated")
			return redirect('home')


		return render(request, 'orders.html', {"order":order, "items":items})




	else:
		messages.success(request, "Access Denied")
		return redirect('home')



def not_shipped_dash(request):
	if request.user.is_authenticated and request.user.is_superuser:
		orders = Order.objects.filter(shipped=False)
		if request.POST:
			status = request.POST['shipping_status']
			num = request.POST['num']
			# Get the order
			order = Order.objects.filter(id=num)
			# grab Date and time
			now = datetime.datetime.now()
			# update order
			order.update(shipped=True, date_shipped=now)
			# redirect
			messages.success(request, "Shipping Status Updated")
			return redirect('home')

		return render(request, "not_shipped_dash.html", {"orders":orders})
	else:
		messages.success(request, "Access Denied")
		return redirect('home')

def shipped_dash(request):
	if request.user.is_authenticated and request.user.is_superuser:
		orders = Order.objects.filter(shipped=True)
		if request.POST:
			status = request.POST['shipping_status']
			num = request.POST['num']
			# grab the order
			order = Order.objects.filter(id=num)
			# grab Date and time
			now = datetime.datetime.now()
			# update order
			order.update(shipped=False)
			# redirect
			messages.success(request, "Shipping Status Updated")
			return redirect('home')


		return render(request, "shipped_dash.html", {"orders":orders})
	else:
		messages.success(request, "Access Denied")
		return redirect('home')

def process_order(request):
	if request.POST:
		# Get the cart
		cart = Cart(request)
		cart_products = cart.get_prods
		quantities = cart.get_quants
		totals = cart.cart_total()

		# Get Billing Info from the last page
		payment_form = PaymentForm(request.POST or None)
		# Get Shipping Session Data
		my_shipping = request.session.get('my_shipping')

		# Gather Order Info
		full_name = my_shipping['shipping_full_name']
		email = my_shipping['shipping_email']
		# Create Shipping Address from session info
		shipping_address = f"{my_shipping['shipping_address1']}\n{my_shipping['shipping_address2']}\n{my_shipping['shipping_city']}\n{my_shipping['shipping_state']}\n{my_shipping['shipping_zipcode']}\n{my_shipping['shipping_country']}"
		amount_paid = totals

		# Create an Order
		if request.user.is_authenticated:
			# logged in
			user = request.user
			# Create Order
			create_order = Order(user=user, full_name=full_name, email=email, shipping_address=shipping_address, amount_paid=amount_paid)
			create_order.save()

			# Add order items
			
			# Get the order ID
			order_id = create_order.pk
			
			# Get product Info
			for product in cart_products():
				# Get product ID
				product_id = product.id
				# Get product price
				if product.is_sale:
					price = product.sale_price
				else:
					price = product.price

				# Get quantity
				for key,value in quantities().items():
					if int(key) == product.id:
						# Create order item
						create_order_item = OrderItem(order_id=order_id, product_id=product_id, user=user, quantity=value, price=price)
						create_order_item.save()

			# Delete our cart
			for key in list(request.session.keys()):
				if key == "session_key":
					# Delete the key
					del request.session[key]

			# Delete Cart from Database (old_cart field)
			current_user = Profile.objects.filter(user__id=request.user.id)
			# Delete shopping cart in database (old_cart field)
			current_user.update(old_cart="")


			messages.success(request, "Order Placed!")
			return redirect('home')

			

		else:
			# not logged in
			# Create Order
			create_order = Order(full_name=full_name, email=email, shipping_address=shipping_address, amount_paid=amount_paid)
			create_order.save()

			# Add order items
			
			# Get the order ID
			order_id = create_order.pk
			
			# Get product Info
			for product in cart_products():
				# Get product ID
				product_id = product.id
				# Get product price
				if product.is_sale:
					price = product.sale_price
				else:
					price = product.price

				# Get quantity
				for key,value in quantities().items():
					if int(key) == product.id:
						# Create order item
						create_order_item = OrderItem(order_id=order_id, product_id=product_id, quantity=value, price=price)
						create_order_item.save()

			# Delete our cart
			for key in list(request.session.keys()):
				if key == "session_key":
					# Delete the key
					del request.session[key]



			messages.success(request, "Order Placed!")
			return redirect('home')


	else:
		messages.success(request, "Access Denied")
		return redirect('home')

def billing_info(request):
	if request.POST:
		# Get the cart
		cart = Cart(request)
		cart_products = cart.get_prods
		quantities = cart.get_quants
		totals = cart.cart_total()

		# Create a session with Shipping Info
		my_shipping = request.POST
		request.session['my_shipping'] = my_shipping

		# Get the host
		host = request.get_host()
		# Create Paypal Form Dictionary
		paypal_dict = {
			'business': settings.PAYPAL_RECEIVER_EMAIL,
			'amount': totals,
			'item_name': 'Book Order',
			'no_shipping': '2',
			'invoice': str(uuid.uuid4()),
			'currency_code': 'USD', # EUR for Euros
			'notify_url': 'https://{}{}'.format(host, reverse("paypal-ipn")),
			'return_url': 'https://{}{}'.format(host, reverse("payment_success")),
			'cancel_return': 'https://{}{}'.format(host, reverse("payment_failed")),
		}

		# Create acutal paypal button
		paypal_form = PayPalPaymentsForm(initial=paypal_dict)


		# Check to see if user is logged in
		if request.user.is_authenticated:
			# Get The Billing Form
			billing_form = PaymentForm()
			return render(request, "billing_info.html", {"paypal_form":paypal_form, "cart_products":cart_products, "quantities":quantities, "totals":totals, "shipping_info":request.POST, "billing_form":billing_form})

		else:
			# Not logged in
			# Get The Billing Form
			billing_form = PaymentForm()
			return render(request, "billing_info.html", {"paypal_form":paypal_form, "cart_products":cart_products, "quantities":quantities, "totals":totals, "shipping_info":request.POST, "billing_form":billing_form})


		
		shipping_form = request.POST
		return render(request, "billing_info.html", {"cart_products":cart_products, "quantities":quantities, "totals":totals, "shipping_form":shipping_form})	
	else:
		messages.success(request, "Access Denied")
		return redirect('home')


def checkout(request):
	# Get the cart
	cart = Cart(request)
	cart_products = cart.get_prods
	quantities = cart.get_quants
	totals = cart.cart_total()

	if request.user.is_authenticated:
		# Checkout as logged in user
		# Shipping User
		shipping_user = ShippingAddress.objects.get(user__id=request.user.id)
		# Shipping Form
		shipping_form = ShippingForm(request.POST or None, instance=shipping_user)
		return render(request, "checkout.html", {"cart_products":cart_products, "quantities":quantities, "totals":totals, "shipping_form":shipping_form })
	else:
		# Checkout as guest
		shipping_form = ShippingForm(request.POST or None)
		return render(request, "checkout.html", {"cart_products":cart_products, "quantities":quantities, "totals":totals, "shipping_form":shipping_form})

	

def payment_success(request):
	# delete browser Cart
	# get the Cart
	cart = Cart(request)
	cart_products = cart.get_prods
	quantities = cart.get_quants
	totals = cart.cart_total()

	# delete our cart
	for key in list(request.session.keys()):
		if key == "session_key":
			# delete the key
			del request.session[key]
			
	return render(request, "payment_success.html", {})


def payment_failed(request):
	return render(request, "payment_failed.html", {})
