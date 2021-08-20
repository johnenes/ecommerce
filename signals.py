from django.dispatch import Signal
'this handles all the ip addres request'
object_viewed_signal = Signal(providing_args=['instance', 'request'])
