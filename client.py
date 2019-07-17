#! /usr/bin/env python
#coding=utf-8
#!/usr/bin/env python
import socket,sys
#,OSError

host="localhost"
port=1234
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
 
s.send( b'hello from client\n' )#.encode('UTF-8')


#try:
buf = s.recv(2048)
print('recv from server:')
print(buf)
'''except (KeyboardInterrupt , SystemExit): 
    print('terminate the procedure?') 
    flag = sys.stdin.readline().rstrip() 
    if((flag == 'yes') or (flag == 'y')): 
        sys.exit(1) 
    else: 
         pass
except: 
    sys.exit(1) 
'''
s.close()
