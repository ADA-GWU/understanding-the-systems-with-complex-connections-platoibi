import socket

def isPortOpen(s : socket.socket, port: int):
    try:
        s.bind(('', port))
        return True
    except:
        return False

s = socket.socket()
port = 10001
while not isPortOpen(s, port):
    port += 1
print('port %s opened'%(port))

s.listen(1)
s = s.accept()[0]

while True:
    msg = s.recv(64).decode()
    if msg.isdigit():
        print(int(msg)*2)

s.close()
        
