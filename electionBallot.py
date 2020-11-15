
import cmd,sys


#Main Function
def main():
    print("Welcome to your election ballot")
    name = getName()
    print(name)
    idNum = getID()
    print(idNum)

#gets name
def getName():
    name = input("Please enter First and Last Name (ex:Jane Doe)\n")
    checkName(name)
    return name

#allow user to change name if wrong
def checkName(text):
    check = input("Is " + text + " correct(y/n)? " )
    if(check == 'n'):
        getName()
    elif(check == 'y'):
        return
    else:
        checkName(text)

#gets id
def getID():
    idNum = input("Please enter First and Last Name (ex:Jane Doe)\n")
    checkID(idNum)
    return idNum

#allow user to change id if wrong
def checkID(text):
    check = input("Is " + text + " correct(y/n)? " )
    if(check == 'n'):
        getID()
    elif(check == 'y'):
        return
    else:
        checkID(text)

#will add function to check if name and id are already in system

if __name__=="__main__": 
    main() 


