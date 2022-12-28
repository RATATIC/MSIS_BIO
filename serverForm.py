from collections.abc import Mapping
import socket
import json
import threading
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
from tkinter import scrolledtext
import numpy as np
from PIL import Image
from bleak import BleakScanner
import asyncio
import time
from threading import Event

#mtx = threading.Lock()

class Server:
    data = {}
    connections = []
    distance = 0.01
    target = [0, 0]
    stop_event = Event()
    
    def __init__(self, SF, bip, power, nl) -> None:
        self.SF = SF
        self.bip = bip
        self.power = power
        self.nl = nl
    
    def circle(self, N, x, y, r):
        A = np.arange(- y + 1,N - y + 1)**2
        B = np.arange(- x + 1,N - x + 1)**2
        dists = np.sqrt(A[:,None] + B)
        return (dists <= r).astype(int)

    def deviations(self, N, x, y, r):
        A = np.arange(- y + 1,N - y + 1)**2
        B = np.arange(- x + 1,N - x + 1)**2
        dists = np.sqrt(A[:,None] + B)
        return dists - r
    
    def ring(self, N, x, y, r):
        eps = 0.0000001
        n = 1
        W = N/3
        A = np.arange(- y + 1,N - y + 1)**2
        B = np.arange(- x + 1,N - x + 1)**2
        dists = np.sqrt(A[:,None] + B)
        # Gauss
        #ring = np.exp(-((dists**2 - r**2)/(dists*W))**2)
        # Butterworth
        ring = 1-(1/(1+((dists*W)/((dists**2 - (r)**2)+eps)**(2*n))+eps))
        return ring

    def getTargetCoords(self):
        N = 500
        eps = 0.001
        scale = 20
        mmap = np.zeros((N, N))
        amount = len(self.data) + 1 
        masks = np.zeros((amount, N,N))
        for i, (x, y, r) in enumerate(self.data.values()):
            masks[i] = self.deviations(N, int(x*scale+N/2), int(y*scale+N/2), r * scale)
            #masks[i][masks[i].astype(bool)] = 1/(r**2)
            mmap = mmap + masks[i]**2
        masks[-1] = self.deviations(N, int(N/2), int(N/2), self.distance * scale)
        #masks[-1][masks[-1].astype(bool)] = 1/(self.distance**2)
        mmap = mmap + masks[-1]**2
        mmap = np.sqrt(mmap)
        temp = np.where(mmap < np.min(mmap) + eps)
        device_coords = [int(np.mean(temp[1]) - N/2)/scale, int(np.mean(temp[0]) - N/2)/scale]
        device_vis = self.circle(N, device_coords[0]*scale + N/2, device_coords[1]*scale + N/2, N/100)
        mmap[device_vis.astype(bool)] = 0
        mmap = (mmap-np.min(mmap))*255/(np.max(mmap)-np.min(mmap))
        img = Image.fromarray(mmap).convert("L")
        img.save('Maps/current_map.png')
        return device_coords

    async def getDistance(self):
        while True:
            if self.stop_event.is_set():
                break
            d = await BleakScanner.find_device_by_address(self.bip)
            if not d is None:
                self.distance = 10**((self.power - d.rssi)/(10*self.nl))
                self.SF.lprint(str(d.name) + ' ' + str(d.address) + ' ' + str(d.rssi) + ' ' + str(self.distance))
                
        self.SF.lprint("Bluetooth search process finished")
        
                    
    def recv_data(self, conn):
        try:
            temp = conn.recv(1024).decode("utf-8")
            temp = json.loads(temp)
        except :
            self.SF.lprint("Client aborted connection")
            return -1
        if temp['state']:
            self.data[temp['IP']] = [int(temp['X']), int(temp['Y']), float(temp['distance'])]
        else:
            self.data.pop(temp['IP'], None)
        if not temp:
            return -1
        self.target = self.getTargetCoords()
        self.SF.lprint('Distance to ' + str(temp['IP']) + ' is ' + str(temp['distance']) + ' and its state is ' + str(temp['state']))
            

    def connection_thread(self, conn, addr):
        while True:
            if self.recv_data(conn) == -1 or self.stop_event.is_set():
                break
            try:
                conn.sendall ('Server successfully recieved the data'.encode ('utf-8'))
            except ConnectionResetError:
                self.SF.lprint("Cannot answer - connection aborted by host")
        conn.close ()

    def create_listen_sock(self, IP, port):
        self.SF.lprint("Server started")
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((IP, port))
        self.sock.listen(10)
        self.sockthrds = []
        while True:
            if self.stop_event.is_set():
                for thread, con in zip(self.sockthrds, self.connections):
                    thread.join()
                    con
                    time.sleep(1)
                    con.close()
                self.sockthrds = []
                break
            try:
                self.conn, self.addr = self.sock.accept()
                self.SF.lprint("Client " + str(self.addr[0]) +  " has joined the server")
                self.connections.append(self.conn)
                self.sockthrds.append(threading.Thread(target = self.connection_thread, args=((self.conn, self.addr))))
                self.sockthrds[-1].start()
            except OSError:
                self.SF.lprint("Server acception was aborted")
            
           
            
    def sync(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.getDistance())
        loop.close()
   
    def startThreads(self, IP, port):
        self.stop_event.clear()
        self.serverThread = threading.Thread(target = self.create_listen_sock, args=(IP, port))
        self.serverThread.start()
        self.blueThread= threading.Thread(target = self.sync)
        self.blueThread.start()
        
    def stopThreads(self):
        self.stop_event.set()
        time.sleep(1)
        self.sock.close()
        self.SF.lprint("Server stopped")


