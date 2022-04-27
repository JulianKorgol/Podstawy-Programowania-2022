pDInput = input()
pD = []
pD.append(pDInput.split())
p = int(pD[0][0])
d = int(pD[0][1])

def bucketSort(arr, k):
    buckets = [[] for i in range(k)]
    srednie = []
    for i in arr:
        srednie.append(i[1])
    x = max(srednie)
    y = min(srednie)
    bucket_range = (x - y)/k
    for a in arr:
        nr = int((a[1] - y) // bucket_range)
        if nr == k:
            nr -= 1
        buckets[nr].append(a)
    posortowane = []
    for b in buckets:
        b.sort(key= lambda x: x[1])
        for x in b:
            posortowane.append(x)
    return posortowane

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
        posortowane = bucketSort(osoby, 8)
        print(*posortowane[:5], sep=' ')
        osoby = posortowane[5:]


zadanie(p, d)







