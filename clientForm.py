import socket
import json
import threading
import time
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
from tkinter import scrolledtext
import random
import asyncio
from bleak import BleakScanner
import asyncio
from threading import Event


class Client:
    def __init__(self, CF, X, Y, bip, power, nl) -> None:
        self.IP = str(random.randint(0, 255))+'.'+str(random.randint(0, 255))+'.'+str(random.randint(0, 255))+'.'+str(random.randint(0, 255))
        #self.name = socket.gethostname()
        #self.IP = socket.gethostbyname(self.name)
        self.CF = CF
        self.distance = 0.01
        self.state = 1
        self.X = X
        self.Y = Y
        self.bip = bip
        self.power = power
        self.nl = nl
        self.stop_event = Event()
        
    async def getDistance(self):
        while True:
            if self.stop_event.is_set():
                break
            d = await BleakScanner.find_device_by_address(self.bip)
            if not d is None:
                self.distance = 10**((self.power - d.rssi)/(10*self.nl))
                self.CF.lprint(str(d.name) + ' ' + str(d.address) + ' ' + str(d.rssi) + ' ' + str(self.distance))
                
        self.CF.lprint("Bluetooth search process finished")
        
            
    def connect_to_server(self, IP, port):
        self.CF.lprint("Client started")
        self.sock = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect ((IP, port))
        self.CF.lprint("Client connected to the server: " + str(IP) + " on " + str(port) + " port")
        while True:
            if self.stop_event.is_set():
                break
            if not self.sendMessage():
                break
            time.sleep (3)
            
    def sync(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.getDistance())
        loop.close()
                
    def startThreads(self, IP, port):
        self.stop_event.clear()
        self.clientThread = threading.Thread (target = self.connect_to_server, args=(IP, port))
        self.clientThread.start ()
        self.blueThread = threading.Thread(target = self.sync)
        self.blueThread.start ()
    
    def stopThreads(self):
        self.stop_event.set()
        self.CF.lprint("Client stopped")
    
    def sendMessage(self):
        try:
            self.data_send = """{"time": "%s", "distance": %s, "X": %s,"Y": %s,"IP": "%s", "state": %s}""" % (time.ctime(), self.distance, self.X, self.Y, self.IP, self.state)
            self.sock.sendall (self.data_send.encode('utf-8'))
            self.data = self.sock.recv(1024).decode("utf-8")
            self.CF.lprint(self.data)
            return 1
        except ConnectionAbortedError:
            self.CF.server_aborted()
            self.CF.lprint("Server connection was aborted ")
            return 0


