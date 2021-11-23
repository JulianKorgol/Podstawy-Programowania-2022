text = input("Text: ")
secret = int(input("Secret: "))

def szyfrCezara(text, secret):
    arr = text
    nowy = ""
    for i in range(len(arr)):
        cyfra = ord(arr[i])
        cyfra += int(secret)
        if cyfra > ord("z"):
            cyfra -= 27
        zmienionyCiag = chr(cyfra)
        nowy += zmienionyCiag
    print(nowy)

def deszyfrCezara(szyfr, secret):
    arr = szyfr
    nowy = ""
    for i in range(len(arr)):
        cyfra = ord(arr[i])
        cyfra -= int(secret)
        if cyfra > ord("z"):
            cyfra -= 27
        zmienionyCiag = chr(cyfra)
        nowy += zmienionyCiag
    print(nowy)



deszyfrCezara(text, secret)