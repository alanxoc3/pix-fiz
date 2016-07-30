import globals as glob
import socket

class Network(object):
	
	def __init__(self):
		print "host ip address is ", glob.HOST_IP
	
	def create(self):
		self.s = socket.socket()
		self.s.bind((glob.HOST_IP, glob.PORT))
		
		
		self.s.listen(5)
		while True:
			self.c, self.addr = self.s.accept()
			print 'Got connection from ', self.addr
			self.c.send('Thank you for connecting')
			self.c.close

	def listen(self):
		pass

	def join(self):
		self.s = socket.socket()
		self.s.connect((glob.HOST_IP, glob.PORT))
		print self.s.recv(1024)

		self.s.close 

	

if __name__ == "__main__":
	p = Network() #init
	try:
		p.join()
	except:
		p.create()
