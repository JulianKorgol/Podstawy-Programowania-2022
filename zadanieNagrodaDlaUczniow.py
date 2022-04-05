import math

liczbaKlas = int(input())
dane = ""
klasy = []

def merge(arr, l, p):
    i_l = 0
    i_p = 0
    i = 0
    while i_l < len(l) and i_p < len(p):
        if l[i_l] < p[i_p]:
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
    while dane != "-":
        dane = input()
        klasy.append(dane.split())
    posortowane = sortowanie(klasy)
    dlugoscPosortowane = math.ceil(len(posortowane))/10
    for i in range(dlugoscPosortowane-1):
        doPrintu = posortowane[i][0]
        doPrintu += posortowane[i][1]
    print("-")