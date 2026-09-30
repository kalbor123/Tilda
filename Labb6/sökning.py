import timeit  # Används för att mäta söktider.
from labb6 import läs_fil  # Hämtar inläsningsfunktionen från labb6.py.

# Källa: ChatGPT.
def linjärsökning(låtar, söktitel):  # Tar emot listan och titeln vi söker.
    for låt in låtar:  # Undersöker ett låtobjekt i taget.
        if låt.låttitel == söktitel:  # Jämför objektets titel med söktiteln.
            return låt  # Returnerar första objektet med rätt titel.

    return None  # Ingen matchande titel hittades.

# Källa: ChatGPT. Listan måste vara sorterad efter låttitel.
def binärsökning(låtar, söktitel):  # Tar emot den sorterade listan och titeln vi söker.
    vänster = 0  # Första index i sökområdet.
    höger = len(låtar) - 1  # Sista index i sökområdet.

    while vänster <= höger:  # Fortsätter så länge någon position återstår.
        mitten = (vänster + höger) // 2  # Beräknar mittenpositionen.
        låt = låtar[mitten]  # Hämtar låtobjektet på den positionen.

        if låt.låttitel == söktitel:  # Kontrollerar om titeln stämmer.
            return låt  # Returnerar det hittade objektet och avslutar.

        elif låt.låttitel < söktitel:  # Söktiteln kommer efter mittenobjektets titel.
            vänster = mitten + 1  # Fortsätter i den högra halvan.

        else:  # Söktiteln kommer före mittenobjektets titel.
            höger = mitten - 1  # Fortsätter i den vänstra halvan.

    return None  # Titeln saknas om hela sökområdet har uteslutits.


def main():  # Samlar stegen som programmet ska utföra.
    låtar = läs_fil("unique_tracks.txt")  # Läser filen och tar emot låtlista
    #låtar = låtar[:250000] #slicar listan

    söktitel = "Låt_som_inte_finns_i_listan"
    träff = linjärsökning(låtar, söktitel)  # Anropar sökfunktionen och sparar dess svar.

    if träff is not None:  # Kontrollerar att sökningen hittade en låt
        print(träff.låttitel)  # Skriver ut låten från det hittade objektet.
        print(låtar.index(träff))  # Skriver ut index för det hittade låtobjektet

    else:  # om ingen låt hittas
        print("Låttiteln hittades inte.")


    linjtid = timeit.timeit(stmt=lambda: linjärsökning(låtar, söktitel), number=100) # tidtagning för linjärsökning
    print("Linjärsökning:", linjtid, "sekunder")

    #sorterar listan eftersom vi måste ha en sorterad lista för att använda binärsökning
    sorterade_låtar = låtar.copy()  # Skapar en separat lista med samma låtobjekt
    sorterade_låtar.sort(key=lambda låt: låt.låttitel)  # Sorterar efter låttitel

    binärträff = binärsökning(sorterade_låtar, söktitel)  # Söker efter samma titel som vid linjärsökningen

    if binärträff is not None:  # Kontrollerar att ett låtobjekt hittades
        print(binärträff.låttitel)  # Skriver ut titeln från det hittade objektet
    else:  # Körs om titeln inte hittades
        print("Låttiteln hittades inte.")

    binärtid = timeit.timeit(stmt=lambda: binärsökning(sorterade_låtar, söktitel), number=100) #tidtagning, binärsökning
    print("Binärsökning:", binärtid, "sekunder")

    låttabell = {}  # Skapar en tom dictionary

    for låt in låtar:  # Går igenom alla låtobjekt
        låttabell[låt.låttitel] = låt  # Sparar objektet med titeln som nyckel



    hashträff = låttabell.get(söktitel)  # Söker efter titeln när tabellen är färdig

    if hashträff is not None:  # Kontrollerar om ett objekt hittades.
        print(hashträff.låttitel)  # Skriver ut den hittade titeln.
    else:  # Körs om titeln saknas.
        print("Låttiteln hittades inte.")  # Meddelar att ingen träff finns.

    hashtid = timeit.timeit(stmt=lambda: låttabell.get(söktitel), number=100)  # tidtag för hashsök
    print("Hashtabell:", hashtid, "sekunder")  # Skriver ut den sammanlagda tiden.

main()
