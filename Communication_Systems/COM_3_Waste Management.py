import socket
import time
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('0.0.0.0', 8080))
serv.listen(5)
print("Values being transferred to the internal process as follows:-")
while True:
    conn, addr = serv.accept()
    from_client = ''
    while True:
        data = conn.recv(4096)
        Value={"Small Cup", "Medium Cup", "Large Cup"}
        if not data: break
        from_client += data
        for x in Value:
           conn.send('Size of Cup Available in the Real Workshop is: '+ x)
           time.sleep(3)
    conn.close()
