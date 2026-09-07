from bintreeFile import Bintree

swedish = Bintree()
english = Bintree()

with open("word3.txt", "r", encoding="utf-8") as swedishfil:
    for rad in swedishfil:
        word = rad.strip()

        if word in swedish:
            print(word, end=" ")
        else:
            swedish.put(word)
print()

with open("engelska.txt", "r", encoding="utf-8") as englishfile:
    for rad in englishfile:
        words = rad.split()

        for word in words:
             if word not in english:
                 english.put(word)

                 if word in swedish: 
                    print(word,  end=" ")