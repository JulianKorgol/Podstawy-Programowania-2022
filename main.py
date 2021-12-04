import math

liczba = int(input("Podaj liczbę do której mam szukać: "))
nowaliczba = liczba*liczba
tab = [True for i in range (nowaliczba+1)]

def liczbypierwsze(tab, liczba):
    is_prime = tab
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(math.sqrt(liczba))+1):
        if tab[i] == True:
            print(i, end=" ") #Wyświetla
            for j in range(i*i, liczba+1, i):
                tab[j] = False
    return tab

liczbypierwsze(tab, nowaliczba)