from bintreeFile import Bintree

svenska = Bintree()
english = Bintree()

with open("word3.txt", "r", encoding = "utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()                # Ett trebokstavsord per rad
        if ordet in svenska:      #anropar __contains__ automatiskt
            print(ordet, end = " ")
        else:
            svenska.put(ordet)             # in i sökträdet
print("\n")

with open("engelska.txt", "r", encoding="utf-8") as englishfile:
    for rad in englishfile:
        words = rad.split()

        for word in words:
             if word not in english:
                 english.put(word)

                 if word in svenska:
                    print(word,  end=" ")
