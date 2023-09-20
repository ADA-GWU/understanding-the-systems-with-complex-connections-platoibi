import socket            
s = socket.socket()        
print ("Socket successfully created")
port = 10000
s.bind(('', port))        
print ("socket binded to %s" %(port))

#lsof -i tcp:10000 to check if it is working
s.listen(2)
print ("socket is listening")
while True:
    c, addr = s.accept()    
    print(c, addr)
    print ('Got connection from', addr )
    c.send('Thank you for connecting'.encode())
    c.close()
    break
