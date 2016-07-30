import socket

def get_ip():
	IP = "172.17.39.61"
	return IP

s = socket.socket()
host_ip = get_ip()
port = 2388

print "host ip address is ", host_ip

s.bind((host_ip, port))

s.listen(5)
while True:
    c, addr = s.accept()
    print 'Got connection from ', addr
    c.send('Thank you for connecting')
    c.close()

