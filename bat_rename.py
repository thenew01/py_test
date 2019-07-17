import os
import sys


for parent, dirnames, filenames in os.walk(sys.argv[1]):
    for filename in filenames:
        #print(filename)
        path = os.path.splitext(filename)    
        #print(parent)
        print(parent + '\\'+filename)
        #print(path)
        #print(path)    
        if path[1] == ".cc":
            print('process:' + parent+'\\'+path[0]+'.cpp')
            os.rename(parent+'\\'+filename, parent+'\\'+path[0]+'.cpp')

