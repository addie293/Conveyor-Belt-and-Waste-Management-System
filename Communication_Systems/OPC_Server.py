from opcua import Server
import time
server = Server()

server.set_endpoint("opc.tcp://127.0.0.1:9090")

addspace = server.register_namespace("SIMULATION_SERVER")

node = server.get_objects_node()

Param = node.add_object(addspace, "Parameters")

val = Param.add_variable(addspace, "Cup Size", 0)

val.set_writable()

server.start()
print("Values being transferred to the internal process as follows:-")

while True:
      Value={"Small Cup", "Medium Cup", "Large Cup"}
      for x in Value:
         print('Size of Cup Available in the Real Workshop is: '+ x)  # x is a str
         val.set_value(Value)
         time.sleep(3)
