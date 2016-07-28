import socket
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 0))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

s = socket.socket()
host = socket.gethostname()
host_ip = get_ip()

print "host name is ", host
print "host ip address is ", host_ip

port = 3033
#s.bind((host_ip, port))

s.listen(5)
while True:
    c, addr = s.accept()
    print 'Got connection from ', addr
    c.send('Thank you for connecting')
    c.close()

