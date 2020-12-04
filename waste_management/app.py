from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit, send
import json

from random import randint

variables = {"Test1": {"value": 1, "type": "int"},
             "Test2": {"value": 2, "type": "bool"},
             "Test3": {"value": 2, "type": "bool"},
             "Test4": {"value": 2, "type": "bool"},
             "Test5": {"value": 2, "type": "bool"},
             "Test6": {"value": 2, "type": "bool"},
             "Test7": {"value": 2, "type": "bool"},
             "Test8": {"value": 2, "type": "bool"},
             "Test9": {"value": 2, "type": "bool"},
             "Test10": {"value": 2, "type": "bool"},
             "Test11": {"value": 2, "type": "bool"}
             }

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@socketio.on('connect')
def io_connect():
    pass


@socketio.on('get_update_data')
def io_get_update_data():
    for key in variables.keys():
        variables[key]['value'] = randint(0, 256)
    emit('update_data', json.dumps(variables))


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/GUI1/')
def gui1():
    return render_template('GUI1.html', variables=variables)


@app.route('/GUI2/')
def gui2():
    return render_template('gui2e.html', variables=variables)


@app.route('/COM1/')
def com1():
    return ""


@app.route('/COM2/')
def com2():
    return ""


@app.route('/COM3/')
def com3():
    return jsonify(variables)


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5001)
