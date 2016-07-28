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
s.connect((host_ip, port))

print s.recv(1024)
s.close
