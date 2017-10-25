
import socket
HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 8000              # Arbitrary non-privileged port
save = "NO"
firsttime = "YES"
print(save)
#Connect to the other computer
def connect():
	textToSend = input("What do you want to send?")
	b = textToSend.encode('utf-8')
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	    s.bind((HOST, PORT))
	    s.listen(1)
	    conn, addr = s.accept()
	    with conn:
	        print('Connected by', addr)
	        while True:
	            data = conn.recv(1024)
	            if not data: break

	            conn.sendall(b)
	
	


#Send text



def sendingstuff():

	#ip = input("What is the other computer's ip address?")
	#ipint = int(ip)
	



	
	
	connect()
	
def getstuff():
	global save
	global host
	global port
	global firsttime
	if(save == "NO"):
		HOST = input("what is the other computer ip ")    # The remote host
		save = input("do you want to save this ip? YES/NO ")
		firsttime = "NO"
		
	elif(save == "YES"):
		if(firsttime == "YES"):
			HOST = input("what is the other computer ip ")    # The remote host
			save = input("do you want to save this ip? YES/NO ")
			firsttime = "NO"
		else:
			return


	PORT = 8000              # The same port as used by the server
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	    s.connect((HOST, PORT))
	    s.sendall(b'Hello, world')
	    data = s.recv(1024)
	print('Received', repr(data))
	main()

def restart():
	recive = input("Do you want to send or receive text? SEND/RECEIVE   ")

	if(recive == "RECEIVE"):
		#do things
		getstuff()
	if(recive == "SEND"):
		
		sendingstuff()

def main():
	print("Welcome to my simple chat program")

	recive = input("Do you want to send or receive text? SEND/RECEIVE   ")

	if(recive == "RECEIVE"):
		#do things
		getstuff()
	if(recive == "SEND"):
		
		sendingstuff()

main()


