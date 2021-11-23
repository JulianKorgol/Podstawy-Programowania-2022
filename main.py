text = input("Text: ")
secret = int(input("Secret: "))

def szyfrCezara(text, secret):
    arr = text
    nowy = ""
    for i in range(len(arr)):
        cyfra = ord(arr[i])
        cyfra += int(secret)
        if cyfra > ord("z"):
            cyfranowa = ord("a") + ((cyfra+secret)-ord("z"))
        zmienionyCiag = chr(cyfranowa)
        nowy += zmienionyCiag
    print(nowy)

def deszyfrCezara(szyfr, secret):
    arr = szyfr
    nowy = ""
    for i in range(len(arr)):
        cyfra = ord(arr[i])
        cyfra -= int(secret)
        if cyfra > ord("z"):
            cyfranowa = ord("a") + ((cyfra+secret)-ord("z"))
            cyfra = cyfranowa
        zmienionyCiag = chr(cyfra)
        nowy += zmienionyCiag
    print(nowy)



deszyfrCezara(text, secret)