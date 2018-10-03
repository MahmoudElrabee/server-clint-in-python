import socket

host = "127.0.0.1"
port = 5002

s = socket.socket()
s.bind((host,port))

s.listen(1)
print("listening...")
c, addr = s.accept()
message = ""
print("connection from :",str(addr))
while True:
	data = c.recv(1024)
	if not data:
		break
	print(str(data))
	message = input("->")
	c.send(message.encode())
s.close()

