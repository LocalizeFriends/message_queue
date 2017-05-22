import requests
import json
import time
from pprint import pprint

FCM_AUTH_KEY = 'AAAAzZSlrBo:APA91bG_XUO5t1s5J-k3NxP08jec0dSxSJAylGSD4DGRTA9pUs99mxHgiZT2DSTUixOTPliMPaTS_92z83jiEYXlcPHv4w0-PfiAFAMHZqVtyfz0IiutBO-Ian5lAY7JOnw1eBX4iRTm'

def send_fcm_message(fcm_ids, message):
    pprint(fcm_ids)
    pprint(message)
    for fcm_id in fcm_ids:
        post_data = json.dumps({
            'to': fcm_id,
            'data': message
        })
        headers = {
            'Content-type': 'application/json',
            'Authorization': 'key={}'.format(FCM_AUTH_KEY)
        }
        res = requests.post('https://fcm.googleapis.com/fcm/send', data=post_data, headers=headers)
        print(res.json())
