
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
	

def main():
	print("Welcome to my simple chat program")

	recive = input("Do you want to send or receive text? SEND/RECEIVE   ")

	if(recive == "RECEIVE"):
		#do things
		print("this funcinality has not been added :(")
	if(recive == "SEND"):
		sendingstuff()

main()


