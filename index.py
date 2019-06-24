from processors import decoder
from flask import Flask, render_template
from flask_socketio import SocketIO, disconnect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@socketio.on('connect')
def test_connect():
    socketio.emit('my response', {'data': 'Connected'})
    
@socketio.on('teste')
def handle_message(teste):
    print('received message: ' + teste)
    print("Sending Event code to processor")
    decoder.processData_decode(teste)
    disconnect()
    

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')



if __name__ == '__main__':
    socketio.run(app)

