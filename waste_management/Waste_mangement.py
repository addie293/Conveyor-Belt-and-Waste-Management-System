from flask import Flask,render_template,jsonify,request

app=Flask(__name__)

conveying_pot_status=[]
filling_potting_status=[]
packaging_status=[]



@app.route('/pot',methods=['POST'])
def recv_pot_status_from_conveying():
    request_data=request.get_json()
    pot_status={'name':request_data['name'],'status':request_data['status']}
    conveying_pot_status.append(pot_status)
    return jsonify(pot_status)

@app.route('/pot')
def visualise_pot_status_positive():
    return jsonify({'pot':conveying_pot_status})

@app.route('/broken_pot',methods=['POST'])
def negative_recv_pot_from_server():
    request_data=request.get_json()
    pot_status={'name':request_data['name'],'status':request_data['status']}
    conveying_pot_status.append(pot_status)
    return jsonify(pot_status)



@app.route('/broken_pot')
def visualise_pot_status_negative():
    return jsonify({'pot':conveying_pot_status})


@app.route('/filling_potting',methods=['POST'])
def filling_potting_workshop():
    request_data=request.get_json()
    filling_potting={'name':request_data['name'],'status':request_data['status']}
    filling_potting_status.append(filling_potting)
    return jsonify(filling_potting)

#{"amount":10,"name":"caps","status":"broken"}

@app.route('/filling_potting')
def visualise_filling_potting():
    return jsonify({'details':filling_potting_status})

@app.route('/packaging',methods=['POST'])
def filling_potting():
    request_data=request.get_json()
    packaging={'details':request_data['details']}
    packaging_status.append(packaging)
    return jsonify(packaging)

@app.route('/packaging')
def visualise_packaging():
    return jsonify({'details':packaging_status})



app.run(port=5002)