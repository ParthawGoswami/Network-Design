# Title and Authors

•	Phase 1(a):  transfer a message (Say “HELLO”) from the UDP client to the UDP server and then ECHO the message back from the UDP server to the UDP client.    
•	Parthaw Goswami 02196346  
# Environment

•	Windows OS  
•	Python 3.10 (64-bit)  
•	Visual Studio 2019  
# Instructions

1.	Download the “Phase1(a).zip” file and export the file to Visual Studio.  
a.	Extract the contents of the zip folder. Place the newly extracted folder in a destination in which is easy to access, such as “Desktop” or leave it in “Downloads”.  
b.	This file contains the “Phase1(a)” Folder which contains a “Design_File”, “Readme_File”, “udpclient.py”, and “udpserver.py”.  
c.	The files that will be used to run the client and server will be “udpclient.py” and “udpserver.py”.  
d.	Ensure Visual Studio is downloaded on your Windows OS.  

2.	To get started, right click on the “udpclient.py” and “udpserver.py” files and click “Open with” then choose “Visual Studio” from one of the options. Verify that both client and server files are opened on Visual Studio.  

3.	Once the files are opened and you are able to see the code for each server and client, navigate or search for “cmd” (command prompt) on your Windows machine. Open two command prompts so both the client and server can be run. Navigate to your directory by typing in “cd” and the directory name (“cd desktop”). Do this until you have reached the final directory and can access the client and server files.  
4.	When reaching the end of the directory, you are able to run the client and server files. IMPORTANT: The server file must be started up first and then the client.  
i.	To run the “udpserver.py” file: Enter the command “py udpserver.py” in the command line.  
ii.	To run the “udpclient.py” file: Enter the command “py udpclient.py” in the command line.  

# Expected Behavior
1.	When the “udpserver” is run, the command line will remain open and waits for a client connection.  
a.	“Server Socket Established.”  
b.	“The server is ready to receive”  
2.	When the “udpclient” is run, a “HELLO” message will be sent to the server.  
a.	At the start you will see two messages:  
i.	“Client is connected to server”  
ii.	“Client is sending message…”  
b.	Two new lines will show up indicating the client’s input.  
i.	“Input from client = HELLO”  
ii.	“Server is sending back the input: HELLO”  
c.	On the client command line you will see a message that the server has sent back the message:  
i.	“Received from server: HELLO”  

# Information of IDE

•	Visual Studio 2019  
•	Python 3.10 (64-bit)  

## References
1.	Vokkarane, V. (2023). Socket Programming 101 in Python [Programming].
