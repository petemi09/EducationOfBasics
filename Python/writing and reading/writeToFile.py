#Created by Mitchell Petellin

def main():
    #file = open("text.txt","w+")
    # for i in range(10):
    #     file.write("This is line %d\r\n" % (i+1))
    # file = open("text.txt","a+")
    # for i in range(2):
    #      file.write("Appended line %d\r\n" % (i+1))        
    # file.close()
    file = open("text.txt", "r")
    # if file.mode == "r":
    #     contents =  file.read()
    #     print(contents)
    f1 = file.readlines()
    for x in f1:
        print(x)
if __name__ == "__main__":
    main()