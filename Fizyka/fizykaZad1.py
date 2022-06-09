S1 = float(input("Wprowadź S1: "))
S2 = float(input("Wprowadź S2: "))
F1 = float(input("Wprowadź F1: "))

def Tloki(s1, s2, f1):
    f2 = (f1 * s2) / s1
    return f2

print(str(Tloki(S1, S2, F1)) + "N")