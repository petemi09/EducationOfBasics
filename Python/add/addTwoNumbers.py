#Made by: Mitchell Petellin

def addThem(x,y):
    final = x + y
    val = ""
    if (final % 2) == 0:
        val = "even"
    else:
        val = "odd"
    print("the numbers combined are {}".format(final))
    print("and that number is {}".format(val))

def main():
    int1 = int(input("enter num1: "))
    int2 = int(input("enter num2: "))
    addThem(int1,int2)
main()