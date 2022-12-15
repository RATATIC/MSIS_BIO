from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
from tkinter import scrolledtext
from clientForm import ClientForm
from serverForm import ServerForm     

wHei = 600
wWid = 800
window = Tk()
window.protocol("WM_DELETE_WINDOW")
window.resizable(width=False, height=False)
window.title("Карта")
window.iconbitmap("123.ico")
window.configure(bg = '#E0FFFF')
window.geometry(str(wWid)+'x'+str(wHei))
pixel = PhotoImage(width=1, height=1)

srvBtn = Button(window, text="Сервер", image = pixel, height = 50, width = 200, compound="c", command = ServerForm.openServerWindow)
srvBtn.grid(row=0, column=0, columnspan=2, padx= 0.1*wWid, pady=20)

clnBtn = Button(window, text="Клиент", image = pixel, height = 50, width = 200, compound="c", command = ClientForm.openClientWindow)
clnBtn.grid(row=0, column=2, columnspan=2, padx= 0.1*wWid, pady=20)

canv = Canvas(window, width=600, height=400, bg='black')
canv.grid(row=3, column=0, rowspan=3, columnspan=4, pady=20)

#creating coordinate grid
for i in range(1, 8):
    canv.create_line(0, i*50, 600, i*50, fill="white")
    
for i in range(0, 12):
    canv.create_line(i*50, 0, i*50, 400, fill="white")

yourLocationX=275
yourLocationY=55
deviceLocationX=175
deviceLocationY=225
circleRadius=25

distance = round((((deviceLocationX-yourLocationX)**2)+((deviceLocationY-yourLocationY)**2))**0.5, 1)

canv.create_line(yourLocationX, yourLocationY, deviceLocationX, deviceLocationY, fill='red', width=5, dash=(10,2))
canv.create_oval(yourLocationX-circleRadius, yourLocationY-circleRadius, yourLocationX+circleRadius, yourLocationY+circleRadius, width=1, fill='red', outline='red')
canv.create_text(yourLocationX, yourLocationY, text= "You",fill="black",font=('Helvetica 15 bold'))
canv.create_oval(deviceLocationX-circleRadius, deviceLocationY-circleRadius, deviceLocationX+circleRadius, deviceLocationY+circleRadius, width=1, fill='blue', outline='blue')
canv.create_text(deviceLocationX, deviceLocationY, text= "1",fill="black",font=('Helvetica 15 bold'))
canv.create_text(10, 10, text="Distance to 1 = "+str(distance), anchor=NW, fill="red", font=('Helvetica 10 bold'))

window.mainloop()