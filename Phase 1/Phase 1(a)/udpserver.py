import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on 

# AF_INET = internet address family for IPv4 (Internet Protocol)
# SOCK_DGRAM = Socket type for UDP
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as serverSocket: # Creates a socket object
    serverSocket.bind(('', PORT)) # associate the socket with host and port
    print ("Server Socket Established.")
    print ("The server is ready to receive")

    while True: # infinite while loop for data
        message, clientAddress = serverSocket.recvfrom(2048) # reads data from client and get address of sender
        if not message:
            break
        # Converts the data to a string
        input_string = message.decode()
        serverSocket.sendto(input_string.encode(), clientAddress) # echos the data back to the sender
        print(f"Input from client = {message.decode()}")
        print(f"Server is sending back the input: {input_string}")
        break
