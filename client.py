import socket
import threading

nickname = input("Choose a nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascli')
            if message == 'NICK':
                client.send(nickname.encode('ascli'))
            else:
                print(message)
        except:
            print("An error occerred!")
            client.close()
            break

def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('ascli'))

receive_thread = threading.Thread(target=receive())
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()