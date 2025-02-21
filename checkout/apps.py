from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    """App Config for Checkout"""
    name = 'checkout'

    def ready(self):
        import checkout.signals
