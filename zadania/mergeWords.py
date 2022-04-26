firstWord = input()
secondWord = input()

def merge(fword, sword):
    fwordLen = int(len(fword))
    swordLen = int(len(sword))
    final = []
    if fwordLen > swordLen:
        for i in range(swordLen):
            final.append(fword[i])
            final.append(sword[i])
    else:
        for i in range(fwordLen):
            final.append(fword[i])
            final.append(sword[i])
    finalConverted = ''.join(final)
    return finalConverted

print(merge(firstWord, secondWord))