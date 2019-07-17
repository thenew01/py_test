#! /usr/bin/env python
#coding=utf-8
'''def tupleVarArgs(arg1, arg2='defaultB', *theRest):
    'display regular args and non-keyword variable args'
    print 'formal arg 1:', arg1
    print 'formal arg 2:', arg2
    for eachXtrArg in theRest:
        print 'another arg:', eachXtrArg


#tupleVarArgs('abc')
#tupleVarArgs(23, 4.56)

tupleVarArgs('abc', 123, 'xyz', 456.789)

'''

'''
def dictVarArgs(arg1, arg2='defaultB', **theRest):
    'display 2 regular args and keyword variable args'
    
    print 'formal arg1:', arg1
    print 'formal arg2:', arg2
    for eachXtrArg in theRest.keys():
        print 'Xtra arg %s: %s' % \
        (eachXtrArg, str(theRest[eachXtrArg]))

#dictVarArgs(arg2='tales', c=123, d='poe', arg1='mystery')
dictVarArgs('one', d=10, e='zoo', men=('freud', 'gaudi'))'''

'''
def newfoo(arg1, arg2, *nkw, **kw):
    'display regular args and all variable args'
    print 'arg1 is:', arg1
    print 'arg2 is:', arg2 
    for eachNKW in nkw:
        print 'additional non-keyword arg:', eachNKW
    for eachKW in kw.keys():
        print "additional keyword arg '%s': %s" % \
        (eachKW, kw[eachKW])

#newfoo('wolf', 3, 'projects', freud=90, gamble=96)
#newfoo(10, 20, 30, 40, foo=50, bar=60)
newfoo(2, 4, *[6, 8], **{'foo': 10, 'bar': 12})
'''

'''
from random import randint
def odd(n):
    return n % 2
allNums = []
for eachNum in range(9):
    allNums.append(randint(1, 99))
    
print filter(odd, allNums)
'''

'''
from random import randint 
allNums = []
for eachNum in range(9):
    allNums.append(randint(1, 99))
print filter(lambda n: n%2, allNums)
'''

'''
from random import randint

allNums = []
for eachNum in range(9):
    allNums.append(randint(1, 99))
print [n for n in allNums if n%2]
'''


from random import randint as ri
print([n for n in [ri(1,99) for i in range(9)] if n%2 == 1 ])

'''
def counter(start_at=0): 
    count = [start_at]
    def incr():
        count[0] += 1
        return count[0]
    
    return incr

count = counter(5)

print count()
print count()

'''
x= 10
def foo():
    y = 5
    bar = lambda : x+y

    print(bar())
    y = 8
    print(bar())
    print(bar())

foo()