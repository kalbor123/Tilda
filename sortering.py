import timeit  # Används för att mäta sorteringstider.
from labb6 import läs_fil  # Hämtar samma inläsningsfunktion som sökprogrammet använder.

# Källa: ChatGPT. Urvalssortering efter låttitel.
def urvalssortering(låtar):  # Sorterar den mottagna listan på plats.
    for plats in range(len(låtar) - 1):  # Går igenom positionerna som ska fyllas.
        minst = plats  # Antar först att det minsta återstående elementet står här.

        for kandidat in range(plats + 1, len(låtar)):  # Undersöker positionerna till höger.
            if låtar[kandidat].låttitel < låtar[minst].låttitel:  # Jämför titlarna.
                minst = kandidat  # Sparar positionen för den mindre titeln.

        låtar[plats], låtar[minst] = låtar[minst], låtar[plats]  # Byter plats på objekten.

# Källa: ChatGPT.
def mergesort(låtar):  # Tar emot listan som ska sorteras.
    if len(låtar) <= 1:  # En tom lista eller ett enda objekt är redan sorterat.
        return låtar  # Lämnar tillbaka listan direkt.

    mitten = len(låtar) // 2  # Beräknar var listan ska delas.
    vänster = mergesort(låtar[:mitten])  # Sorterar vänstra halvan med samma funktion.
    höger = mergesort(låtar[mitten:])  # Sorterar högra halvan med samma funktion.

    resultat = []  # Samlar objekten i sorterad ordning.
    v = 0  # Index för nästa objekt att undersöka i vänstra halvan.
    h = 0  # Index för nästa objekt att undersöka i högra halvan.

    while v < len(vänster) and h < len(höger):  # Fortsätter medan båda halvorna har objekt kvar.
        if vänster[v].låttitel <= höger[h].låttitel:  # Jämför de två nästa titlarna.
            resultat.append(vänster[v])  # Lägger till objektet från vänster.
            v += 1  # Flyttar till nästa position i vänstra halvan.
        else:  # Titeln i högra halvan kommer först.
            resultat.append(höger[h])  # Lägger till objektet från höger.
            h += 1  # Flyttar till nästa position i högra halvan.

    resultat.extend(vänster[v:])  # Lägger till eventuella kvarvarande objekt från vänster.
    resultat.extend(höger[h:])  # Lägger till eventuella kvarvarande objekt från höger.

    return resultat  # Returnerar den sammanslagna, sorterade listan.

def main():  # Samlar sorteringsmätningarna.
    låtar = läs_fil("unique_tracks.txt")  # Läser in låtarna i ursprunglig ordning.

    sorteringslista = låtar[:1000]  # Skapar en separat lista med de första 1 000 låtarna.

    urvalstid = timeit.timeit(stmt=lambda: urvalssortering(sorteringslista), number=1)  # Mäter en sortering.
    print("Urvalssortering", urvalstid, "sekunder")  # Skriver ut tiden.

    mergelista = låtar[:100000]  # Skapar en lista med de första 1 000 låtarna i ursprunglig ordning.

    mergetid = timeit.timeit(stmt=lambda: mergesort(mergelista), number=1)  # Mäter en körning av mergesort.
    print("Mergesort", mergetid, "sekunder")  # Skriver ut sorteringstiden.

main()
