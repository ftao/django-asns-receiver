curl -v -X POST --data @sample_subscribe_confirm.json  \
    http://127.0.0.1:8000/receiver/asns/notify/

curl -v -X POST --data @sample_notification.json  \
    http://127.0.0.1:8000/receiver/asns/notify/



