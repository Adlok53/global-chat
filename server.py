import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 1111))

server.listen()

client, address = server.accept()

flag = True

while flag:
    msg = client.recv(1024).decode('utf-8')
    if msg == 'quit':
        flag = False
    else:
        print(msg)
    client.send(input('Server: ').encode('utf-8'))

client.close()
server.close()