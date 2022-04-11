
from flask import Flask, redirect, render_template, request, session, url_for
from flask_socketio import SocketIO, send, emit, join_room, leave_room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html' )

@app.route('/chat', methods=['GET','POST'])
def chat():
    if(request.method=='POST'):
        session['username'] = request.form['username']
        session['room'] = request.form['room']
        return render_template('chat.html', username=session['username'], room=session['room'])
    else:
        session.clear()
        return redirect(url_for('/'))
    

@socketio.on('message')
def handle_message(data):
    print('receiveddas message: ' + data)

@socketio.on('message')
def handle_message(message):
    print('Message:', message)
    send(message,broadcast=True)

@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')

# @socketio.on('join')
# def on_join(data):
#     username = data['username']
#     room = data['room']
#     join_room(room)
#     send(username + ' has entered the room.', to=room)

# @socketio.on('leave')
# def on_leave(data):
#     username = data['username']
#     room = data['room']
#     leave_room(room)
#     send(username + ' has left the room.', to=room)

if __name__ == '__main__':
    socketio.run(app)
