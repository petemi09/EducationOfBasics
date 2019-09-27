#Made by: Mitchell Petellin

import random

def gen():
    alphas = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    nums = ["0","1","2","3","4","5","6","7","8","9"]
    keys = [alphas,nums]
    password = []
    password1 = ""
    for x in range(8):
        val = random.choice(random.choices(keys, weights=map(len, keys))[0])
        password.append(val)
        if x < 7:
            password.append('-')
        else:
            pass
    for i in range(len(password)):
        password1 = ''.join(password)
    return password1

def main():
    password = gen()
    print(password)

main()
