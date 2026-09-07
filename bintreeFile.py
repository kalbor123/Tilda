class Node: #klass som beskriver nod i trädet

    def __init__(self, value): #Anropas när ny nod skapas
        self.value = value # sparar värdet i noden
        self.left = None # pekare åt vänster
        self.right = None # pekare åt höger

class Bintree: # representerar binärt sökträd

    def __init__(self): #ger nytt träd startvärde
        self.root = None # hänvisar till roten

    def put(self, newvalue): # Sorterar in newvalue i trädet
        self.root = putta(self.root, newvalue) # sparar roten som returneras av putta

    def __contains__(self, value): #används för att söka i trädet
        return finns(self.root, value) # returnerar true om värdet finns

    def write(self): #skriver ut trädet värden inorder
        skriv(self.root) #anropar skriv
        print("\n")


def putta(node, newvalue):
    if node is None:
        return Node(newvalue) #skapar ny nod med newvalue

    if newvalue < node.value: #mindre värde till vänster
        node.left = putta(node.left, newvalue) #läger in och sparar referens som returneras

    elif newvalue > node.value: # större värden till höger
        node.right = putta(node.right, newvalue) #lägger in där och sparar referensen som returnears

    return node #returenrar roten till funktionen


def finns(node, value): #söker ett värde, börjar vid node
    if node is None:
        return False
    if value == node.value:
        return True

    if value < node.value:
        return finns(node.left, value)
    else:
        return finns(node.right, value)


def skriv(node): #skriver ut värden i delträdet som börjar vid node
    if node is not None:
        skriv(node.left)
        print(node.value, end=" ")
        skriv(node.right) # de indragna raderna gör inorder-regeln.

