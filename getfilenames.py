#! /usr/bin/env python
#coding=utf-8
#os.listdir(),os.path.join().主要代码贴在下面。
from os import path.join,listdir

def getfilenames(findpath,filetype,join):#有的时候不需要路径，所以加了个参数
    filelist=[]
    filenames=os.listdir(findpath)
    
    for thefile in filenames:
        if (filetype in thefile):
            if join=="join":#listdir会得到当前路径下的文件名和文件夹名，结果不包括长长的路径
                fullfilename=os.path.join(findpath,thefile)#将路径和查找的文件合并成绝对路径
            else:
                fullfilename=thefile
            
            filelist.append(fullfilename)
        
    filelist.sort()
    return filelist
