import os
from aiohttp import web
import motor.motor_asyncio
import socketio
from json import dumps, loads

while(True):
	try:
		mgr = socketio.AsyncRedisManager('redis://redis')
	except:
		print("redis is not responding, trying again in 1 sec...")
		sleep(1)
		continue
	break

mgr = socketio.AsyncRedisManager('redis://redis')
sio = socketio.AsyncServer(client_manager=mgr)
app = web.Application()
sio.attach(app)
client = motor.motor_asyncio.AsyncIOMotorClient("mongodb")
db = client.messages
logged_in_users = {}

async def index(request):
	"""Serve the client-side application."""
	with open('index.html') as f:
		return web.Response(text=os.environ["SERVICE_NAME"], content_type='text/html')

@sio.on('connect', namespace='/chat')
def connect(sid, environ):
	pass

@sio.on('enter room', namespace="/chat")
async def enter_room(sid, data):
	print ("entering to room")
	sio.enter_room(sid, data['room'], namespace="/chat")

@sio.on('login', namespace="/chat")
async def login(sid, data):
	print ("user logged in")
	logged_in_users[sid] = data['username']
	await sio.emit('loggedInChanged', {'data': dumps(logged_in_users)}, room=data['room'], namespace='/chat')

@sio.on('logout', namespace="/chat")
async def logout(sid, data):
	print ("user logged out")
	del logged_in_users[sid]
	await sio.emit('loggedInChanged', {'data': dumps(logged_in_users)}, room=data['room'], namespace='/chat')

@sio.on('leave room', namespace="/chat")
async def leave_room(sid, data):
	print ("leaving the room")
	sio.leave_room(sid, data['room'], namespace="/chat")

@sio.on('chat message', namespace='/chat')
async def message(sid, data):
	print("message ", data, os.environ["SERVICE_NAME"])
	document = {'key': 'value'}
	await db.test_collection.insert_one(document)
	await sio.emit('reply', {'data': data}, room=data['room'], namespace='/chat', skip_sid=sid)
	print("after await")

@sio.on('disconnect', namespace='/chat')
def disconnect(sid):
	print('disconnect ', sid)
	del logged_in_users[sid]
	sio.emit('loggedInChanged', {'data': dumps(logged_in_users)}, namespace='/chat')

app.router.add_get('/', index)

if __name__ == '__main__':
	web.run_app(app, port=80)
