import json
from random import randint

from flask import Flask, render_template, jsonify
from flask_socketio import SocketIO, emit
from gevent.pywsgi import WSGIServer

import internal_process

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

internal_process.init()


@socketio.on('connect')
def io_connect():
    pass


@socketio.on('get_update_data')
def io_get_update_data():
    # internal_process.variables['Vérine_Verte']['value'] = True if randint(0, 1) == 1 else False
    emit('update_data', json.dumps(internal_process.get_variables()))


@socketio.on('set_data')
def io_set_data(data):
    dt = json.loads(data)
    internal_process.set_variable(dt)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/GUI1/')
def gui1():
    return render_template('GUI1.html', variables=internal_process.get_variables())


@app.route('/GUI2/')
def gui2():
    return render_template('gui2e.html', variables=internal_process.get_variables())


@app.route('/COM1/')
def com1():
    return ""


@app.route('/COM2/', methods=['GET'])
def com2_get_all():
    return jsonify(internal_process.get_variables()), 200


@app.route('/COM2/<path:request>', methods=['GET'])
def com2_get(request: str):
    s = request.split("/")
    res = {}
    keys = internal_process.get_variables().keys()
    for k in s:
        if k in keys:
            res[k] = internal_process.get_variables()[k]
    if len(res) > 0:
        return jsonify(res), 200
    return jsonify({"message": "non existent resource asked"}), 400


@app.route('/COM2/<path:request>', methods=['post'])
def com2_post(request: str):
    s = request.split("/")
    res = {}
    keys = internal_process.get_variables().keys()
    for o in s:
        k = o.split("=")
        if len(k) == 2 and k[0] in keys:
            res[k[0]] = k[1]

    if len(res) > 0:
        for k, v in res:
            internal_process.get_variables()[k] = v
        return jsonify({"message": "non existent resource asked"}), 200
    return jsonify({"message": "non existent resource asked"}), 400


@app.route('/COM3/')
def com3():
    return ""


if __name__ == '__main__':
    # socketio.run(app, host='0.0.0.0', port=5000)
    http_server = WSGIServer(('0.0.0.0', 5000), app)
    http_server.serve_forever()