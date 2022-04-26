# https://www.remnote.com/w/626702873955700016366d8f/Algorytm-pakowania-plecaka-5bWYv8uLuE7Nzmchj

waga = int(input("Ile kg możesz unieść: "))
liczbaPrzedmiotow = int(input("Ile produktów masz? "))
produkty = []
produkt = []


for i in range(liczbaPrzedmiotow):
    nowyProdukt = input("Wprowadź waga oraz wartość produktu oddzielając spacją: ")
    produkt = nowyProdukt.split()
    produkty.append(produkt)

