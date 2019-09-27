#Created by: Mitchell Petellin

class Node:
    def __init__(self,data,node_Id,name):
        self.data = data
        self.children = []
        self.name = name
        self.node_Id = node_Id

    def add_child(self,obj):
        self.children.append(obj)

    def findObjectByName(self, name):
        if self.name == name:
            print("Found! --- ",self.data)
            return self
        else:
            for child in self.children:
                match = child.findObjectByName(name)
                if match:
                    return match
                
    def showTree(self):
        print()
        print(self.data)
        for child in self.children:
            nextpass = child.showTree()
            if nextpass:
                return nextpass

def addition():
    name = input("enter name: ")
    email = input("enter email: ")
    phone = input("enter number: ")
    personalID = input("enter id: ")
    contents = [name,email,phone,personalID]
    return contents

def tree():
    contents = addition()
    root = Node([contents],0,contents[0])
    stop = None
    starting_number = 1
    while stop != "stop":
        stop = input(str("enter 'stop' to stop: "))
        if stop == "stop":
            break
        items = addition()
        contact = Node([items],starting_number,items[0])
        root.add_child(contact)
        starting_number += 1
    searching = False
    while searching != True:
        question = str(input("Would you like to search the tree(y/n): "))
        if question != "n":
            search_name = str(input("enter a name to find: "))
            root.findObjectByName(search_name)
        done_searching = str(input("search again?(y/n): "))
        if done_searching == "n":
            searching = True
    print()  
    stop3 = ""
    add_off_of_child_node = str(input("would you like to create a tree off a exsisting child node? (y/n): "))
    if add_off_of_child_node != "n":
        while stop3 != "stop":
            search_name = str(input("enter a name of node to find: "))
            newRoot = root.findObjectByName(search_name)
            
            stop2 = None
            while stop2 != "stop":
                stop = input(str("enter 'stop' to stop: "))
                if stop == "stop":
                    break
                items2 = addition()
                contact2 = Node([items2],starting_number,items2[0])
                newRoot.add_child(contact2)
            root.showTree() 
            stop3 = input(str("Enter 'stop' to stop, or a new tree node will be created: "))
            #would you like to create a nother tree off exsisting node?      
    else:
        print("- - - - - goodbye! - - - - -")
    root.showTree() 

def searchTree(self):
    print()
    check_root = str(input("Do you want to check or update the root node?(y/n): "))
    if check_root != "n":
        print(self.data)
    check_node = str(input("Do you want to check or update a node?(y/n): "))
    if check_node != "n":
        node_num = int(input("what node number do you want to check?: "))
        print(self.children[node_num].data)

def main():
    tree() 
main()