#! /usr/bin/env python
#coding=utf-8
#sqlite.py

import sqlite3,os

#con = sqlite3.connect(":memory:")
con = sqlite3.connect("a.db")
cx = con.cursor()

cx.execute('drop table catalog')
cx.execute("create table catalog (id integer primary key,pid integer,name varchar(10) UNIQUE,nickname text NULL)")


for t in[(0,10,'abc','Yu'),(1,20,'cba','Xu')]:
    cx.execute("insert into catalog values (?,?,?,?)", t)
con.commit()

# never do this ,insecure
pid=20
cx.execute("update catalog set name='boy111' where pid = '%s'" % pid)

cx.execute('select * from catalog')

print cx.fetchall()
#print os.getcwd()

'''cx.execute("update catalog set name='boy' where id=0")
cx.commit()

cx.execute('select * from catalog')
cx.fetchall()

cx.execute('delete from catalog where id = 0')
cx.commit()
cx.execute('select * from catalog')
cx.fetchall()
'''