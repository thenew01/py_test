import socket,sys,threading, time
from SocketServer import TCPServer, ForkingMixIn, StreamRequestHandler
from time import sleep,ctime

def now():
	return str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime() ) )
	
class myThread( threading.Thread ):
	"""doc string for myThread"""
	def __init__(self,clientsock,clientaddr):
		super(myThread, self).__init__()
		self.clientsock = clientsock
		self.clientaddr = clientaddr
		
		self.run()
		
	def run(self):		
		work(self.clientsock, self.clientaddr)
			
def work(clientsock,clientaddr):
	#clientsock.sendall("welcome,"+str(clientaddr)+"\n")
	
	while 1:
		try:
			line = clientsock.recv(2048)
			clientsock.sendall(line)

		except (KeyboardInterrupt , SystemExit): 
			print('terminate the procedure?') 
			flag = sys.stdin.readline().rstrip() 
			if((flag == 'yes') or (flag == 'y')): 
				sys.exit(1) 
			else: 
				continue 
		except: 
			sys.exit(1) 

	clientsock.close()
	
	print 'server done.'
	
def listen():
	print 'starting at:', now()
	thpool= []
	
	host=''
	port = 1234
	if len(sys.argv)>1:		
		port=int( sys.argv[1] )
		
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
	s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
	s.bind( ( host,port) )
	s.listen(5)

	print "server is running on port %d." %port

	while 1:
		try:			
			clientsock,clientaddr=s.accept()
			th = threading.Thread(target=work, args=(clientsock, clientaddr))
			th.setDaemon = True
			th.start()		
			thpool.append(th)
			#thpool.append(myThread(clientsock, clientaddr))
			
		except (KeyboardInterrupt , SystemExit): 
			print('terminate?') 
			flag = sys.stdin.readline().rstrip() 
			if((flag == 'yes') or (flag == 'y')): 
				sys.exit(1) 
			else: 
				continue 
		except: 
			sys.exit(1) 
		
	'''for th in thpool:
		th.join()'''
		
	print 'listen thread exited at:', now()

def main():	
	th = threading.Thread( target = listen )
	th.setDaemon = True
	th.start()
	
	sleep(2)
	
	print 'enter \'q\' to exit'
	while 1:
		c = raw_input()	
		if c == 'q':
			break
		
	#th.join()
	
	print 'done.'
		
if __name__ == '__main__':
	main()
		
