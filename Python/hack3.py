# Mitchell Petellin
import random

def guess(number, maxNumberFromMain):
    try1 = 0
    maxNumber = maxNumberFromMain
    minNumber = 0
    for x in range(0,100):
        computersGuess = random.randint(minNumber,maxNumber)
        if number < computersGuess:
            maxNumber = computersGuess - 1
        else:
            minNumber = computersGuess + 1
        if computersGuess == number:
            return try1
        else:
            try1 += 1
            print("the computer guessed " +str(computersGuess) + " it also updated its range,")
            print("its new range is min("+str(minNumber)+") , max("+str(maxNumber)+")")

def main():
    print("fuck you")
    user = int(input("enter a four digit password: "))
    setMax = int(input("set the max number you want the computer to start at: "))
    x = guess(user,setMax)
    print("it took the computer " + str(x) + " tries to guess your password")

main()