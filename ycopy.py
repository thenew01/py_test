#! /usr/bin/env python
#coding=utf-8

import sys,os

def main():	
    if len(sys.argv) != 3:
        print('copy src files to dest path')
        print('Usage:ycopy srcFiles destPath')
        print('e.g. ycopy d:\music\*.mp3 d:\mp3')
        os.system("pause")
        return

    cmds = "dir /B /S "
    cmds += str(sys.argv[1])
    cmds += " > dir.txt"
    print(cmds)

    os.system(cmds)


    f = open("dir.txt")
    for line in f:
        cmd = "xcopy /Y  \""
        cmd += line.strip()
        cmd += "\" \"";
        cmd += sys.argv[2]
        cmd += "\"";
        print (cmd)        
        os.system(cmd)
    
    f.close()
    
    print('done.')
    os.system("pause")
		
if __name__ == '__main__':
	main()
