class Node:
    
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Bintree: 

    def __init__(self):
        self.root = None

    def put(self, newvalue): 
        if self.root is None:
            self.root = Node(newvalue)
        else:
            putta(self.root, newvalue) 
    
    def __contains__(self, value):
         return find(self.root, value)
    
    def write(self):
        write(self.root)
        print()

def putta(node, newvalue):
    if newvalue < node.value: 
        if node.left is None: 
            node.left = Node(newvalue)
        else:
            putta(node.left, newvalue)

    elif newvalue > node.value:
        if node.right is None:
            node.right = Node(newvalue)
        else:
            putta(node.right, newvalue)

def find(node, value): 
    if node is None:
        return False
    if value == node.value:
        return True
    
    if value < node.value:
        return find(node.left, value)
    else:
        return find(node.right, value)

def write(node):
    if node is not None:
        write(node.left)
        print(node.value, end=" ")
        write(node.right)
