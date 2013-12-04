import urllib2
import traceback
from base64 import b64decode

from M2Crypto import X509

from asnsreceiver.signals import asns_message_received


def verify_message(msg):
    try:
        cert_res = urllib2.urlopen(msg['SigningCertURL'])
        signature = cert_res.read()
    except (urllib2.HTTPError, IOError):  # Can't open the URL
        return False

    message = u''
    if msg['Type'] == 'SubscriptionConfirmation':
        message += 'Message\n'
        message += msg['Message'] + '\n'
        message += 'MessageId\n'
        message += msg['MessageId'] + '\n'
        message += 'SubscribeURL\n'
        message += msg['SubscribeURL'] + '\n'
        message += 'Timestamp\n'
        message += msg['Timestamp'] + '\n'
        message += 'Token\n'
        message += msg['Token'] + '\n'
        message += 'TopicArn\n'
        message += msg['TopicArn'] + '\n'
        message += 'Type\n'
        message += msg['Type'] + '\n'
    elif msg['Type'] == 'Notification':
        message += 'Message\n'
        message += msg['Message'] + '\n'
        message += 'MessageId\n'
        message += msg['MessageId'] + '\n'
        if msg['Subject'] != '':
            message += 'Subject\n'
            message += msg['Subject'] + '\n'
        message += 'Timestamp\n'
        message += msg['Timestamp'] + '\n'
        message += 'TopicArn\n'
        message += msg['TopicArn'] + '\n'
        message += 'Type\n'
        message += msg['Type'] + '\n'

    cert = X509.load_cert_string(str(signature))
    pubkey = cert.get_pubkey()
    pubkey.reset_context(md='sha1')
    pubkey.verify_init()
    pubkey.verify_update(message.encode())
    result = pubkey.verify_final(b64decode(msg['Signature']))
    if result != 1:
        return False
    else:
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
