#! /usr/bin/env python
#coding=utf-8
import socket, select

s = socket.socket()
host = ''#socket.gethostname()
port = 1234
s.bind((host, port))

s.listen(5)
inputs = [s]
outputs=[]
while True:
    rs, ws, es = select.select(inputs, outputs, [])
    for r in rs:
        if r is s:
            c, addr = s.accept()
            print 'Got connection from', addr
            inputs.append(c)
        else:
            try:
                data = r.recv(1024)
                disconnected = not data
            except socket.error:
                disconnected = True

            if disconnected:
                print r.getpeername(), 'disconnected'
                inputs.remove(r)
            else:
                print data
                r.sendall(data)
                outputs.append(r)

    for w in ws:
        print 'write'
        outputs.remove(w)