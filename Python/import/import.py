import helloworld

def imported():
    helloworld.main()

def stringManipulate(x):
    x = helloworld.toAllCaps(x)
    print(x)

def main():
    imported()
    val = helloworld.adder(3,2)
    print(val)
    stringManipulate("mitch")
    

if __name__ == "__main__":
    main()