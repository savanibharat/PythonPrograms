'''
Created on Feb 25, 2014

@author: Savani Bharat
'''
#ord gives us the number for chracter that is ascii  
def main():
    fin=open('utf8.txt','r',encoding='utf_8')
    fout=open('utf8.html','w')
    outbytes=bytearray()
    for line in fin:
        for c in line:
            if ord(c)>127:
                outbytes+=bytes('&#{:04d};'.format(ord(c)),encoding='utf_8')
               
            else:
                outbytes.append(ord(c))
                
    outstr=str(outbytes,encoding='utf-8')
    file=fout
    print outstr,file
    print("done")
    print ""

if __name__=="__main__":main()