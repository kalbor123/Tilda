import unittest #hämtar Pythons testverktyg
from molekyler import skapa_kö, read_group, Syntaxfel #hämtar funktionerna och undantagsklassen


class TestMolekyler(unittest.TestCase): #samlar våra tester

    def test_korrekt(self): #testar att en korrekt formel godkänns
        q = skapa_kö("Aa5") #skapar kön med formelns tecken
        read_group(q) #ska köras klart utan undantag

    def test_saknad_stor_bokstav(self): #testar att en liten bokstav först upptäcks
        q = skapa_kö("cr12") #skapar kön med en felaktig formel

        with self.assertRaises(Syntaxfel): #testet kräver att Syntaxfel utlöses
            read_group(q) #kontrollerar formeln som ska ge Syntaxfel


if __name__ == "__main__": #kör blocket när filen startas direkt
    unittest.main() #hittar och kör testerna