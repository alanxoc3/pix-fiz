import socket

def get_ip():
	IP = "localhost"
	return IP

s = socket.socket()
host_ip = get_ip()
port = 2388

print "host ip address is ", host_ip

s.connect((host_ip, port))
print s.recv(1024)

s.close
