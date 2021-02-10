'''socket programming
'''
import socket

server = socket.socket() #network socket object 
print('Socket created')

server.bind(('127.0.0.1',5001))  #binding ip & port to create socket

server.listen() #listen incoming connections
print('Waiting for connections...')

while True:
    client_port, address  = server.accept() #accept from incoming connection
    print('Connected with',address, client_port)
    
    client_port.send(bytes('Welcome...','utf-8')) #converting msg to bytes utf-8 format & sending
    client_port.close() 
     
