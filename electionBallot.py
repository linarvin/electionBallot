

import cmd,sys


#Main Function
canidates = {'1':"Rick Sanchez",'2':"Charlie Brown"}

def main():
    #canidates = {'1':"Rick Sanchez",'2':"Charlie Brown"}
##    print("Welcome to your election ballot")
##    name = getName()
##    print(name)
##    idNum = getID()
##    print(idNum)
    vote = getVote()
    print(vote)

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
    idNum = input("Please enter you ID number\n")
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
##def checkRegistration:
##    return

def getVote():
    while True:
        print("The canidates are as follow: ")
        print("1. Rick Sanchez")
        print("2. Charlie Brown")
        vote = input("Enter the number coresponding to the canidate you choose.")
        vote2 = str(vote)
        #print(vote2)
        #print(type(vote2))
        if((vote2 == '1') or (vote2 == '2')):
            myVote = checkVote(vote2)
            print(myVote)
            return myVote
        print("Invalid Number")
        

def checkVote(num):
    name = canidates[num]
    check = input("Is " + name + " correct(y/n)? " )
    if(check == 'n'):
        getVote()
    elif(check == 'y'):
        confirm = num
        print(confirm)
        return confirm
    else:
        checkVote(text)

#store vote into file?
#or write into new file
def storeVote(name,ID,vote):
    return
        

if __name__=="__main__": 
    main() 


