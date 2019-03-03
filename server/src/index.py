from aiohttp import web
import socketio

sio = socketio.AsyncServer()
app = web.Application()
sio.attach(app)

async def index(request):
	"""Serve the client-side application."""
	with open('index.html') as f:
		return web.Response(text=f.read(), content_type='text/html')

@sio.on('connect', namespace='/chat')
def connect(sid, environ):
	pass

@sio.on('enter room', namespace="/chat")
async def enter_room(sid, data):
	print ("entering to room")
	sio.enter_room(sid, data['room'], namespace="/chat")

@sio.on('leave room', namespace="/chat")
async def leave_room(sid, data):
	print ("leaving the room")
	sio.leave_room(sid, data['room'], namespace="/chat")

@sio.on('chat message', namespace='/chat')
async def message(sid, data):
	print("message ", data)
	await sio.emit('reply', {'data': data}, room=data['room'], namespace='/chat', skip_sid=sid)
	print("after await")

@sio.on('disconnect', namespace='/chat')
def disconnect(sid):
	print('disconnect ', sid)

app.router.add_static('/static', 'static')
app.router.add_get('/', index)

async def get_chat_id():
    return "chat-%s" % "ehsan"

if __name__ == '__main__':
	web.run_app(app)