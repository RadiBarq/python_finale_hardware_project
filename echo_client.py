import socketio
import time
# standard Python
sio = socketio.Client()
sio.connect('http://0.0.0.0:8000')


sio.emit('forward', 'foo')

time.sleep(1)
sio.disconnect()
