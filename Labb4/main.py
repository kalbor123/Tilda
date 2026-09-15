from bintreeFile import Bintree

svenska = Bintree() # alla ord från listan lagras här
gamla = Bintree() # Sparar ord som sökningen redan hittat

def makechildren(ordet): #tar emot ordet som ska användas
    alfabet = "abcdefghijklmnopqrstuvwxyzåäö" #bokstäver som provas

    for plats in range(len(ordet)): #går igenom ordets index, 0 1 och 2 för trebokstäver
        for bokstav in alfabet: #provar varje bokstav på respektive plats
            if bokstav != ordet[plats]: #hoppar över orginalbokstaven så att ordet ändras

                nytt_ord= ordet[:plats] + bokstav + ordet[plats+1:] # bygger nya ordet
                if nytt_ord in svenska and nytt_ord not in gamla:
                    print(nytt_ord)
                    gamla.put(nytt_ord)

with open("word3.txt", "r", encoding="utf-8") as svenskfil:#öppnar ordlistan för läsning
    for rad in svenskfil: # läser en rad i taget från filen
        ordet = rad.strip() #tar bort radbrytning
        svenska.put(ordet) #lägger in ordet i sökträdet

startord = input("Startord: ").strip()
slutord = input("Slutord: ").strip()

gamla.put(startord)
makechildren(startord)
