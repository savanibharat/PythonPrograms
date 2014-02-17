'''
Created on Feb 16, 2014

@author: Savani Bharat
'''
def main():
    for line in readfile("lines.doc"):
        print(line)
    
def readfile(filename):
    
    if filename.endswith(".txt"):
        fh=open(filename)
        return fh.readlines()
    else:
        raise ValueError("filename must end with .txt")

if __name__=="__main__":main()

'''
ValueError: filename must end with .txt
'''