import django.dispatch

asns_message_received = django.dispatch.Signal(providing_args=["message"])
