#Made by Nauczyciel TechniSchools
#Made in 2021-11-23
def szyfr(text, secret):
    napis = ""
    for x in text:
        if ord(x) >= ord('a') and ord(x) <= ord('z'):
            a = ord(x) + secret
            napis += chr(a)
        else:
            a = ord('a') + (ord(x)+secret-ord('z'))
            napis += chr(a)
        if ord(x) >= ord('A') and ord(x) <= ord('Z'):
            a = ord(x) + secret
            napis += chr(a)
        else:
            a = ord('A') + (ord(x) + secret - ord('Z'))
            napis += chr(a)
    return napis
#Moim zdaniem w pełni nie działa