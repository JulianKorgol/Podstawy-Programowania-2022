# Zadanie 8.7 -> Nie działa
# liczbaLiczb = int(input())
# lista = []
#
#
# for i in range(liczbaLiczb):
#     ciag = input().split()
#     imie = ciag[0]
#     wzrost = int(ciag[1])
#     razem = [imie, wzrost]
#     lista.append(razem)
#
# def najwieksza(zbior):
#     funkcyjna = []
#     for i in range(liczbaLiczb):
#         wartosc = zbior[i][1]
#         funkcyjna.append(wartosc)
#     najwieksza = max(funkcyjna)
#     mojIndex = funkcyjna.index(najwieksza)
#     return mojIndex
#
# mojIndex = najwieksza(lista)
# print(lista[mojIndex])


# Zadanie 8.8
# liczbaLiczb = int(input())
# lista = []
#
# for i in range(liczbaLiczb):
#     liczba = int(input())
#     lista.append(liczba)
#
# def Average(liczba):
#     avg = sum(liczba) / len(liczba)
#     return avg
#
# print(Average(lista))


# Zadanie 8.10
liczbaLiczb = int(input())
lista = []


for i in range(liczbaLiczb):
    ciag = input().split()
    imie = ciag[0]
    waga = int(ciag[1])
    razem = [imie, waga]
    lista.append(razem)
    lista.sort()

def listy(zbior):
    najmniejsza = zbior[0]
    lista1 = [x for x in zbior if x >= 20]
    return lista1


print(listy(lista))
