#beachBoy

def passWord():
    password = (input("enter a 4 digit password: "))
    return password

def hack():
    user = passWord()
    tries = 0
    for x in range(0,10):
        if x < 10:
            hackGuess = str("0" + str(x))
            print(hackGuess)
        elif x < 100 and x > 9:
            hackGuess = str("00" + str(x))
        elif x < 1000 and x > 99:
            hackGuess = str("0" + str(x))
        else:
            hackGuess = str(x)
        #print("0",hackGuess, type(hackGuess))
        #print("1",user, type(user))
        if user == hackGuess:

            return hackGuess, tries
        tries += 1
    return "computer couldn't hack the password"

def main():
    
    answers = hack()
    print("it took the computer " + str(answers[1]) + " to guess your password")
    print("your password was " + str(answers[0]))
main()