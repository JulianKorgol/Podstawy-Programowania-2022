import matplotlib.pyplot as plt

S1 = float(input("Wprowadź S1: "))
S2 = float(input("Wprowadź S2: "))
F1 = 100

def Obliczenia(s1, s2, f1):
    f1Lista = []
    f2Lista = []

    for i in range(1, f1+1):
        f1Lista.append(i)

    for i in f1Lista:
        f2 = (s2/s1) * i
        f2Lista.append(f2)

    plt.plot(f1Lista, f2Lista)
    plt.show()

Obliczenia(S1, S2, F1)