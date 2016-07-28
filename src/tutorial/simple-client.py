import socket

s = socket.socket()

print "host name is ", socket.gethostname()

host = socket.gethostname()
port = 12345

s.connect((host, port))
print s.recv(1024)
s.close
