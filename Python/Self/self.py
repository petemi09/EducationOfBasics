# Dogs Created by Mitchell Petellin

class breed:
    def __init__(self,dogName,color,age,breed):
        self.dogName = dogName
        self.color = color
        self.age = age
        self.breed = breed
        self.barking = False

    def info(self):
        print(self.dogName, self.color,self.age,self.breed, self.barking)
    
    def bark(self):
        loud = str(input("Does the dog bark alot (Y/N)?: "))
        if loud == "Y":
            self.barking = True
        breed.info(self)


def main():
    x = breed("mesha","brown","4","german shpeard")
    y = breed("george","white","12","chiwawa")
    x.info()
    y.info()
    x.bark()
if __name__ == "__main__":
    main()