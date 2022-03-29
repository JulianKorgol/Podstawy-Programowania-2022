# Zadanie "Nagroda dla uczniów"
szkola = globals()
liczbaKlas = int(input())
dane = ""
klasy = []

# Przyjmowanie danych
for i in range(liczbaKlas):
    dane = ""
    while dane != "-":
        dane = input()
        klasy.append(dane.split())

# Podział danych na klasy
def podzialdanych(klasy):
    dlugoscTablicy = len(klasy)
    x = 1
    # print(klasy)
    for i in range(len(klasy)):
        runned = False
        if klasy[i][0] == '-' or i == 0:
            szkola['klasa_{0}'.format(x)] = []
            x += 1
            runned = True
        # https://stackoverflow.com/questions/9553638/find-the-index-of-an-item-in-a-list-of-lists
        numer = next(((y, klasy.index('-'))
            for y, klasy in enumerate(klasy)
            if '-' in klasy),
            None)
        if numer != None:
            numer = numer[0]
            klasy.pop(numer)
            print(numer)
            for i in range(numer):
                szkola['klasa_{0}'.format(x - 1)].append(klasy[i])
        print(szkola['klasa_{0}'.format(x - 1)].append(klasy[i]))
    print(klasa_1)

podzialdanych(klasy)
# print(klasy)