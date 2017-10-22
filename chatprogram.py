#Connect to the other computer
def connect(conn):
	print(conn)
	return


#Send text
def Send(sendtext):
	print(sendtext)
	return
def sendingstuff():

	ip = input("What is the other computer's ip address?")
	connect(ip)




	textToSend = input("What do you want to send?")

	Send(textToSend)

def main():
	print("Welcome to my simple chat program")

	recive = input("Do you want to send or receive text? SEND/RECEIVE   ")

	if(recive == "RECEIVE"):
		#do things
		print("this funcinality has not been added :(")
	if(recive == "SEND"):
		sendingstuff()

main()


