# Mitchell Petellin
#bindary Tree

class Tree:
    def __init__(self,leaf):
        self.leaf = leaf
        self.left = None
        self.right = None

    def plant(self,leaf):
        if leaf < self.leaf:
            print("moved Left")
            if self.left == None:
                self.left = Tree(leaf)
            else:
                self.left.plant(leaf)
        else:
            print("moved right")
            if self.right == None:
                self.right = Tree(leaf)
            else:
                self.right.plant(leaf)

    def showMeTheTree(self):
        #print(self.info)
        if self.left != None:
            self.left.showMeTheTree()
        print(self.leaf)
        if self.right != None:
            self.right.showMeTheTree()

def main():
    print("The Tree")
    seed = Tree(5)
    branches = [3,51,5,2,17,8,9,3,21,6,14]
    for x in branches:
        seed.plant(x)
    seed.showMeTheTree()

main()
