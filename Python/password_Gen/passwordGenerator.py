import random

def final(lst1):
    password = ''.join(lst1)
    print(password)

def gen(x):
    alphasCaps = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    alphasLower = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","W","x","y","z"]
    numbers = ["0","1","2","3","4","5","6","7","8","9"]
    specials = ["!","@","#","$","&","?","*","+","-","_"," "]
    finalPassword = []
    for num in range(0, x):
        val = random.choice([alphasCaps,alphasLower,numbers,specials])
        position = random.choice(val)
        finalPassword.append(position)
    return finalPassword   

def main():
    userInput = int(input("enter a integer the length of the password(must be greater then 6): "))
    if userInput < 6:
        print("error pick larger then 6!")
    else:
        gen(userInput)

        lst1 = gen(userInput) 
        final(lst1)
main()