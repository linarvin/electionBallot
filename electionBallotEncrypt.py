
import cmd,sys
import pycryptodome


def main():

    plainTextFile = open("voteCount_PlainText.txt","r")
    x = plainTextFile.read() #get copy of votes in voteCount file
    print(x)
    plainTextFile.close()
    

if __name__=="__main__": 
    main() 
