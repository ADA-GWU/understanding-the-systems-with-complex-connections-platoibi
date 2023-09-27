import socket            

sender = []
for i in range(10001, 10004):
    s = socket.socket()
    s.connect(('127.0.0.1', i))
    sender.append(s)

cur = 0

while True:
    msg = input()
    if msg.isdigit():
        sender[cur].send(msg.encode())
        print('Packet sent to port ' + str(10001+cur))
        cur = (cur+1)%len(sender)
    elif msg == "exit":
        break

for s in sender:
    s.close()