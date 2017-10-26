import tkinter
from tkinter import Tk, Frame
import socket

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 8000              # Arbitrary non-privileged port
save = "NO"
# firsttime = "YES"

root = Tk()
root.title("A Python Chat Program")
# def Button1():
#     listbox.insert(END, "button1 pressed")
textframe = Frame(root)
listframe = Frame(root)


def connect(toSend):
    #HOST = ''
    # textToSend = input("What do you want to send?")
    b = toSend.encode('utf-8')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(1)
        conn, addr = s.accept()
        with conn:
            text_contents = text.get()
            listbox.insert(tkinter.END, 'Connected by', addr)
            # print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(b)


def getstuff():
    global SAVE
    global HOST
    global PORT
    HOST = ''
    #print(host)
    PORT = 8000              # The same port as used by the server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b'Hello, world')
        data = s.recv(1024)
    text_contents = text.get()
    listbox.insert(tkinter.END, 'Received', repr(data))


def Button3():
    text_contents = text.get()
    connect(text_contents)
    listbox.insert(tkinter.END, "sent successfully:")
    listbox.insert(tkinter.END, text_contents)
    text.delete(0, tkinter.END)


def ReturnInsert(event):
    Button3()

# button1 = Button(root, text="button1", command = Button1)
# button2 = Button(root, text="button2")


button3 = tkinter.Button(textframe, text="Send Data", command=Button3)
label1 = tkinter.Label(textframe, text="Other computer's IP")
E1 = tkinter.Entry(textframe, bd=5)


def getDate():
    global HOST
    HOST = E1.get()


submit = tkinter.Button(textframe, text="Submit IP", command=getDate)
refresh = tkinter.Button(listframe, text="Refresh", command=getstuff)
text = tkinter.Entry(textframe)
scrollbar = tkinter.Scrollbar(listframe, orient=tkinter.VERTICAL)
listbox = tkinter.Listbox(listframe, yscrollcommand=scrollbar.set)

scrollbar.configure(command=listbox.yview)
text.bind("<Return>", ReturnInsert)
text.pack(side=tkinter.LEFT, fill=tkinter.X, expand=1)
# button1.pack()
# button2.pack()
label1.pack(side=tkinter.LEFT)
submit.pack(side=tkinter.LEFT)
E1.pack()
refresh.pack(side=tkinter.LEFT)
button3.pack(side=tkinter.LEFT)
listbox.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=1)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
textframe.pack(fill=tkinter.X)
listframe.pack(fill=tkinter.BOTH, expand=1)
submit.pack(side=tkinter.RIGHT)
root.geometry("600x400")
root.mainloop()