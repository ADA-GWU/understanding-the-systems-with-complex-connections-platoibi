import socket

sender = []
for i in range(10001, 10004):
    s = socket.socket()
    s.connect(('127.0.0.1', i))
    sender.append(s)

clientListener = socket.socket()
clientListener.bind(('', 10000))
clientListener.listen(1)
clientListener = clientListener.accept()[0]

cur = 0

while True:
    sender[cur].send(clientListener.recv(64))
    cur = (cur+1)%len(sender)
