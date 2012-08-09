from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('asnsreceiver.views',
    url(r'^asns/notify/$', 'receive_notification', name='asns-receive-notification'),
)
