'''
Created on Feb 25, 2014

@author: Savani Bharat
'''
def main():
    buffersize=5
    infile=open('lines.txt','r')
    outfile=open('new.txt','w')
    buffer=infile.read(buffersize)
    while len(buffer):
        outfile.write(buffer)
        print'.',
        buffer=infile.read(buffersize)
    print("")
    print("DONE")
    
if __name__ == '__main__':main()  