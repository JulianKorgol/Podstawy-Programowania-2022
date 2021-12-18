from math import sqrt
##Można działać na wielu plikach w jednym programie/skrypcie/funkcji.

#Generowanie liczb losowych
#Znajdowanie liczb losowych
#Znajdowanie konkretnej liczby z tablicy liczb pierwszych

def eratostenes(n):
    is_prime = [True] * (n+1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(sqrt(n))+1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    primes = []
    for i in range(n):
        if is_prime[i]:
            primes.append(i)
    return primes

arr = eratostenes(618)

def binarysearch(arr, x):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < x:
            left = mid + 1
        elif arr[mid] > x:
            right = mid -1
        else:
            return mid
    return -1

n = 618
x = 331
arr = eratostenes(n)
index = binarysearch(arr, x)
print(index)

#importowanie funkcji z innego pliku
#from cezar import cezar
#from revision.cezar import cezar
#from revision.binary_search import arr
#Szczegółowe informacje na zdjęciu.

#Zasady czystego kodu:
#importy
#definicje funkcji
#deklaracje zmiennych
#program(ciało programu)

#Na sprawdzian:
#ASCI
#Wyszukiwanie ze zbioru
#Konwersja (szyfrowanie), konwertowanie na liczby i póxniejsze operacje na nim.

#Można korzystać z notatek i internetu, jednak musimy rozumieć co to robi.