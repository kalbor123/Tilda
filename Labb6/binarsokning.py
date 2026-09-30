# Källa: ChatGPT. Listan måste vara sorterad i stigande ordning.
def binary_search(the_list, key):  # Tar emot listan och värdet vi söker.
    left = 0  # Första index som fortfarande kan innehålla värdet.
    right = len(the_list) - 1  # Sista index som fortfarande kan innehålla värdet.

    while left <= right:  # Fortsätter så länge sökområdet innehåller något.
        middle = (left + right) // 2  # Beräknar index i mitten av sökområdet.

        if the_list[middle] == key:  # Kontrollerar om vi har hittat värdet.
            return True  # Avslutar funktionen och meddelar att värdet finns.

        elif the_list[middle] < key:  # Värdet i mitten är mindre än sökvärdet.
            left = middle + 1  # Fortsätter till höger om mitten.

        else:  # Värdet i mitten är större än sökvärdet.
            right = middle - 1  # Fortsätter till vänster om mitten.

    return False  # Sökområdet är tomt: värdet finns inte i listan.

def main():  # Sköter inläsning och utskrift för kattis
    indata = input().strip()  # Läser raden med sorterade ord.
    the_list = indata.split()  # Skapar en lista av orden.
    key = input().strip()  # Läser första sökvärdet.

    while key != "#":  # Fortsätter tills stopptecknet anges.
        print(binary_search(the_list, key))  # Skriver ut sökningens svar.
        key = input().strip()  # Läser nästa sökvärde.


main()  # Startar just denna fils huvudprogram