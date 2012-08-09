# Create your views here.
try:
    import json
except ImportError:
    import simpjson as json

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest, HttpResponse
from asnsreceiver.models import verify_message, process_subscription, process_notification

@csrf_exempt
def receive_notification(request):
    msg = json.loads(request.raw_post_data)

    if not verify_message(msg):
        return HttpResponseBadRequest('bad request')

    if msg['Type'] == 'SubscriptionConfirmation':
        if process_subscription(msg):
            return HttpResponse('SubscriptionConfirmation OK')
        else:
            return HttpResponse('SubscriptionConfirmation Failed')
    elif msg['Type'] == 'Notification':
        process_notification(msg)
        return HttpResponse(json.dumps({
            'error' : 0,
            'msg' : msg
        }))

