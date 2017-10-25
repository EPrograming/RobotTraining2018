from tkinter import *
import socket
HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 8000              # Arbitrary non-privileged port
save = "NO"
#firsttime = "YES"

root = Tk()
root.title("A Python Chat Program")
#def Button1():
#	listbox.insert(END, "button1 pressed")
textframe = Frame(root)
listframe = Frame(root)
def connect(toSend):
	#textToSend = input("What do you want to send?")
	b = toSend.encode('utf-8')
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	    s.bind((HOST, PORT))
	    s.listen(1)
	    conn, addr = s.accept()
	    with conn:
	        text_contents = text.get()
	        listbox.insert(END, 'Connected by', addr)
	        #print('Connected by', addr)
	        while True:
	            data = conn.recv(1024)
	            if not data: break

	            conn.sendall(b)
def getstuff():
	global save
	global host
	global port


	PORT = 8000              # The same port as used by the server
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	    s.connect((HOST, PORT))
	    s.sendall(b'Hello, world')
	    data = s.recv(1024)
	text_contents = text.get()
	listbox.insert(END, 'Received', repr(data))
	
def Button3():
	text_contents = text.get()
	connect(text_contents)
	listbox.insert(END, "sent successfully:")
	listbox.insert(END, text_contents)


	text.delete(0,END)
def ReturnInsert(event):
	Button3()

#button1 = Button(root, text="button1", command = Button1)
#button2 = Button(root, text="button2")
button3 = Button(textframe, text="Send Data", command = Button3)
label1 = Label(textframe, text="Other computer's IP")
E1 = Entry(textframe, bd =5)
def getDate():
	HOST = E1.get


submit = Button(textframe, text ="Submit IP", command = getDate)
refresh = Button(listframe, text="Refresh", command = getstuff)
text = Entry(textframe)
scrollbar = Scrollbar(listframe, orient=VERTICAL)
listbox = Listbox(listframe, yscrollcommand=scrollbar.set)
scrollbar.configure(command=listbox.yview)



text.bind("<Return>", ReturnInsert)
text.pack(side=LEFT, fill=X, expand=1)
#button1.pack()
#button2.pack()
label1.pack(side=LEFT)
submit.pack(side=LEFT)
E1.pack()
refresh.pack(side=LEFT)
button3.pack(side=LEFT)
listbox.pack(side=LEFT,fill=BOTH, expand=1)
scrollbar.pack(side=RIGHT, fill=Y)
textframe.pack(fill=X)
listframe.pack(fill=BOTH, expand=1)
submit.pack(side=RIGHT)
root.geometry("600x400")
root.mainloop()