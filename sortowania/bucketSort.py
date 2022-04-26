#Bucket sort - nie było mnie
arr = [0.78, 0.17, 0.39, 0.26, 0.72,0.94, 0.21, 0.12, 0.23, 0.68]

def bucket_sort(arr, k):
    buckets = [[] for i in range(k)]
    bucket_range = (max(arr) - min(arr)) / k
    for a in arr:
        nr = int((a - min(arr)) // bucket_range)
        if nr == k:
            nr -= 1
        buckets[nr].append(a)
    for b in buckets:
        b.sort()
    return buckets

print(bucket_sort(arr, 1))