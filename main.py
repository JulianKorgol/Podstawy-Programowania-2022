#Bucket sort - nie było mnie
arr = [0.78, 0.17, 0.39, 0.26, 0.72,0.94, 0.21, 0.12, 0.23, 0.68]
print(arr)

def bucketSort(tab):
    najwieksza = max(tab)
    najmniejsza = min(tab)
    bucket = []
    for i in range(len(tab)):
        bucket.append([])
    for liczba in tab:
        index = int(10 * liczba)
        bucket[index].append(liczba)
    for liczba2 in range(len(tab)):
        bucket[liczba2] = sorted(bucket[liczba2])

    k=0
    for i in range(len(tab)):
        for j in range(len(bucket[i])):
            tab[k] = bucket[i][j]
            k += 1
    return tab



print(bucketSort(arr))

# https://www.programiz.com/dsa/bucket-sort