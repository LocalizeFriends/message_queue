import zmq

def send_fcm_messages(fcm_ids, message):
    context = zmq.Context()
    socket = context.socket(zmq.PUSH)
    socket.connect("tcp://localhost:5555")

    socket.send_json({
        'operation': 'send_fcm_messages',
        'arguments': {
            'fcm_ids': fcm_ids,
            'message': message
        }
    })

send_fcm_messages(['aaa', 'bbb'], { 'xd': 'aaa', 'vvv': 'vbb' })

# #  Do 10 requests, waiting each time for a response
# for request in range(5):
#     print("Sending request %s …" % request)
#     socket.send(b"Hello1")
#
#     #  Get the reply.
#     message = socket.recv()
#     print("Received reply %s [ %s ]" % (request, message))
