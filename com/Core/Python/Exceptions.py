'''
Created on Feb 13, 2014

@author: Savani Bharat
'''
try:
    fh=open("myfile.txt")
    for line in fh.readlines():
        print(line)

except IOError as e:
    print(format(e))

print("after exception")
    
'''
[Errno 2] No such file or directory: 'myfile.txt'
after exception

'''