text = input("Text: ")
secret = int(input("Secret: "))

def szyfrCezara(text, secret):
    newsecret = secret % 26
    nowy = ""
    for n in text:
        if ord(n) + newsecret > ord('z') or (ord('Z') < ord(n) + newsecret < ord('a')):
            nowy += chr(ord(n) + newsecret - 26)
        else:
            nowy += chr(ord(n) + newsecret)
    return nowy

# W pełni jeszcze nie działa.
# def deszyfrCezara(text, secret):
#     newsecret = (secret % 26) * -1
#     nowy = ""
#     for n in text:
#         if ord(n) + newsecret > ord('z') or (ord('Z') < ord(n) + newsecret < ord('a')):
#             nowy += chr(ord(n) + newsecret - 26)
#         else:
#             nowy += chr(ord(n) + newsecret)
#     return nowy

print(szyfrCezara(text, secret))
#print(deszyfrCezara(text, secret))