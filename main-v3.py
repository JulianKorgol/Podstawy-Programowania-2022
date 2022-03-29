# Zadanie "Nagroda dla uczniów"
szkola = {}
liczbaKlas = int(input())
dane = ""
klasy = []

# Przyjmowanie danych
for i in range(liczbaKlas):
    dane = ""
    print(i)
    szkola[f"klasa{i}"]= []
    while dane != "-":
        dane = input()
        doDodania = dane.split()
        print(doDodania)
        szkola[f"klasa{i}"].append(doDodania)

print(klasa1)
print(klasa2)
