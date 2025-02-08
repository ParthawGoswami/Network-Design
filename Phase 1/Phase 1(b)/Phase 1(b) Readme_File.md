# Title and Authors
•	Phase 1 (b): UDP File Transfer with RDT 1.0  
•	Parthaw Goswami 02196346
# Environment
•	What OS we used for our code. e.g.: Windows  
•	The name of the programming language we used: Python.  
•	The version of programming language:  Python 3.10  
# Files inside .zip Folder (Network-Design.zip)
•	Phase 1 Folder
1.	Phase 1(a) Folder
-	Phase 1(a) Readme_File
-	udpclient.py
-	udpserver.py 
2.	Phase 1(b) Folder
-	Phase 1(b) Readme_File
-	ImageServer.py 
-	ClientServer.py
-	tricolor.bmp (file that has been sent)
-	received_image.bmp (file that has been received)
3.	Design Document Phase 1
# Instructions
1.	Create two distinct files titles “ClientServer.py” and “ImageServer.py” on PC.  
2.	Copy and paste the code supplied in the question for Client.py and Server.py into the relevant files generated.  
3.	Ensure that the original .bmp file is in the same directory as ClientServer.py.  
4.	Ensure that the installed version of Python is compatible with the code. The code was created and evaluated using Python 3.10.  
5.	Open a terminal (Windows command prompt) and go to the folder containing the two Python files.  
6.	The following command will initiate the ImageServer.py script: **Python ImageServer.py**
   The result should say “The server is ready to receive”  

8.	Open a second terminal (command prompt on Windows) and go to the directory containing the two Python files.  
9.	To initiate the ClientServer.py script, use the following command: **Python ClientServer.py**

The output should display the hostname and IP address of the client as well as a message indicating that the client is connected to the server.  

9.	Once the ClientServer.py script has completed executing, a new “received_image.bmp” file should be created in the same folder as the two Python scripts.  
10.	When the transfer is completed, the connection between the server and client will close.  
