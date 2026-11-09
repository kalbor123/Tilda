from LinkedQFile import LinkedQ #hämtar köklassen från filen i samma mapp

STORA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
SMÅ = "abcdefghijklmnopqrstuvwxyz"
SIFFROR = "0123456789"
ATOMER = """H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr
Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd
In Sn Sb Te I Xe Cs Ba La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf
Ta W Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn Fr Ra Ac Th Pa U Np Pu Am Cm
Bk Cf Es Fm Md No Lr Rf Db Sg Bh Hs Mt Ds Rg Cn Fl Lv""".split() #delar texten till en lista med godkända atomsymboler

class Syntaxfel(Exception): #undatgasklass som ärver från exception, används för fel
    pass #inget extra beteende behövs utöver det som ärvs från Exception

def skapa_kö(text):
    q = LinkedQ()
    for tecken in text:
        q.enqueue(tecken)
    return q

def read_formel(q): #kontrollerar hela formeln
    read_mol(q) #läser formelns grupper

    if not q.isEmpty(): #kontrollerar om det finns olästa tecken kvar
        raise Syntaxfel("Felaktig gruppstart vid radslutet") #avbryter om hela formeln inte kunde läsas

def read_mol(q): #läser en eller flera grupper
    read_group(q) #läser den första gruppen som alltid måste finnas

    if not q.isEmpty(): #undersöker om det finns fler tecken
        if q.peek() != ")": #fortsätter om nästa tecken inte avslutar en parentes
            read_mol(q) #anropar samma funktion för att läsa nästa grupp och resten

def read_group(q): #läser en atomgrupp eller en parentesgrupp
    if q.isEmpty(): #kontrollerar om gruppen saknar innehåll
        raise Syntaxfel("Felaktig gruppstart vid radslutet") #en grupp måste innehålla något

    if q.peek() == "(": #väljer parentesalternativet om nästa tecken är en vänsterparentes
        q.dequeue() #läser bort vänsterparentesen
        read_mol(q) #kontrollerar grupperna inuti parentesen

        if q.peek() != ")": #kontrollerar att innehållet följs av en högerparentes
            raise Syntaxfel("Saknad högerparentes vid radslutet") #avbryter om parentesen saknas

        q.dequeue() #läser bort högerparentesen

        if q.isEmpty(): #kontrollerar om formeln tog slut direkt efter parentesen
            raise Syntaxfel("Saknad siffra vid radslutet") #en parentesgrupp måste följas av ett antal

        if q.peek() not in SIFFROR: #kontrollerar att nästa tecken är en siffra
            raise Syntaxfel("Saknad siffra vid radslutet") #avbryter om antalet saknas

        read_num(q) #läser antalet och kontrollerar att det är tillåtet

    elif q.peek() in STORA or q.peek() in SMÅ: #väljer atomalternativet om nästa tecken är en bokstav
        read_atom(q) #läser och kontrollerar atomsymbolen

        if not q.isEmpty(): #kontrollerar om det finns något tecken kvar
            if q.peek() in SIFFROR: #undersöker om atomen följs av ett antal
                read_num(q) #läser antalet om det finns

    else: #hanterar tecken som inte kan börja en grupp
        raise Syntaxfel("Felaktig gruppstart vid radslutet") #avbryter exempelvis för en ensam siffra eller högerparentes

def read_atom(q): #läser en atomsymbol och kontrollerar att den är godkänd
    atom = read_LETTER(q) #läser den stora bokstaven och sparar den i atom

    if not q.isEmpty(): # kontrollerar att det finns ett tecken att titta på
        if q.peek() in SMÅ: # undersöker om nästa tecken är en liten bokstav
            atom += read_letter(q) #läser den lilla bokstaven och lägger till den i atom

    if atom not in ATOMER: #kontrollerar om atomsymbolen saknas i listan
        raise Syntaxfel("Okänd atom vid radslutet") #avbryter kontrollen om atomen är okänd

def read_LETTER(q):
    if q.isEmpty(): #kontrollerar om kön är tom
        raise Syntaxfel("Saknad stor bokstav vid radslutet")

    if q.peek() not in STORA: #kontrollerar stor bokstav
        raise Syntaxfel("Saknad stor bokstav vid radslutet")

    return q.dequeue() #tar bort och returnerar bokstaven till anropande funktion

def read_letter(q):
    if q.isEmpty(): #kontrollerar om kön är tom
        raise Syntaxfel("Saknad liten bokstav vid radslutet")

    if q.peek() not in SMÅ: #kontrollerar om
        raise Syntaxfel("Saknad liten bokstav vid radslutet")

    return q.dequeue() #tar bort och returnerar bokstaven till anropande funktion

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
            read_formel(q)  # kontrollerar hela formeln i stället för bara en grupp
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


