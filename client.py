import socket

client = socket.socket() #network socket object 
client.connect(('127.0.0.1',5001)) #conencting  to ip & port 
msg = input('Enter message ')
client.send(bytes(msg,'utf-8')) #sending msg to server
print(client.recv(1024).decode()) #decode byte msg sent by server


