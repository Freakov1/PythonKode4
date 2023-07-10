from socket import *
import requests
import json

serverPort = 14014
serverSocket = socket(AF_INET, SOCK_DGRAM)
api_url = "http://localhost:5213/api/EasterEggs"
headers = {'Content-type': 'application/json'}

serverAddress = ('255.255.255.255', serverPort)

serverSocket.bind(serverAddress)
print("The server is ready")
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    decoded_message = message.decode()
    print(decoded_message)
    words = decoded_message.split()

    # Using data and headers instead of json, as the data is already json encoded, using json= would
    # double encode it, and would not be a valid object.
    response = requests.put(api_url + "/" + words[1] + "?productno=" + words[1], data=decoded_message, headers=headers)
    print(response.json())