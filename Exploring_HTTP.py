from __future__ import print_function	
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('pythonlearn.com', 80))
cmd = 'GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end ='')

mysock.close()
	