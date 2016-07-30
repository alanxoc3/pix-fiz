import globals as glob
import socket

class Network(object):
	
	def __init__(self):
		#do init networking
		self.c = 0
		print "Host ip address is ", glob.HOST_IP
		self.s = socket.socket()

		#try join and create
		try:
			self.join()
			self.created = False
			print '--------CONNECTED!-------'
		except:
			self.create()
			self.created = True
			print '--------HOSTING!!!-------'

		#other stuff
		self.s.setblocking(0)

	def create(self):
		#reset socket
		self.s.close
		self.s = socket.socket()
	
		#create
		self.s.bind((glob.HOST_IP, glob.PORT))
		self.s.listen(5)

	def join(self):
		self.s.connect((glob.HOST_IP, glob.PORT))	
	
	def listen(self):
		if self.created == True:
			try:
				self.c, addr = self.s.accept()
				print 'Got connection from', addr
				self.c.send('Thank you for connecting')

			except socket.error:
				pass
		else:
			try:
				a = self.s.recv(1024)
				print a
			except:
				pass

	def pass_message(self, message):
		if self.c != 0:
			self.c.send(message)
	

if __name__ == "__main__":
	p = Network() #init

