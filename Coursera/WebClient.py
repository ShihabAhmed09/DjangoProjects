import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('127.0.0.1', 9000))
cmd = 'GET http://127.0.0.1/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(), end='')

mysock.close()

# An Even Simpler Web Client:
# import urllib.request
#
# fhand = urllib.request.urlopen('http://127.0.0.1:9000/romeo.txt')
# for line in fhand:
#     print(line.decode().strip())
