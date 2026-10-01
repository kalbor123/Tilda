import csv
from hashtable import Hashtable  # Hämtar klassen från filen hashtable.py.

# från labb1
class Drama:
    # tilldelar atributen till varje skapat objekt
    def __init__(self, Drama_Name, Rating, Actors, Viewship_Rate,
                 Genre, Director , Writer, Year, No_of_Episodes, Network):
        self.Drama_Name = Drama_Name
        self.Rating = float(Rating)
        self.Actors = Actors
        self.Viewship_Rate = Viewship_Rate
        self.Genre = Genre
        self.Director = Director
        self.Writer = Writer
        self.Year = int(Year)
        self.No_of_Episodes = int(No_of_Episodes)
        self.Network = Network


class DictHash:
    def __init__(self):
        self.dictionary = {} # skapar en tom dictionary för lagring

    def store(self, key, data): # tar emot nyckeln och värdet som ska lagras för objektet
        self.dictionary[key] = data #lagrar värdet under nyckeln key

    def search(self, key):
        return self.dictionary[key] #hämtar nyckelns data och returnerar

    def __getitem__(self, key): #kör automatiskt när vi skriver typ d[key]
        return self.dictionary[key]

    def __contains__(self, key): #gör enkelt att söka om en nyckel finns
        return key in self.dictionary


#från labb1
def read_lista(filnamn):
    lista = [] # lista för att lagra objekten

    fil = open(filnamn, 'r') #öppnar filen
    reader = csv.reader(fil) #läser filen

    next(reader)

    for rad in reader: # går ignm csv-filen rad för rad
        if not rad:
            continue

        drama = Drama(rad[0],
                      rad[1],
                      rad[2],
                      rad[3],
                      rad[4],
                      rad[5],
                      rad[6],
                      rad[7],
                      rad[8],
                      rad[9],
        )

        lista.append(drama) #lagrar skapade objekt i listan


    return lista

def main():
    lista = read_lista('kdrama.csv')

    tabell = Hashtable(541)

    for drama in lista:
        tabell.store(drama.Drama_Name, drama) #lagrar dramat med namnet som nyckel

    namn = input("Vilket drama söker du efter: ")  # Väljer första dramats namn att testa med.

    if namn in tabell:  # Använder  __contains__ för att kontrollera om nyckeln finns
        hittat_drama = tabell[namn]  # Använder  __getitem__ för att hämta Drama-objekte
        print(hittat_drama.Drama_Name, "finns i listan")  # Skriver ut det hämtade objektets namn
    else:
        print("Det finns inget drama med det namnet")

main()
