pDInput = input()
pD = []
pD.append(pDInput.split())
p = int(pD[0][0])
d = int(pD[0][1])

def bucketSort(arr):
    buckets = [[] for i in range(1)]
    x = max(arr)
    y = min(arr)
    x = x[1]
    y = y[1]
    bucket_range = (x - y)
    for a in arr:
        a = a[1]
        nr = int((a - y) // bucket_range)
        if nr == 1:
            nr -= 1
        # print(nr)
        # print(a)
        buckets[nr].append(a)
    for b in buckets:
        b.sort()
    return buckets

def zadanie(p, d):
    osoby = []
    doPrintu = []
    for i in range(d):
        n = int(input())
        for i in range(n):
            uczen = input()
            uczen = uczen.split()
            uczen[0] = int(uczen[0])
            uczen[1] = float(uczen[1])
            osoby.append(uczen)
    # print(osoby)
    posortowane = bucketSort(osoby)
    print(posortowane)
    for i in range(p):
        doPrintu.append(posortowane[i])
    return doPrintu


print(zadanie(p, d))