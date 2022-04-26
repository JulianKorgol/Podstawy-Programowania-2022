banknoty = [500, 200, 100, 50, 20, 10, 5, 2, 1]
reszta = 433
doWydania = reszta
doWydaniaBanknoty = []

# Mój kod
while doWydania > 0:
    for i in range(len(banknoty)):
        while doWydania >= banknoty[i]:
            if doWydania >= banknoty[i]:
                doWydania = doWydania - banknoty[i]
                doWydaniaBanknoty.append(banknoty[i])

print("Do wypłacenia: ", reszta)
print("W banknotach: ", doWydaniaBanknoty)










# Kod Pana
# r = int(input())
# n = [500, 200, 100, 50, 20, 10, 5, 2, 1]
#
# w = []
# i = 0
# while r > 0:
#     if r >= n[i]:
#         w.append(n[i])
#         r -= n[i]
#     else:
#         i+=1
# print(w)