def reverse(x):
    lst = []
    item = len(x)
    for y in range(0,len(x)):
        item -=1
        position = x[item]
        lst.append(position)
    return lst

def buildReverse(parts):
    for x in range(len(parts)):
        final = "".join(parts)
    print(final)

def main():   
    string1 = str(input("enter a string: "))
    x = reverse(string1)
    buildReverse(x)
main()