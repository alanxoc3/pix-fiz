import socket

s = socket.socket()
host = socket.gethostname()
host_ip = "172.17.39.61"

print "host name is ", host
print "host ip address is ", host_ip

port = 12345
s.connect((host_ip, port))

print s.recv(1024)
s.close
