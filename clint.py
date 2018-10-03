import socket
host = "127.0.0.1"
port = 5002
s = socket.socket()
print("try to connect...")
try:
	s.connect((host,port))
except:
	print("there an error")
else:
	message = input("->")
	while message != 'q':
		s.send(message.encode())
		data = s.recv(1024)
		print("~ ",str(data))
		message = input("->")
s.close()

