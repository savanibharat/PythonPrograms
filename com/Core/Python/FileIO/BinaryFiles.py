'''
Created on Feb 25, 2014

@author: Savani Bharat
'''
def main():
    buffersize = 5
    
    infile = open("GOT.jpg", "rb")
    outfile = open("newGOT.jpg", "wb")
    
    buffer = infile.read(buffersize)
   
    while len(buffer):
        outfile.write(buffer)
        buffer = infile.read(buffersize)
    
    print("DONE")
        
if __name__ == '__main__':main()
    
