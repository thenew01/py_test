#! /usr/bin/env python
#coding=utf-8

import os,sys
from os.path import join, getsize  
  
def getdirsize(dir):  
   size = 0L  
   for root, dirs, files in os.walk(dir):  
      size += sum([getsize(join(root, name)) for name in files])  
    #[expr for iter_var in iterable]
    #这个语句的核心是 for 循环, 它迭代 iterable 对象的所有条目. 前边的 expr 应用于序列
    #的每个成员, 最后的结果值是该表达式产生的列表. 迭代变量并不需要是表达式的一部分.
    
   return size  


if __name__ == '__main__':  
   path = str(sys.argv[1])
   filesize = getdirsize(path)  
   print 'There are %.3f' % (filesize/1024/1024), 'Mbytes in \"%s\"' % path  

    
    '''---------------
    os.mkdir(os.path.join('work', newfileName))
    self.cureentMtf = os.path.join('work', newfileName, newfileName+'-%d'%len(os.listdir(newfileName))+'.mtf')
    f = open(self.cureentMtf, 'w') 
    f.write('='+newfileName+'\n') 
    f.close() '''
    
