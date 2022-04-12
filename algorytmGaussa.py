'''
1. a - reszta z dzielenia obecnego roku na 19
2. b - reszta z dzielenia obecnego roku na 4
3. c - reszta z dzielenia obecnego roku na 7
4. d - reszta z dzielenia a*19+24 przez 30
5. e - reszta z dzielenia (2*b + 4*c + 6*d + 5) przez 7
6. w = 22 + d + e
if (d == 29 and e == 6) or (d==28 and e ==6):
    w -= 7
if w > 31:
    w -= 31
'''

rok = int(input())

def algorytmGaussa(rok):
    a = rok % 19
    b = rok % 4
    c = rok % 7
    d = (a*19+24)%30
    e = (2*b + 4*c + 6*d + 5)%7
    w = 22+d+e
    if (d == 29 and e == 6) or (d == 28 and e == 6):
        w -= 7
    if w > 31:
        w -= 31
    return w

print(algorytmGaussa(rok))
