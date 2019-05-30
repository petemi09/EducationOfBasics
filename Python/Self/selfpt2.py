class point:    
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def add(self):
        print(self.x)
        print(self.y)
        print(self.y + self.x)

def main():
    a = point(1,2)
    print(a.add())

    a = point(5,8)
    print(a.add())
main()