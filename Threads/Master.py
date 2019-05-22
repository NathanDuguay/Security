import socket
import threading

tabClient = []

bind_ip = "10.0.0.2"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip, bind_port))

server.listen(5)

print("Le serveur attend une connexion")


def thread_recevoir_client(client_socket):
    while True:
        request = client_socket.recv(1024)
        print("[*] Received %s" % request)


def thread_connexion():
    client, addr = server.accept()
    tabClient.append(tabClient[client])

    while True:
        print("[*] Accepted Connection from %s:%d" % (addr[0], addr[1]))
        thread_recevoir_client = threading.Thread(target=thread_recevoir_client, args={client, })
        thread_recevoir_client.start()
while True:
    texte = input()
    tabClient.send(str.encode(texte))
