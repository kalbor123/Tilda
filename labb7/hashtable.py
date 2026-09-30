class HashNode: #nod som håller ihop nyckel och värde

   def __init__(self, key = "", data = None): #tar emot nyckeln och värdet
      self.key = key #sparar nyckeln
      self.data = data #sparar värdet


class Hashtable:

   def __init__(self, size):
       self.size = size
       self.table = []

       for i in range(size):
           self.table.append([])

   def store(self, key, data):
      """key är nyckeln
         data är objektet som ska lagras
         Stoppar in "data" med nyckeln "key" i tabellen."""
      #Fyll i kod här!

   def search(self, key):
      """key är nyckeln
         Hamtar det objekt som finns lagrat med nyckeln "key" och returnerar det.
         Om "key" inte finns ska det bli KeyError """
      #Fyll i kod här!
      #...
      else:
         raise KeyError

   def hashfunction(self, key):
       hashvärde = 0

