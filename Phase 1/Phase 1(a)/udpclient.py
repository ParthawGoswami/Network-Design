# echo-client.py

import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 12000  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as clientSocket:
    print(f"Client is connected to server")
    message = "HELLO"
    clientSocket.sendto(message.encode(), (HOST, PORT)) # sends the message to the server
    print(f"Client is sending message...")
    message, serverAddress = clientSocket.recvfrom(2048) # read server's reply and get address of sender
print(f"Received from server: {message.decode()}") # print server's reply
