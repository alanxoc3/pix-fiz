import socket

s = socket.socket()
host = socket.gethostname()
host_ip = socket.gethostbyname(host)

print "host name is ", host
print "host ip address is ", host_ip

port = 2
s.connect((host_ip, port))

print s.recv(1024)
s.close
