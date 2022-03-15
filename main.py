tab = [9, 1, 2, 7, 3, 5, 8, 7]

def m_sort():
    if len(tab) > 1:
        s = len(tab)//2
        left = tab[:s]
        right = tab[s:]
        m_sort(left)
        m_sort(right)
        merge(tab, left, right)



# print(tab[0])
# print(tab[0:2])