class ServerForm:

    def __init__(self, mainform) -> None:
        self.mainform = mainform
        self.state = 0
        
    def click_on_button(self):
        #messagebox.showinfo("Статус сервера", "Сервер запущен", parent = self.serverWindow)
        self.state = 1
        self.status("1")
        self.server = Server(self, self.bip, self.power, self.nl)
        self.server.startThreads(self.IP_adress_entry.get(), int(self.port_entry.get()))
        
        self.on_off_button['text'] = "Выключить сервер"
        self.on_off_button['command'] = self.click_off_button
        self.mainform.window.withdraw()

    def click_off_button(self):
        #messagebox.showinfo("Статус сервера", "Сервер завершил работу", parent = self.serverWindow)
        # for conn in self.server.connections:
        #     conn.shutdown(socket.SHUT_RDWR)
        #     conn.close()
        #self.server.sock.shutdown(socket.SHUT_RDWR)
        self.server.stopThreads()
        self.state = 0
        self.status("0")
        self.on_off_button['text'] = "Включить сервер"
        self.on_off_button['command'] = self.click_on_button
        
    
    def refresh_map(self):
        self.mainform.setCoords(self.server.data, self.server.target, self.server.distance)
        self.mainform.repaint()
        self.mainform.window.deiconify()

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
        self.serverWindow.destroy()
        if self.state == 1:
            self.mainform.window.destroy()
        else:
            self.mainform.window.deiconify()
        
    def lprint(self, text, both = True):
        if both:
            print(text)
        if not self.serverWindow is None:
            try:
                self.logs.insert(END, str(text) + "\n")
                self.logs.see("end")
            except:
                pass
        
    def openServerWindow(self, bip, power, nl): 
        self.bip = bip
        self.power = power
        self.nl = nl
        
        swHei = 600
        swWid = 800
        self.serverWindow = Tk()
        self.serverWindow.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.serverWindow.title("Сервер")
        self.serverWindow.resizable(0, 0)
        self.serverWindow.iconbitmap("123.ico")
        self.serverWindow.geometry(str(swWid)+'x'+str(swHei))

        frame1 = Frame(self.serverWindow, width = 400, height = 100, bg = '#E0FFFF')
        frame2 = Frame(self.serverWindow, width = 400, height = 100, bg = '#E0FFFF')
        frame3 = Frame(self.serverWindow, width = 800, height = 100, bg = '#E0FFFF')
        frame5 = Frame(self.serverWindow, width = 800, height = 100, bg = '#E0FFFF')
        frame6 = Frame(self.serverWindow, width = 800, height = 100, bg = '#E0FFFF')
        frame4 = Frame(self.serverWindow, width = 800, height = 200, bg = '#E0FFFF')

        frame1.place(relx = 0, rely = 0, relwidth = 0.5, relheight = 0.15)
        frame2.place(relx = 0.5, rely = 0, relwidth = 0.5, relheight = 0.15)
        frame3.place(relx = 0, rely = 0.15, relwidth = 0.33, relheight = 0.1)
        frame5.place(relx = 0.33, rely = 0.15, relwidth = 0.33, relheight = 0.1)
        frame6.place(relx = 0.66, rely = 0.15, relwidth = 0.33, relheight = 0.1)
        frame4.place(relx = 0, rely = 0.25, relwidth = 1, relheight = 0.75)

        mydir = ""
        self.IP_adress = StringVar()
        self.port = StringVar()

        self.IP_adress_label = Label(frame1, text="IP адрес:", bg = '#E0FFFF')
        self.port_label = Label(frame2, text="Порт:", bg = '#E0FFFF')

        self.IP_adress_entry = Entry(frame1, textvariable=self.IP_adress)
        self.port_entry = Entry(frame2, textvariable=self.port)

        self.IP_adress_label.pack(side = LEFT, anchor="w", padx=35, pady=30)
        self.IP_adress_entry.pack(side = LEFT, anchor="w", padx=10, pady=30, ipadx = 50)
        self.IP_adress_entry.focus()

        self.port_label.pack(side = LEFT, anchor="w", padx=35, pady=30)
        self.port_entry.pack(side = LEFT, anchor="w", padx=10, pady=30, ipadx = 50)
        self.port_entry.insert(END, "8888")

        self.on_off_button = Button(frame3, text="Включить сервер", command=self.click_on_button)
        self.on_off_button.pack(side = TOP)

        self.refresh_button = Button(frame5, text="Обновить карту", command=self.refresh_map)
        self.refresh_button.pack(side = TOP)

        self.server_status_label = Label(frame6, text="Статус сервера:", bg = '#E0FFFF')
        self.server_status_label.place(relx = 0, rely = 0)

        self.canvas = Canvas(frame6, width = 100, height = 40, bg = '#E0FFFF')

        self.r = self.canvas.create_oval(10, 10, 30, 30, fill="red")
        self.y = self.canvas.create_oval(40, 10, 60, 30, fill="#708090")
        self.g = self.canvas.create_oval(70, 10, 90, 30, fill="#708090")

        self.canvas.place(relx = 0.50, rely = 0)

        self.logs = scrolledtext.ScrolledText(frame4, height=500, width=800, bg = 'black', fg='white')
        self.logs.insert(END, "")
        self.logs.see("end")
        self.logs.pack(side = BOTTOM)
        self.serverWindow.mainloop()
        #self.canvas.bind_all("", self.status)
