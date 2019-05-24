# Created by: Mitchell Petellin

def user():
    userInput = input("please enter something: ")
    return userInput

def convert(x):
    newList = []
    for item in range(len(x)):
        newList = list(x.split(" "))
    return newList

def add(x):
    total = 0
    for i in range(len(x)):
        total += int(x[i])
    return total

def main():
    x = user()
    y = convert(x)
    final = add(y)
    print("your total is: " + str(final))
main()