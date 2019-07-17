#! /usr/bin/env python
#coding=utf-8


from SocketServer import TCPServer, StreamRequestHandler
#第一步。其中StreamRequestHandler类是BaseRequestHandler类的子类，它为流socket定义了
#rfile和wfile方法
class Handler(StreamRequestHandler):
    def handle(self):
        addr = self.request.getpeername()
        print 'Got connection from', addr
        #line = self.request.recv(2048).strip()
        line = self.rfile.readline().strip()
        if line != '':
            print line
        self.wfile.write('Thank you for connecting')

#第二步。其中''代表运行服务器的主机
server = TCPServer(('', 1234), Handler)
#第三步。serve_forever()导致进入循环状态
server.serve_forever() 
