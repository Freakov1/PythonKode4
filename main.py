from socket import *
from time import sleep
import random
import json

serverName = '255.255.255.255'
serverPort = 14014

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

while True:
    AmountSold = random.randint(1, 10)
    message = {"productNo": 8013, "Amount Sold": AmountSold}
    clientSocket.sendto(json.dumps(message).encode(), (serverName, serverPort))
    print("Sent message: " + json.dumps(message))
    sleep(random.randint(1, 3))
clientSocket.close()