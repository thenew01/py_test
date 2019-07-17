import socket, sys
from os.path import getsize

host=sys.argv[1]
port = int(sys.argv[2])
filename = sys.argv[3]

length = getsize(filename)
print 'file len:', length


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect( (host,port) )
s.sendall(filename)
f = open(filename, "r")


while 1:
#for reads in f:
	reads = f.readline()
	if not len(reads):
		break
	reads.strip()
	s.sendall(reads)

while 1:
	buf = s.recv(2048)	
	
	sys.stdout.write(buf)
	print 'buf len:',len(buf)
	
print 'done.'

s.close()
f.close()
