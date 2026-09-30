class Låt:
    def __init__(self, trackid, låtid, artistnamn, låttitel): # tar emot låtens uppgifter
        self.trackid = trackid #sparar trackid
        self.låtid = låtid #sparar låt
        self.artistnamn = artistnamn #sparar artist
        self.låttitel = låttitel #sparar titel

    def __lt__(self, other):
        return self.artistnamn < other.artistnamn

def läs_fil(filnamn):  # Tar emot namnet på filen som ska läsas.
    låtar = []  # Skapar en tom lista som vi senare ska lägga låtobjekten i.

    with open(filnamn, "r", encoding="utf-8") as fil:
        for rad in fil:  # Hämtar en rad i taget
            låtupg = rad.rstrip("\n").split("<SEP>")  # delar filraden till en lista med fyra uppgifter/strängar
            låt = Låt(låtupg[0], låtupg[1], låtupg[2], låtupg[3])  # Skapar ett låtobjekt från låtupg
            låtar.append(låt) #listar låtobjektet (sist i listan)


    return låtar  # returnerar listan efter att hela filen har lästs
