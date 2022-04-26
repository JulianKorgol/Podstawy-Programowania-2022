zbior = [10, 8, 7, 9, -3]
# zbior = [-5, -10, 7, 2]

def sortowanieBombelkowe(zbior):
    x = 1
    for i in range(len(zbior)-1):
        if zbior[i] > zbior[i+1]:
            lewa = zbior[i]
            prawa = zbior[i+1]
            zbior[i] = prawa
            zbior[i+1] = lewa
        for i in range(len(zbior) - x):
            if zbior[i] > zbior[i + 1]:
                lewa = zbior[i]
                prawa = zbior[i + 1]
                zbior[i] = prawa
                zbior[i + 1] = lewa
                x=+1
    print(zbior)

sortowanieBombelkowe(zbior)