class A:#(object):
    def __init__(self):
        self.x = 'Hello'
        self.butts = "7"

    def method_a(self, foo):
        print(self.x + ' ' + foo)
        print(self.x)
        print(foo)
    
    def method_b(self, poo):
        #print(self.butts + ' ' + poo)
        print(poo)
        print(self.butts)
        print(int(self.butts))
        answer = int(self.butts) + poo
        print(answer)

def main():
    print("hello")
    print(A)
    print(A())
    a = A()
    print(a.method_a('Sailor'))
    print(a.method_a('Mitch'))
    b = A()
    #print(b.method_b("heeeeelllooooooo"))
    print(b.method_b(5))
main()