class ClientForm:
    def __init__(self, mainform) -> None:
        self.mainform = mainform
        self.state = 0
    def click_on_button(self):
        #messagebox.showinfo("Статус клиента", "Клиент запущен", parent = self.clientWindow)
        self.state = 1
        self.status("1")
        self.client = Client(self, float(self.x_entry.get()), float(self.y_entry.get()), self.bip, self.power, self.nl)
        self.client.startThreads(self.IP_adress_entry.get(), int(self.port_entry.get()))
        self.on_off_button['text'] = "Отключиться от сервера"
        self.on_off_button['command'] = self.click_off_button
        self.IP_server_label['text'] = f"IP адрес севера: {self.IP_adress_entry.get()}"
        self.mainform.window.withdraw()

    def click_off_button(self):
        #messagebox.showinfo("Статус клиента", "Клиент завершил работу", parent = self.clientWindow)
        self.client.stopThreads()
        self.state = 0
        self.status("0")
        self.client.state = 0
        self.client.sendMessage()
        self.client.sock.close()
        self.on_off_button['text'] = "Подключиться к серверу"
        self.on_off_button['command'] = self.click_on_button
        
    def server_aborted(self):
        self.status("2")
        self.client.sock.close()
        self.on_off_button['text'] = "Подключиться к серверу"
        self.on_off_button['command'] = self.click_on_button
        
    def status(self, key):
        if key == '1':
            self.canvas.itemconfig(self.r, fill='#708090') 
            self.canvas.itemconfig(self.y, fill='#708090') 
            self.canvas.itemconfig(self.g, fill='green')
            
        elif key == '0':
            self.canvas.itemconfig(self.r, fill='red') 
            self.canvas.itemconfig(self.g, fill='#708090') 
            self.canvas.itemconfig(self.y, fill='#708090') 

        elif key == '2':
            self.canvas.itemconfig(self.r, fill='#708090') 
            self.canvas.itemconfig(self.g, fill='#708090') 
            self.canvas.itemconfig(self.y, fill='darkorange') 
            
    def on_closing(self):
        if self.state == 1:
            self.click_off_button()
        self.clientWindow.destroy()
        if self.state == 1:
            self.mainform.window.destroy()
        else:
            self.mainform.window.deiconify()
            
    def lprint(self, text, both = True):
        if both:
            print(text)
        if not self.clientWindow is None:
            try:
                self.logs.insert(END, str(text) + "\n")
                self.logs.see("end")
            except:
                pass
        
    def openClientWindow(self, bip, power, nl):  
        self.bip = bip
        self.power = power
        self.nl = nl
        swHei = 600
        swWid = 800
        self.clientWindow = Tk()
        self.clientWindow.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.clientWindow.title("Клиент")
        self.clientWindow.resizable(0, 0)
        self.clientWindow.wm_attributes("-topmost", 1)
        self.clientWindow.iconbitmap("123.ico")
        self.clientWindow.geometry(str(swWid)+'x'+str(swHei))

        frame0 = Frame(self.clientWindow, width = 800, height = 100, bg = '#E0FFFF')
        frame1 = Frame(self.clientWindow, width = 400, height = 100, bg = '#E0FFFF')
        frame2 = Frame(self.clientWindow, width = 400, height = 100, bg = '#E0FFFF')
        frame4 = Frame(self.clientWindow, width = 800, height = 100, bg = '#E0FFFF')
        frame5 = Frame(self.clientWindow, width = 800, height = 200, bg = '#E0FFFF')
        frame6 = Frame(self.clientWindow, width = 800, height = 100, bg = '#E0FFFF')
        frame7 = Frame(self.clientWindow, width = 400, height = 100, bg = '#E0FFFF')
        frame8 = Frame(self.clientWindow, width = 400, height = 100, bg = '#E0FFFF')
        frame9 = Frame(self.clientWindow, width = 400, height = 100, bg = '#E0FFFF')

        frame0.place(relx = 0, rely = 0, relwidth = 1, relheight = 0.055)
        frame1.place(relx = 0, rely = 0.04, relwidth = 0.5, relheight = 0.15)
        frame2.place(relx = 0.5, rely = 0.04, relwidth = 0.5, relheight = 0.15)
        frame6.place(relx = 0, rely = 0.13, relwidth = 1, relheight = 0.055)
        frame7.place(relx = 0, rely = 0.17, relwidth = 0.5, relheight = 0.15)
        frame8.place(relx = 0.5, rely = 0.17, relwidth = 0.5, relheight = 0.15)
        frame4.place(relx = 0.5, rely = 0.32, relwidth = 0.5, relheight = 0.1)
        frame5.place(relx = 0, rely = 0.42, relwidth = 1, relheight = 0.58)
        frame9.place(relx = 0, rely = 0.32, relwidth = 0.5, relheight = 0.1)

        mydir = ""
        self.IP_adress = StringVar()
        self.port = StringVar()
        self.X = StringVar()
        self.Y = StringVar()

        self.IP_server_label = Label(frame0, text="IP адрес севера: ", bg = '#E0FFFF')
        self.IP_adress_label = Label(frame1, text="IP адрес:", bg = '#E0FFFF')
        self.port_label = Label(frame2, text="Порт:", bg = '#E0FFFF')
        self.x_label = Label(frame7, text="X:", bg = '#E0FFFF')
        self.y_label = Label(frame8, text="Y:", bg = '#E0FFFF')

        self.IP_adress_entry = Entry(frame1, textvariable=self.IP_adress)
        self.port_entry = Entry(frame2, textvariable=self.port)
        self.port_entry.insert(END, "8888")
        self.x_entry = Entry(frame7, textvariable=X)
        self.x_entry.insert(END, str(random.randint(-10, 10)))
        self.y_entry = Entry(frame8, textvariable=Y)
        self.y_entry.insert(END, str(random.randint(-10, 10)))

        self.IP_server_label.pack(side = LEFT, anchor="w", padx=300, pady=10)

        self.IP_adress_label.pack(side = LEFT, anchor="w", padx=35, pady=30)
        self.IP_adress_entry.pack(side = LEFT, anchor="w", padx=10, pady=30, ipadx = 50)
        self.IP_adress_entry.focus()

        self.port_label.pack(side = LEFT, anchor="w", padx=35, pady=30)
        self.port_entry.pack(side = LEFT, anchor="w", padx=10, pady=30, ipadx = 50)


        self.x_label.pack(side = LEFT, anchor="w", padx=35, pady=30)
        self.x_entry.pack(side = LEFT, anchor="w", padx=10, pady=30, ipadx = 50)

        self.y_label.pack(side = LEFT, anchor="w", padx=35, pady=30)
        self.y_entry.pack(side = LEFT, anchor="w", padx=10, pady=30, ipadx = 50)

        self.on_off_button = Button(frame9, text="Включить клиента", command=self.click_on_button)
        self.on_off_button.pack(side = TOP)

        self.server_status_label = Label(frame4, text="Статус подключения:", bg = '#E0FFFF')
        self.server_status_label.place(relx = 0, rely = 0.10)

        self.canvas = Canvas(frame4, width = 100, height = 40, bg = '#E0FFFF')

        self.r = self.canvas.create_oval(10, 10, 30, 30, fill="#708090")
        self.y = self.canvas.create_oval(40, 10, 60, 30, fill="#708090")
        self.g = self.canvas.create_oval(70, 10, 90, 30, fill="#708090")

        self.canvas.place(relx = 0.50, rely = 0)
        
        self.logs = scrolledtext.ScrolledText(frame5, height=500, width=800, bg = 'black', fg='white')
        self.logs.insert(END, "")
        self.logs.see("end")
        self.logs.pack(side = BOTTOM)
        self.clientWindow.mainloop()