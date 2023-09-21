import socket            
s = socket.socket()        
port = 10000
s.connect(('127.0.0.1', port))
while True:
    msg = input()
    if msg.isdigit():
        s.send(msg.encode())
    else:
        break
s.close()