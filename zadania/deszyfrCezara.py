text = input("Text: ")
starysecret = int(input("Secret: "))
secret = starysecret * -1

def szyfrCezara(text, secret):
    newsecret = secret % 26
    nowy = ""
    for n in text:
        if ord(n) + newsecret > ord('z') or (ord('Z') < ord(n) + newsecret < ord('a')):
            nowy += chr(ord(n) + newsecret - 26)
        else:
            nowy += chr(ord(n) + newsecret)
    return nowy


print(szyfrCezara(text, secret))