class HashNode: #nod som håller ihop nyckel och värde

    def __init__(self, key = "", data = None): #tar emot nyckeln och värdet
        self.key = key #sparar nyckeln
        self.data = data #sparar värdet


class Hashtable:

    def __init__(self, size): # hur stor tabellen ska vara
        self.size = size
        self.table = []

        for i in range(size):
            self.table.append([])

    def store(self, key, data):
        """key är nyckeln
        data är objektet som ska lagras
        Stoppar in "data" med nyckeln "key" i tabellen."""
        index = self.hashfunction(key)

        for nod in self.table[index]:
            if nod.key == key:
                nod.data = data #ersätter nodens gamla data
                return #avslutar eftersom updt är klar

        ny_nod = HashNode(key, data) #skapar ny nod för ny nyckel
        self.table[index].append(ny_nod) #lägger den noden på rätt index

    def search(self, key):
        """key är nyckeln
        Hamtar det objekt som finns lagrat med nyckeln "key" och returnerar det.
        Om "key" inte finns ska det bli KeyError """

        index = self.hashfunction(key)
        for nod in self.table[index]:
            if nod.key == key:
                return nod.data

        raise KeyError

    def __getitem__(self, key): #anropas när tabell[key] skrivs
        return self.search(key)  #anropar search för att hämta värdet

    def __contains__(self, key):
        try:
            self.search(key)
            return True
        except KeyError:
            return False

    def hashfunction(self, key): # tar emot nyckeln
        hashvärde = 0

        for tecken in key: #går igenom namnet, ett tecken/bokstav i taget
            teckenkod = ord(tecken) #hämtar heltalskoden för tecknet/bokstaven
            hashvärde = hashvärde * 17 + teckenkod #bygger vidare värdet

        return hashvärde % self.size #ger ett tal från 0 till (self.size - 1),
        # ger index där nyckeln ska ligga