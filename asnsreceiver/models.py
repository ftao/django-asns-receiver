import urllib2
import traceback
from asnsreceiver.signals import asns_message_received

def verify_message(msg):
    return True

def process_subscription(msg):
    try:
        urllib2.urlopen(msg['SubscribeURL']).read()
        return True
    except IOError:
        traceback.print_exc()
        return False

def process_notification(msg):
    asns_message_received.send("ProcessNotificationSender", message=msg) 
