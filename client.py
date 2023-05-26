PORT  = 8080
IP_ADDRESS = '127.0.0.1'
SERVER = None
BUFFER_SIZE = 4096

from tkinter import *
from tkinter import ttk
from tkinter import filedialog

def musicWindow():
    
    print("IP MESSENGER")
    window=Tk()
    window.title("messenger")
    window.geometry("500*500")
    nameLabel=Label(window,text="entr your name",font=("calibri",10))
    nameLabel.place(x=10,y=8)
    name=Entry(window,width=30,font=("calibri",10))
    name.place(x=120,y=8)
    name.focus()
    connectServer=Button(window,text="connect to chat server",bd =1,font=("calibri",10))
    connectServer.place(x=350,y=6)
    separator=ttk.Separator(window,orinet="horizontal")
    separator.place(x=0,y=35,relwidth=1,relheight=0.1)
    connectButton=Button(window,text="connect",bd=1,font=("calbiri",10))
    connectButton.place(x=282,y=160)
    disconnectButton=Button(window,text="disconnect",bd=1,font=("calbiri",10))
    disconnectButton.place(x=350,y=160)
    refresh=Button(window,text="refresh",bd=1,font=("calbiri",10))
    refresh.place(x=435,y=160)
    window.mainloop()



def setup():
    global SERVER
    global PORT
    global IP_ADDRESS

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.connect((IP_ADDRESS, PORT))

    musicWindow()
setup()