from flask import Flask,render_template,jsonify,request

app=Flask(__name__)

server_jack_status=[]
server_stock_status=[]
server_cup_size_status=[]
conveyer_speed_status_stock_status=[]
opc_server_error_status_status=[]
master_count_pots_status=[]


@app.route('/jack',methods=['POST'])
def recv_jack_from_server():
    request_data=request.get_json()
    jack_status={'name':request_data['name'],'status':request_data['status']}
    server_jack_status.append(jack_status)
    return jsonify(jack_status)

@app.route('/jack')
def visualise_jack_status_positive():
    return jsonify({'jack':server_jack_status})

@app.route('/no_jack',methods=['POST'])
def negative_recv_jack_from_server():
    request_data=request.get_json()
    jack_status={'name':request_data['name'],'status':request_data['status']}
    server_jack_status.append(jack_status)
    return jsonify(jack_status)



@app.route('/no_jack')
def visualise_jack_status_negative():
    return jsonify({'jack':server_jack_status})

@app.route('/gui2_power')
def power_button():
    return jsonify({'message':'press the power button'})

@app.route('/no_stock',methods=['POST'])
def negative_recv_stock_from_server():
    request_data=request.get_json()
    stock_status={'name':request_data['name'],'status':request_data['status']}
    server_stock_status.append(stock_status)
    return jsonify(stock_status)

@app.route('/stock',methods=['POST'])
def recv_stock_from_server():
    request_data=request.get_json()
    stock_status={'name':request_data['name'],'status':request_data['status']}
    server_stock_status.append(stock_status)
    return jsonify(stock_status)

@app.route('/stock')
def visualise_stock_status_positive():
    return jsonify({'stock':server_stock_status})

@app.route('/no_stock')
def visualise_stock_status_negative():
    return jsonify({'stock':server_stock_status})


@app.route('/gui2_cup_size_info')
def cup_size():
    #return "select 1 for small, 2 for medium, 3 for large"
    return jsonify({'select_1':'small','select_2':'medium','select_3':'large'})

@app.route('/gui2_cup_number_info')
def cup_number():
    #return "tray has 10 cups available"
    return jsonify({'available_cups':10})

@app.route('/gui2_cup_size',methods=['POST'])
def recv_cup_size():
    request_data=request.get_json()
    cup_size_status={'cup_size':request_data['cup_size']}
    server_cup_size_status.append(cup_size_status)
    return jsonify(cup_size_status)

@app.route('/gui2_cup_size')
def visualise_cup_size_status():
    return jsonify({'cup_size':server_cup_size_status})

@app.route('/gui2_no_stock')
def no_cup_stock():
    #return "no cups are available"
    return jsonify({'available_cups':0})


@app.route('/gui2_speed_info_set')
def conveyer_speed():
    #return "set a speed for the conveyer"
    return jsonify({'select_speed_in_m/s':[]})

@app.route('/gui2_speed_info',methods=['POST'])
def recv_conveyer_speed():
    request_data=request.get_json()
    conveyer_speed_status={'speed_in_m/s':request_data['speed_in_m/s']}
    conveyer_speed_status_stock_status.append(conveyer_speed_status)
    return jsonify(conveyer_speed_status)

@app.route('/gui2_speed_info')
def visualise_conveyer_speed():
    return jsonify({'speed_in_m/s':conveyer_speed_status_stock_status})

@app.route('/opc_server_errors')
def server_errors():
    #return "starting belt,starting arm,checking error,checking air fault status,air fault doesn't exist all well,checking axis controller fault"
    return jsonify({'starting_belt':[],'starting_arm':[],'checking_error':[],'checking_air_fault_status':[],'checking_axis_controller_fault':[]})


@app.route('/server_errors',methods=['POST'])
def recv_server_errors():
    request_data=request.get_json()
    server_error_status={'starting_belt':request_data['starting_belt'],
    'starting_arm':request_data['starting_arm'],
    'checking_error':request_data['checking_error'],
    'checking_air_fault_status':request_data['checking_air_fault_status'],
    'checking_axis_controller_fault':request_data['checking_axis_controller_fault']}
    opc_server_error_status_status.append(server_error_status)
    return jsonify(server_error_status)

@app.route('/server_errors')
def visualise_opc_server_error_status_status():
    return jsonify({'data':opc_server_error_status_status})

@app.route('/count_pots_request')
def count_pots():
    return jsonify({'count_pots_status':[]})


@app.route('/count_pots',methods=['POST'])
def recv_count_pots():
    request_data=request.get_json()
    count_pots_status={'serial_number_of_incoming_pots':request_data['serial_number_of_incoming_pots']}
    master_count_pots_status.append(count_pots_status)
    return jsonify(count_pots_status)

@app.route('/count_pots')
def visualise_count_pots_status():
    return jsonify({'data':master_count_pots_status})

app.run(port=5001)