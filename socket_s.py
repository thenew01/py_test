#! /usr/bin/env python
#coding=utf-8
import SocketServer

host=''
port=1234

#class Server(ForkingMixIn,TCPServer):pass
#class Server(ThreadingMixIn,TCPServer):pass

class Handler(SocketServer.StreamRequestHandler):

 def handler(self):
  addr=self.request.getpeername()
  print( "got connection from",addr )
  self.wfile.write("connected")

server=SocketServer.TCPServer((host,port),Handler)
print('started')
server.serve_forever()
