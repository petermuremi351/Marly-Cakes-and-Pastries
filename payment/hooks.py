from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received
from django.dispatch import receiver
from django.conf import settings
import time
from .models import Order

@receiver(valid_ipn_received)
def paypal_payment_received(sender, **kwargs):
    # a 10 seconds to wait paypal to send ipn data
    time.sleep(10)

    # grap the info that paypal sends
    paypal_obj = sender
    # get the invoice
    my_Invoice = str(paypal_obj.invoice)

    # match the paypal invoice to Order invoice
    # look up the Order
    my_Order = Order.objects.get(invoice=my_Invoice)

    # Record the Order paid
    my_Order.paid = True
    # save the Order
    my_Order.save()




    # print(paypal_obj)
    # print(f'Amount Paid: {paypal_obj.mc_gross}')