# hello.py
# coding:utf-8

print 'hello world'

# print absolute value of an integer:
a = 100
if a >= 0:
	print a
else:
	print -a

	
age = 20
if age >= 6:
    print 'teenager'
elif age >= 18:
    print 'adult'
else:
    print 'kid'
	
u=u'abc'.encode('utf-8')
u=u'中文'.encode('utf-8')
print u

sum = 0
a = range(101)
for x in a:
	sum=sum+x
print sum