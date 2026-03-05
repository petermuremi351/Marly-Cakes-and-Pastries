from django.apps import AppConfig


class PaymentConfig(AppConfig):
    name = 'payment'

    # set up paypal IPN signal
    def ready(self):
        import payment.hooks
