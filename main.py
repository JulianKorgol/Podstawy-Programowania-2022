# Zadanie1
text = input("Text: ")
secret = int(input("Secret: "))

def szyfrCezara(text, secret):
    newsecret = secret % 26
    nowy = ""
    for n in text:
        if ord(n) + newsecret > ord('z') or (ord('Z') < ord(n) + newsecret < ord('a')):
            nowy += chr(ord(n) + newsecret - 26)
        else:
            nowy += chr(ord(n) + newsecret)
    return nowy


print(szyfrCezara(text, secret))

# Zadanie2
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

arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
z = 8

print(binarysearch(arr, z))

# Zadanie3
def myBigTestFunction(text):
    lista = []
    for n in text:
        lista.append(ord(n))
    maximum = max(lista)
    return maximum

slowo = input()
print(myBigTestFunction(slowo))

# Zadanie4
from math import sqrt

def sito(n):
    is_prime = [True] * (n+1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(sqrt(n))+1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    primes = []
    for i in range(n+1):
        if is_prime[i]:
            primes.append(i)
    return primes

def myBigTestFunction(text):
    lista = []
    for n in text:
        lista.append(ord(n))
    minimum = min(lista)
    return minimum

napis = input()
najmniejszaWartosc = myBigTestFunction(napis)
print(sito(najmniejszaWartosc))