#Created by: Mitchell Petellin

class information:
    def __init__(self,fName,lName,address):#,idNum,phone,email,blurb):
        self.fName = None
        self.lName = None
        self.address = None
        # self.idNum = idNum
        # self.phone = phone
        # self.email = email
        # self.blurb = blurb

    def getCredentials(self):
        if self.fName == None:
            self.fName = str(input("Enter your first name: "))
        if self.lName == None:
            self.lName = str(input("Enter your last name: "))
        valResponse1 = str(input("Would you like to use your address? (y/n)"))
        if valResponse1 == "y":
            self.address = str(input("Enter your address: "))

    def printCredentials(self):
        print(self.fName,self.lName,self.address)


    
def main():
    x = information(None,None,None)
    x.getCredentials()
    x.printCredentials()
if __name__ == "__main__":
    main()