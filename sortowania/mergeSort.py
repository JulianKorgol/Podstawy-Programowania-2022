tab = [9, 1, 2, 7, 3, 5, 8, 7]

def merge(arr, l, p):
    i_l = 0
    i_p = 0
    i = 0
    while i_l < len(l) and i_p < len(p):
        if l[i_l] < p[i_p]:
            arr[i] = l[i_l]
            i_l += 1
        else:
            arr[i] = p[i_p]
            i_p += 1
        i += 1
    while i_l < len(l):
        arr[i] = l[i_l]
        i += 1
        i_l += 1
    while i_p < len(p):
        arr[i] = p[i_p]
        i += 1
        i_p += 1



def m_sort(tab):
    if len(tab) > 1:
        s = len(tab)//2
        left = tab[:s]
        right = tab[s:]
        m_sort(left)
        m_sort(right)
        merge(tab, left, right)


m_sort(tab)
print(tab)