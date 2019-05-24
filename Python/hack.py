#beachBoy

def passWord():
    password = (input("enter a 4 digit password: "))
    
    print(password)
    #print("%04d" %int(password))
    #print("password",password)
    #return password

def hack():
    user =str(1)
    tries = 0
    for x in range(0,10000):
        if x < 10:
            hackGuess = str("000" + str(x))
        elif x < 100 and x > 9:
            hackGuess = str("00" + str(x))
        elif x < 1000 and x > 99:
            hackGuess = str("0" + str(x))
        else:
            hackGuess = str(x)
        if user == hackGuess:
            return "whooooooooo", tries
        tries += 1
    return "computer couldn't hack the password"

def check(attempt):
    list1 = (list(str(attempt)))
    char = False
    place = 0
    for item in list1:
        print("this is the check", list1[place])
        if list1[place] == "0":
            print("was zero")
        else:
            print("wasn't zero")
        place += 1

def main():
    x = passWord()
    #print(hack())
    check(x)

main()
