import socketio
import eventlet
from motor import Motor
sio = socketio.Server()
app = socketio.WSGIApp(sio)
motor = Motor()
st = .4
@sio.event
def connect(sid, environ):
    print('connect ', sid)

@sio.event
def forward(sid, data):
    print('message ', data)
    motor.forward(st)

@sio.event
def backward(sid, data):
    print('message ', data)
    motor.backward(st)
@sio.event
def right(sid, data):
    print('message ', data)
    motor.right(st)
@sio.event
def left(sid, data):
    print('message ', data)
    motor.left(st)

@sio.event
def disconnect(sid):
    print('disconnect ', sid)

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 8000)), app)
