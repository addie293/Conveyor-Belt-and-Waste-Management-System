from opcua import Client
import time
client = Client("opc.tcp://127.0.0.1:9090")
client.connect()
print("Connected to OPC Database: Real Workshop Values Incoming")
while True:
    size = client.get_node("ns=2;i=1")
    cup_size = size.get_value()
    print("Data Fed to Internal Process: "+cup_size)
    time.sleep(3)


