# Zad 1

# import math
#
# liczba = int(input("Podaj liczbę: "))
# pierwiastek = int(math.sqrt(liczba))
#
# isPrime = True
# for i in range(2, pierwiastek+1):
#     if (liczba%i)==0:
#         isPrime = False
#         break
# if isPrime:
#     print('Jest pierwsza.')
# else:
#     print("Nie jest pierwsza.")

# Zad 2
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
            print(i, end=" ")
            for j in range(i*i, liczba+1, i):
                tab[j] = False
    return tab

liczbypierwsze(tab, nowaliczba)

# Trzeba użyć whila.
# while n > len(tab)