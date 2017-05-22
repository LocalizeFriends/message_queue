import zmq
import requests
from pprint import pprint
import traceback
from operations import send_fcm_message

context = zmq.Context()
socket = context.socket(zmq.PULL)
socket.bind("tcp://127.0.0.1:5678")

handlers = {
    'send_fcm_message': send_fcm_message
}

while True:
    message = socket.recv_json()
    print("Received request: ")
    pprint(message)

    handler = handlers.get(message['operation'])
    if handler is not None:
        try:
            handler(**message['arguments'])
        except:
            traceback.print_exc()
