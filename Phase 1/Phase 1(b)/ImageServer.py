import socket
import base64
serverPort = 12000
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind(("",serverPort))
print("The server is ready to receive")
imageReconstruct = []
while True: #continue loop to read data from the client
	packet, clientAddress = serverSocket.recvfrom(2048)
	print("Packet has been received from the client")
	#decode our packet from the client
	decodedPacket = base64.b64decode(packet)
	if decodedPacket -- b"last-packet-sent":
		break
	imageReconstruct.append(decodedPacket)
	#tell the client that we have processed the packet
	message = "packet processed"
	serverSocket.sendto(message.encode(), clientAddress)

print("Now process the packets and construct the new image file")
# put together our image
with open("received_image.bmp", "wb") as file:
	for packet in imageReconstruct:
		file.write(packet)

serverSocket,close()
