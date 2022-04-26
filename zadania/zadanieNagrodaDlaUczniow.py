import math

liczbaKlas = int(input())
dane = ""
klasy = []

def merge(arr, l, p):
    i_l = 0
    i_p = 0
    i = 0
    while i_l < len(l) and i_p < len(p):
        if l[i_l][2] > p[i_p][2]:
            arr[i] = l[i_l]
            i_l += 1
        elif l[i_l][2] == p[i_p][2]:
            arr[i] = l[i_l]
            i_l += 1
        else:
            arr[i] = p[i_p]
            i_p += 1
        i += 1
    while i_l < len(l):
        arr[i] = l[i_l]
        i += 1
        i_l += 1
    while i_p < len(p):
        arr[i] = p[i_p]
        i += 1
        i_p += 1



def sortowanie(tab):
    if len(tab) > 1:
        s = len(tab)//2
        left = tab[:s]
        right = tab[s:]
        sortowanie(left)
        sortowanie(right)
        merge(tab, left, right)



# Przyjmowanie danych i podział danych na klasy
for i in range(liczbaKlas):
    dane = ""
    klasy = []
    while dane != "-":
        dane = input()
        klasy.append(dane.split())
    klasy.pop()
    sortowanie(klasy)
    dlugoscPosortowane = math.ceil(len(klasy)/10)
    doPrintu = ""
    for i in range(dlugoscPosortowane):
        doPrintu = klasy[i][0]
        doPrintu += klasy[i][1]
        print(doPrintu)
    print("-")