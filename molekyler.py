from LinkedQFile import LinkedQ

STORA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
SMÅ = "abcdefghijklmnopqrstuvwxyz"
SIFFROR = "0123456789"

class Syntaxfel(Exception): #undatgasklass som ärver från exception, används för fel
    pass #inget extra beteende behövs utöver det som ärvs från Exception

def skapa_kö(text):
    q = LinkedQ()
    for tecken in text:
        q.enqueue(tecken)
    return q

def read_group(q):
    read_atom(q)  # Läser atomnamnet som alltid måste finnas

    if not q.isEmpty():  #kontrollerar om det finns något tecken kvar
        if q.peek() in SIFFROR:  #undersöker om nästa tecken är en siffra
            read_num(q)  #läser och kontrollerar antalet om det finns

def read_atom(q):#läser atomnamn
    read_LETTER(q) #läser stor bokstav

    if not q.isEmpty(): #tittar på nästa tecken om det finns ngt kvar
        if q.peek() in SMÅ: # kontrollerar att det är en liten bokstav
            read_letter(q) # läser den lilla bokstaven om den finns

def read_LETTER(q):
    if q.isEmpty(): #kontrollerar om kön är tom
        raise Syntaxfel("Saknad stor bokstav vid radslutet")

    if q.peek() not in STORA: #kontrollerar stor bokstav
        raise Syntaxfel("Saknad stor bokstav vid radslutet")

    q.dequeue()

def read_letter(q):
    if q.isEmpty(): #kontrollerar om kön är tom
        raise Syntaxfel("Saknad liten bokstav vid radslutet")

    if q.peek() not in SMÅ: #kontrollerar om
        raise Syntaxfel("Saknad liten bokstav vid radslutet")

    q.dequeue()

def read_num(q):
    tal = q.dequeue()

    if tal == "0":  #ett antal får inte börja med noll
        raise Syntaxfel("För litet tal vid radslutet")  #avbryter och lämnar resten kvar

    while not q.isEmpty():  #fortsätter så länge det finns tecken kvar
        if q.peek() not in SIFFROR:  #om nästa tecken inte är en siffra är talet färdigläst
            break  #avslutar while-loopen

        tal += q.dequeue()  #tar ut nästa siffra och lägger till den i strängen

    if int(tal) < 2:  #omvandlar hela siffersträngen till ett heltal och jämför med 2
        raise Syntaxfel("För litet tal vid radslutet")  #antalet är för litet

if __name__ == "__main__": #kör blocket när filen startas direkt
    text = input() #läser den första raden

    while text != "#": #fortsätter tills användaren eller Kattis skickar # (stopptecken)
        q = skapa_kö(text) #skapar en ny kö med den aktuella formelns tecken

        try: #försöker genomföra kontrollen
            read_group(q) #kontrollerar atomnamnet och ett eventuellt antal
            print("Formeln är syntaktiskt korrekt") #skrivs om kontrollen lyckas

        except Syntaxfel as fel: #fångar ett syntaxfel och sparar undantagsobjektet i fel
            rest = "" #skapar en tom sträng för de olästa tecknen

            while not q.isEmpty(): #fortsätter så länge tecken finns kvar i kön
                rest += q.dequeue() #tar ut nästa tecken och lägger till det i strängen

            if rest != "": #kontrollerar om det fanns några olästa tecken
                print(str(fel) + " " + rest) #skriver felmeddelandet och den olästa delen
            else: #används om kön var tom efter felet
                print(str(fel)) #skriver bara felmeddelandet

        text = input() #läser nästa rad efter att den aktuella formeln har behandlats