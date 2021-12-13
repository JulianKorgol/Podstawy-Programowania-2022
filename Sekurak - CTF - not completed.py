import socket
import math

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('192.46.238.236', 1337))
data = b''

# data = s.recv(1000)
# print(data)
while not b'>' in data:
    data += s.recv(1)

data = data.decode('utf-8').split('a * a + b * b = ')[1].split('\n\n')[0]
# print("OTRZYMALEM")
# s.sendall('1212'.encode("utf-8"))
# print("WYSLALEM")
# answer = s.recv(100).decode('utf-8')
# print("OTRZYMALEM")
# print(answer)
# number = int(data)
#
# print(data)
#
# obliczenie = (number/2)
# obliczeniepierwiastek = math.sqrt(obliczenie)
# wynik = int(obliczeniepierwiastek)
# print(wynik)
wynik = 1234
s.sendall(f'{wynik} {wynik}'.encode("utf-8"))
print('WYSLALEM')
answer = s.recv(100).decode('utf-8')
print(answer)