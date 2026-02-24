from flask import Flask, render_template, jsonify, request
from flask_socketio import SocketIO, emit
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vtuber-toolkit-secret'
socketio = SocketIO(app, cors_allowed_origins="*")

# Storage
chat_messages = []
alerts = []
obs_config = {'host': 'localhost', 'port': 4455, 'password': ''}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/overlay')
def overlay():
    return render_template('overlay.html')

@app.route('/alerts')
def alerts_page():
    return render_template('alerts.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/api/chat', methods=['GET', 'POST'])
def chat():
    global chat_messages
    if request.method == 'POST':
        msg = request.json
        msg['id'] = len(chat_messages)
        msg['timestamp'] = time.time()
        chat_messages.append(msg)
        if len(chat_messages) > 100:
            chat_messages = chat_messages[-100:]
        socketio.emit('new_message', msg)
        return jsonify({'status': 'ok'})
    return jsonify(chat_messages[-50:])

@app.route('/api/alerts', methods=['GET', 'POST'])
def handle_alerts():
    global alerts
    if request.method == 'POST':
        alert = request.json
        alert['id'] = len(alerts)
        alert['timestamp'] = time.time()
        alerts.append(alert)
        socketio.emit('new_alert', alert)
        return jsonify({'status': 'ok'})
    return jsonify(alerts[-10:])

@app.route('/api/obs/config', methods=['GET', 'POST'])
def obs_config_route():
    global obs_config
    if request.method == 'POST':
        obs_config.update(request.json)
        return jsonify({'status': 'ok'})
    return jsonify(obs_config)

@socketio.on('connect')
def handle_connect():
    emit('connected', {'data': 'VTuber Toolkit Connected'})

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)
