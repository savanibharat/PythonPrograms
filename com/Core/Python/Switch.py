'''
Created on Feb 14, 2014

@author: Savani Bharat
'''
def main():
    choices=dict(
                 one="first",
                 two="second",
                 three="third",
                 four="fourth",
                 )
    v="two"
    print(choices.get(v,"other"))
    

if __name__=="__main__":main()