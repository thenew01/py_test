#! /usr/bin/env python
#coding=utf-8
#!/usr/bin/env python

'''
关于柯里化（currying），我们可以这么理解：
柯里化就是一个函数在参数没给全时返回另一个函数，
返回的函数的参数正好是余下的参数。
比如：你制定了x和y, 如2的3次方,就返回8, 
如果你只制定x为2,y没指定, 那么就返回一个函数：
2的y次方, 这个函数只有一个参数:y。
这样就非常容易理解吧。
'''
output = '<int %r id=%#0x val=%d>'
w = x = y = z = 1
def f1():
    x = y = z = 2

    def f2():
        y = z = 3

        def f3():
            z = 4
            print output % ('w', id(w), w)
            print output % ('x', id(x), x)
            print output % ('y', id(y), y)
            print output % ('z', id(z), z)


        clo = f3.func_closure
        if clo:
            print "f3 closure vars:", [str(c) for c in clo]
        else:
            print "no f3 closure vars"
        f3()

    clo = f2.func_closure
    if clo:
        print "f2 closure vars:", [str(c) for c in clo]
    else:
        print "no f2 closure vars"
    f2()

clo = f1.func_closure
if clo:
    print "f1 closure vars:", [str(c) for c in clo]
else:
    print "no f1 closure vars"

f1()


'''f2 closure vars: ['<cell at 0x5ee30: int object at
0x200377c>']
f3 closure vars: ['<cell at 0x5ee90: int object at 0x2003770>', 
'<cell at 0x5ee30: int object at 0x200377c>']
<int 'w' id=0x2003788 val=1>
<int 'x' id=0x200377c val=2>
<int 'y' id=0x2003770 val=3>
<int 'z' id=0x2003764 val=4>
'''