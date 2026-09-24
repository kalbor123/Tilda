from bintreeFile import Bintree
from linkedQFile import LinkedQ

class ParentNode: #beskriver hur en ny sorts objekt ska se ut
    def __init__(self, word, parent=None): #anropas automatisk när nytt objekt skapas

        self.word = word #sparar ordet i objektet
        self.parent = parent #sparar var word kommer ifrån

svenska = Bintree() # alla ord från listan lagras här
gamla = Bintree() # Sparar ord som sökningen redan hittat
q = LinkedQ() #skapar tom kö

def writechain(nod): #tar emot noden vars väg vi vill skriva ut
    if nod.parent is not None: #kontrollerar att noden har en förälder
        writechain(nod.parent) #skriver först ut vägen fram till föräldern
    print(nod.word) #skriver ut aktuell nods ord

def makechildren(nod, q, slutord): #tar emot ordet som ska användas
    ordet = nod.word 
    alfabet = "abcdefghijklmnopqrstuvwxyzåäö" #bokstäver som provas

    for plats in range(len(ordet)): #går igenom ordets index, 0 1 och 2 för trebokstäver
        for bokstav in alfabet: #provar varje bokstav på respektive plats
            if bokstav != ordet[plats]: #hoppar över orginalbokstaven så att ordet ändras

                nytt_ord= ordet[:plats] + bokstav + ordet[plats+1:] # bygger nya ordet
                if nytt_ord in svenska and nytt_ord not in gamla:
                    barn = ParentNode(nytt_ord, nod) #skapar en nod med det nya ordet med nuvarande som förälder
                    q.enqueue(barn) # lägger "barnet"/objektet sist i kön
                    gamla.put(nytt_ord) #lägger upptäckt barn i gamla

                    if nytt_ord == slutord: #om nya barnet är samma som slutord
                        writechain(barn) #skriver ut barnet genom att följa föräldern
                        return True
    return False #om slutordet inte finns bland en viss nods barns

with open("../labb 5/word3.txt", "r", encoding="utf-8") as svenskfil:#öppnar ordlistan för läsning
    for rad in svenskfil: # läser en rad i taget från filen
        ordet = rad.strip() #tar bort radbrytning
        svenska.put(ordet) #lägger in ordet i sökträdet

startord = input("Startord: ").strip()
slutord = input("Slutord: ").strip()  #skapar nod med startordet, parentnode = none

gamla.put(startord)
startnod = ParentNode(startord)
q.enqueue(startnod) #lägger startord först i kön


hittad = startord == slutord # True om start och slutord är samma

while not q.isEmpty() and not hittad:
    word = q.dequeue()
    hittad = makechildren(word, q, slutord) #skckar med slutord och sparar svar
if not hittad:
    print("Det finns ingen väg till", slutord)
elif startord == slutord:
    writechain(startnod)
