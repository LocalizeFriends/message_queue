import time
import zmq
from pprint import pprint

context = zmq.Context()
socket = context.socket(zmq.PULL)
socket.bind("tcp://*:5555")

while True:
    message = socket.recv_json()
    print("Received request: ")
    pprint(message)
