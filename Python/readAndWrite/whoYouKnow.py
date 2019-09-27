#Created By: Mitchell Petellin

# CheckList:
#     read in file if there is one if not create one
#     username, basic info
#     root
#     nodes
#     how they connect to each other

import sys
import os

def readFile():
    file = str(input("Enter 'Y' to use exsiting file, \n or use 'N' for new file: "))
    if file == "Y":
        fileName = str(input("Enter the file name: "))
        textFile = open(fileName, 'r')
        # for line in textFile:
        #     print(line)
        #     print("done")
        textFile.close()
    else:
        print("Creating a new file...")
        fileName = str(input("What would you like to name the file: "))
        createFile = open(fileName, 'w')
        print("created " + str(fileName))
        createFile.close()
    return fileName

def contents(fileName):
    print("$$$$$$$$$$$")
    readFile = open(fileName, 'r')
    line = readFile.readlines()
    print(type(line))
    print(line[0])
    print(line[1])
    print("*********")

def addContents(fileName):
    #add content if user wants to
    info = input(str("would you like to add anything to the file (Y/N): "))
    file = open(fileName,'a+')
    if info == "Y":
        #personal
        name = str(input("Enter first name: "))
        last = str(input("Enter last name: "))
        email = str(input("Enter email: "))
        file.write("First Name: " + name + "\n")
        file.write("Last Name: " + last + "\n")
        file.write("Email: " + email + "\n")
    
    else:
        print("------------------------")
        print("--------  Bye!  --------")
        print("------------------------")
    
    
     
    file.close()

def main():
    x = readFile()
    print(x)
    contents(x)
    addContents(x)

if __name__ == "__main__":
    main()