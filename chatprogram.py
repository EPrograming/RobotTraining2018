
import socket
HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 8000              # Arbitrary non-privileged port
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
	HOST = input("what is the other computer ip")    # The remote host
	PORT = 8000              # The same port as used by the server
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	    s.connect((HOST, PORT))
	    s.sendall(b'Hello, world')
	    data = s.recv(1024)
	print('Received', repr(data))

def main():
	print("Welcome to my simple chat program")

	recive = input("Do you want to send or receive text? SEND/RECEIVE   ")

	if(recive == "RECEIVE"):
		#do things
		getstuff()
	if(recive == "SEND"):
		sendingstuff()

main()


