#Created By: Mitchell Petellin
import sys


def openThis():
    x = open("bitches.txt", 'r')
    for i in x:
        print(i)    

# def writeTo():
#     wouldWrite = input("would you like to write to the file? (y/n): ")
#     if wouldWrite == "y":
#         print("COOL")
#         file = open("bitches.txt", 'w')
#         file.readline()
#         print(file)
#     else:
#         pass

def main():
    openThis()
    #writeTo()
    


if __name__ == "__main__":
    main()
