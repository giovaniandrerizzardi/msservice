import socketio
from flask_socketio import SocketIOTestClient
sio = socketio.Client()


@sio.event
def connect():
    print('connection established')

@sio.event
def disconnect():
    print('disconnected from server')
    return 1

#SocketIOTestClient.connect('http://localhost:5000')
#SocketIOTestClient.emit("teste", "EV_276")

sio.connect('http://localhost:7877')
sio.emit("teste", "EV_276")
sio.wait()

sio.disconnect()
