from bintreeFile import Bintree
from LinkedQFile import LinkedQ

class ParentNode:
    def __init__(self, word, parent=None):
        self.word = word 
        self.parent = parent
        

svenska = Bintree() # alla ord från listan lagras här
gamla = Bintree() # Sparar ord som sökningen redan hittat
q = LinkedQ() #skapar tom kö


def writechain(node):
    if node.parent is not None:
        writechain(node.parent)
    print(node.word)

def makechildren(parent, q, slutord): #tar emot ordet som ska användas
    ordet = parent.word
    alfabet = "abcdefghijklmnopqrstuvwxyzåäö" #bokstäver som provas

    for plats in range(len(ordet)): #går igenom ordets index, 0 1 och 2 för trebokstäver
        for bokstav in alfabet: #provar varje bokstav på respektive plats
            if bokstav != ordet[plats]: #hoppar över orginalbokstaven så att ordet ändras

                nytt_ord= ordet[:plats] + bokstav + ordet[plats+1:] # bygger nya ordet
                if nytt_ord in svenska and nytt_ord not in gamla:
                    barn = ParentNode(nytt_ord, parent)
                    q.enqueue(barn) #lägger "barnet" sist i kön
                    gamla.put(nytt_ord) #lägger upptäckt barn i gamla

                    if nytt_ord == slutord: #om nya barnet är samma som slutord
                        writechain(barn)
                        return True
    return False #om slutordet inte kan hittas

with open("word3.txt", "r", encoding="utf-8") as svenskfil:#öppnar ordlistan för läsning
    for rad in svenskfil: # läser en rad i taget från filen
        ordet = rad.strip() #tar bort radbrytning
        svenska.put(ordet) #lägger in ordet i sökträdet

startord = input("Startord: ").strip()
slutord = input("Slutord: ").strip()

gamla.put(startord)

startnode = ParentNode(startord)
q.enqueue(startnode) #lägger startord först i kön

hittad = startord == slutord # True om start och slutord är samma

while not q.isEmpty() and not hittad:
    word = q.dequeue()
    hittad = makechildren(word, q, slutord) #skckar med slutord och sparar svar
if hittad:
    print("Det finns en väg till", slutord)
else:
    print("Det finns ingen väg till", slutord)