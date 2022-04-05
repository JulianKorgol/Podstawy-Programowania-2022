# Sam sobie zadanie zmodyfikowałem
peselInput = int(input())
liczby = list(map(int,str(peselInput)))

def pesel(liczba):
    a = int(liczba[0])
    b = int(liczba[1])
    c = int(liczba[2])
    d = int(liczba[3])
    e = int(liczba[4])
    f = int(liczba[5])
    g = int(liczba[6])
    h = int(liczba[7])
    i = int(liczba[8])
    j = int(liczba[9])
    k = int(liczba[10])
    stanOperacyjny = a*1 + b*3 + c*7 + d*9 + e*1 + f*3 + g*7 + h*9 + i*1 + j*3 + k*1
    return stanOperacyjny

if len(liczby) > 11 or len(liczby) < 11:
    print("Pesel nieprawidłowy")
else:
    stanPooperacyjny = pesel(liczby)
    stanKrytyczny = list(map(int,str(stanPooperacyjny)))
    stanSuper = stanKrytyczny[len(stanKrytyczny)-1]
    if stanSuper == 0:
        print("Pesel prawidłowy")
    else:
        print("Pesel nieprawidłowy")