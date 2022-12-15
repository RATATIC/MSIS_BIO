from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
from tkinter import scrolledtext
from clientForm import ClientForm
from serverForm import ServerForm     

def getDeviceLocationFromServer():
    #deviceX.append(xVal) добавляем в массив значение x девайса с сервера
    #deviceY.append(yVal) добавляем в массив значение y девайса с сервера
    print("Device added")

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
deviceX = [175, 300, 125, 230]
deviceY = [225, 350, 125, 230]
distances = []
legendFontSize = 8

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
circleRadius=20

for i in range(0, len(deviceX)):
    distances.insert(i, round((((deviceX[i]-yourLocationX)**2)+((deviceY[i]-yourLocationY)**2))**0.5, 1))
    canv.create_line(yourLocationX, yourLocationY, deviceX[i], deviceY[i], fill='red', width=5, dash=(10,2))

canv.create_oval(yourLocationX-circleRadius, yourLocationY-circleRadius, yourLocationX+circleRadius, yourLocationY+circleRadius, width=1, fill='red', outline='red')
canv.create_text(yourLocationX, yourLocationY, text= "You",fill="black",font=('Helvetica 15 bold'))

for i in range(0, len(deviceX)):
    canv.create_oval(deviceX[i]-circleRadius, deviceY[i]-circleRadius, deviceX[i]+circleRadius, deviceY[i]+circleRadius, width=1, fill='blue', outline='blue')
    canv.create_text(deviceX[i], deviceY[i], text= str(i+1),fill="black",font=('Helvetica 15 bold'))

canv.create_rectangle(10, 10, 120, 100, fill="white", outline="white")

if len(distances) > 9:
    legendFontSize = int(50/len(distances))

for i in range(0, len(deviceX)):
    if len(distances) < 10:
        canv.create_text(10, 10*(i+1), text="Distance to "+ str(i+1)+ "= "+str(distances[i]), anchor=NW, fill="black", font=('Helvetica bold', legendFontSize))
    else:
        canv.create_text(10, 90/len(distances)*(i+1), text="Distance to "+ str(i+1)+ "= "+str(distances[i]), anchor=NW, fill="black", font=('Helvetica bold', legendFontSize))
window.mainloop()