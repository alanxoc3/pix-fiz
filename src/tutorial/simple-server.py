import socket 

s = socket.socket()
host = socket.gethostname()
host_ip = socket.gethostbyname(host)

print "host name is ", host
print "host ip address is ", host_ip

port = 12345
s.bind((host_ip, port))

s.listen(5)
while True:
    c, addr = s.accept()
    print 'Got connection from ', addr
    c.send('Thank you for connecting')
    c.close()

