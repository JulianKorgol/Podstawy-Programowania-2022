# Insertion sort

zbior = [4, 3, 8, 1, 2, 9]

def insertionSort(zbior):
    for i in range(1, len(zbior)):
        j = zbior[i]
        k = i-1
        while k>=0 and j < zbior[k]:
            zbior[k+1] = zbior[k]
            k -= 1
        zbior[k+1] = j
    print(zbior)

insertionSort(zbior)
