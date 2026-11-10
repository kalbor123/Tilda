import unittest #hämtar Pythons verktyg för automatiska tester
from formelkoll import skapa_kö, read_formel, Syntaxfel #hämtar funktionerna och vår undantagsklass

class TestFormelkoll(unittest.TestCase): #samlar tester och ärver testverktygets funktioner
    def test_korrekta_formler(self): #testar alla korrekta formler från Kattis första exempel
        formler = ["Na", "H2O", "Si(C3(COOH)2)4(H2O)7", "Na332"] #samlar formlerna i en lista

        for formel in formler: #väljer en formel i taget från listan
            with self.subTest(formel=formel): #markerar vilken formel som testas
                q = skapa_kö(formel) #skapar en ny kö för den aktuella formeln
                read_formel(q) #kontrollerar formeln och ska inte utlösa något undantag
                self.assertTrue(q.isEmpty()) #kontrollerar att hela formeln har lästs

    def test_felaktiga_formler(self): #testar alla felaktiga formler från Kattis andra exempel
        testfall = [ #varje rad innehåller formeln, förväntat fel och förväntad rest
            ("C(Xx4)5", "Okänd atom vid radslutet", "4)5"),
            ("C(OH4)C", "Saknad siffra vid radslutet", "C"),
            ("C(OH4C", "Saknad högerparentes vid radslutet", ""),
            ("H2O)Fe", "Felaktig gruppstart vid radslutet", ")Fe"),
            ("H0", "För litet tal vid radslutet", ""),
            ("H1C", "För litet tal vid radslutet", "C"),
            ("H02C", "För litet tal vid radslutet", "2C"),
            ("Nacl", "Saknad stor bokstav vid radslutet", "cl"),
            ("a", "Saknad stor bokstav vid radslutet", "a"),
            ("(Cl)2)3", "Felaktig gruppstart vid radslutet", ")3"),
            (")", "Felaktig gruppstart vid radslutet", ")"),
            ("2", "Felaktig gruppstart vid radslutet", "2"),
        ]

        for formel, felmeddelande, förväntad_rest in testfall: #packar upp de tre värdena från ett testfall i taget
            with self.subTest(formel=formel): #visar vilken formel som testas om något misslyckas
                q = skapa_kö(formel) #skapar en ny kö med den aktuella formeln

                with self.assertRaises(Syntaxfel) as resultat: #kräver att kontrollen utlöser Syntaxfel
                    read_formel(q) #kontrollerar den felaktiga formeln

                self.assertEqual(str(resultat.exception), felmeddelande) #jämför det faktiska felmeddelandet med det förväntade

                rest = "" #skapar en tom sträng för de olästa tecknen
                while not q.isEmpty(): #fortsätter så länge kön innehåller tecken
                    rest += q.dequeue() #tar ut nästa tecken och lägger till det i resten

                self.assertEqual(rest, förväntad_rest) #kontrollerar att rätt tecken återstod vid felet



    def test_egna_korrekta(self): #testar egna exempel på tillåtna formler
        formler = ["H", "H10", "((OH)2)3"] #provar ensam atom, flersiffrigt antal och nästlade parenteser

        for formel in formler: #går igenom en formel i taget
            with self.subTest(formel=formel): #markerar vilken formel som testas
                q = skapa_kö(formel) #skapar en ny kö med formeln
                read_formel(q) #kontrollerar att formeln passerar utan undantag
                self.assertTrue(q.isEmpty()) #kontrollerar att hela formeln har lästs

    def test_egna_felaktiga(self): #testar egna exempel på otillåtna formler
        testfall = [ #samlar formel, förväntat felmeddelande och förväntad rest
            ("()2", "Felaktig gruppstart vid radslutet", ")2"),
            ("(H)1", "För litet tal vid radslutet", ""),
            ("(H)02", "För litet tal vid radslutet", "2"),
            ("Mg(OH)", "Saknad siffra vid radslutet", ""),
        ]

        for formel, felmeddelande, förväntad_rest in testfall: #hämtar ett testfalls tre värden
            with self.subTest(formel=formel): #markerar vilken formel som testas
                q = skapa_kö(formel) #skapar en ny kö med formeln

                with self.assertRaises(Syntaxfel) as resultat: #kräver att ett syntaxfel upptäcks
                    read_formel(q) #startar kontrollen

                self.assertEqual(str(resultat.exception), felmeddelande) #kontrollerar felmeddelandet

                rest = "" #samlar tecknen som återstår efter felet
                while not q.isEmpty(): #fortsätter tills kön är tom
                    rest += q.dequeue() #lägger nästa tecken sist i strängen

                self.assertEqual(rest, förväntad_rest) #kontrollerar den olästa resten
if __name__ == "__main__": #kör blocket när testfilen startas direkt
    unittest.main() #hittar och kör filens tester