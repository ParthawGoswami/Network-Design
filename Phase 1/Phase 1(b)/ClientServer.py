
import socket
import os
import base64

# ************ function definitions ************
def MakeOutputPacketArray(fileToRead):
	#all of the packets that we are going to send out
	packetsToSend = []
	#open our file that is in the same directory of out python script
	with open(fileToRead, "rb") as file:
		#indefinitely loop our file
		while True:
			packet = file.read(1024)
			#once we have reached the end of our .bmp file, we need to exit our while loop
			if not packet:
				break
			#create our array of packets to output
			packetsToSend.append(packet)
	retutn packetsToSend



#setup the client UDP
#we will use a generic estabilishment, thus will work on any pc
serverName = socket.gethostname()
print("Host client name: " + serverName)
serverHostIP = socket.gethostbyname(serverName)
print("Host server IP: " + serverHostIP)
HOST = serverHostIP
clientPort = 12000
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print(f"Client is now connected to the server")


#server connection has now been established. Now that we have our server working 
#we should now work on splitting up our image

#source of image: https://people.math.sc.edu/Burkardt/data/bmp/bmp.html

#fileDir = os.environ.get("PythonApplication1")
fileName = "tricolor.bmp"
#call our make packet function
outputImage = MakeOutputPacketArray(fileName)
count = 0
#all of our packets are now in our outputImage array, we now need to parse this array and send each packet one by one.
for packet in outputImage:
	#base64 must be used to encode each packt before sending them over, base64 will be used to decode each packet on the server side as well
	#we need to send packets 1 by 1. We will wait for a message back from the server stating that the packet has been processed, this will let us know we can move on to the next packet to send
	#if this message does not state the packet has been processed, we will continue to wait and listen to the server to hear back that the packet that was sent has been processed
	#start off by sending 1 packet over to the server
	encodePacket = base64.b64encode(packet)
	clientSocket.sendto(encodePacket, (serverName, clientPort))
	messageFromServer, serverAddress = clientSocket.recvfrom(2048)
	messageFromServer = messageFromServer.decode()
	#we now must wait for our server to tell us that it has processed our packet and then we can move on to our next packet
	while messageFromServer != "packet processed":
		messageFromServer = ""
		messageFromServer, serverAddress = clientSocket.recvfrom(2048)
		messageFromServer = messageFromServer.decode()
	count += 1

finalMessage = b"last-packet-sent"
encodeFinalMessage = base64.b64encode(finalMessage)
clientSocket.sendto(encodeFinalMessage, (serverName, clientPort))
print("packet sent {count}")
print("all packets sent, shutting down client")
clientSocket.close()	
