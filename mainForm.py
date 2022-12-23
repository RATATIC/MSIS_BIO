from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import time
import random
from tkinter import scrolledtext
from clientForm import ClientForm
from serverForm import ServerForm 
import numpy as np    

class Mainform:
    wHei = 600
    wWid = 600
    canvW = 500
    canvH = 400
    legon = False
    def __init__(self) -> None:
        self.window = Tk()
        self.window.protocol("WM_DELETE_WINDOW")
        self.window.resizable(width=False, height=False)
        self.window.title("Карта")
        self.window.iconbitmap("123.ico")
        self.window.configure(bg = '#E0FFFF')
        self.window.geometry(str(self.wWid)+'x'+str(self.wHei))
        self.pixel = PhotoImage(width=1, height=1)
        self.deviceX = []
        self.deviceY = []
        self.distances = []
        self.legendFontSize = 8
        self.target = [0, 0]
        self.scale = 1
        
        self.SF = ServerForm(self)
        self.srvBtn = Button(self.window, text="Сервер", image = self.pixel, height = 50, width = 200, compound="c", command = lambda: self.SF.openServerWindow(self.blueip.get(), int(self.power.get()), int(self.noisel.get())))
        self.srvBtn.grid(row=0, column=0, pady=20)
        
        self.legbut = Button(self.window, text="Вкл. легенду", image = self.pixel, height = 50, width = 200, compound="c", command = self.legend_on)
        self.legbut.grid(row=0, column=1, pady=20)
        
        self.CF = ClientForm(self)
        self.clnBtn = Button(self.window, text="Клиент", image = self.pixel, height = 50, width = 200, compound="c", command = lambda: self.CF.openClientWindow(self.blueip.get(), int(self.power.get()), int(self.noisel.get())))
        self.clnBtn.grid(row=0, column=2, pady=20)
        
        self.bip = StringVar()
        self.blueip = Entry(self.window, textvariable=self.bip)
        self.blueip.insert(END, "EE:97:75:4D:A0:79")
        self.blueip.grid(row=1, column=0, columnspan=1, pady=20)
        
        self.p = StringVar()
        self.power = Entry(self.window, textvariable=self.p)
        self.power.insert(END, "-43")
        self.power.grid(row=1, column=1, columnspan=1, pady=20)
        
        self.n = StringVar()
        self.noisel = Entry(self.window, textvariable=self.n)
        self.noisel.insert(END, "3")
        self.noisel.grid(row=1, column=2, columnspan=1, pady=20)
        
        

        self.canv = Canvas(self.window, width=self.canvW, height=self.canvH, bg='black')
        self.canv.grid(row=2, column=0, columnspan=3, pady=20)

        #creating coordinate grid
        for i in range(1, 8):
            self.canv.create_line(0, i*50, 600, i*50, fill="white")
            
        for i in range(0, 12):
            self.canv.create_line(i*50, 0, i*50, 400, fill="white")

        self.myLocationX = 0
        self.myLocationY = 0
        self.mydistance = 25
        self.unsc_mydistance = 0
        self.radius = 25

        for i in range(0, len(self.deviceX)):
            self.canv.create_line(self.myLocationX, self.myLocationY, self.deviceX[i], self.deviceY[i], fill='red', width=5, dash=(10,2))

        self.canv.create_oval(self.myLocationX-self.radius, self.myLocationY-self.radius, self.myLocationX+self.radius, self.myLocationY+self.radius, width=1, fill='blue', outline='blue')
        self.canv.create_text(self.myLocationX, self.myLocationY, text= "Host",fill="black",font=('Helvetica 15 bold'))
        self.canv.create_oval(self.myLocationX-self.mydistance, self.myLocationY-self.mydistance, self.myLocationX+self.mydistance, self.myLocationY+self.mydistance, width=5, outline = 'green', dash=(5,5))

        for x,y,d in zip(self.deviceX, self.deviceY, self.distances):
            self.canv.create_oval(x-self.radius, y-self.radius, x+self.radius, y+self.radius, width=1, fill='blue', outline='blue')
            self.canv.create_text(x, y, text= str(i+1),fill="black",font=('Helvetica 15 bold'))
            self.canv.create_oval(x-d, y-d, x+d, y+d, width=5, outline = 'green', dash=(5,5))

        self.window.mainloop()
        
    def legend_on(self):
        self.legbut['text'] = "Выкл. легенду"
        self.legbut['command'] = self.legend_off
        self.legon = True
        self.repaint()
        
    def legend_off(self):
        self.legbut['text'] = "Вкл. легенду"
        self.legbut['command'] = self.legend_on
        self.legon = False
        self.repaint()
        
    def setCoords(self, devices, target, mydist):
        self.deviceX = np.array([x for x, y, d in devices.values()])
        self.deviceY = np.array([y for x, y, d in devices.values()])
        self.distances = np.array([d for x, y, d in devices.values()])
        self.mydistance = mydist
        print(self.deviceX)
        print(self.deviceY)
        print(self.distances)
        maxx = max(self.deviceX)
        if maxx < 0:
            maxx = 0
        minx = min(self.deviceX)
        if minx > 0:
            minx = 0
        rangex = maxx-minx
        maxy = max(self.deviceY)
        if maxy < 0:
            maxy = 0
        miny = min(self.deviceY)
        if miny > 0:
            miny = 0
        rangey = maxy-miny
        sc = 10
        li = self.canvW/sc
        ri = self.canvW - 2*li
        ti = self.canvH/sc
        bi = self.canvH - 2*ti
        self.scale = ((ri**2+bi**2)**(0.5))/((rangex**2+rangey**2)**(0.5))
        self.distances = self.distances*self.scale
        self.mydistance = self.mydistance*self.scale
        self.deviceX = (self.deviceX - minx)/(maxx - minx) * ri + li
        self.deviceY = (self.deviceY - miny)/(maxy - miny) * bi + ti
        self.myLocationX = (- minx)/(maxx - minx) * ri + li
        self.myLocationY = (- miny)/(maxy - miny) * bi + ti
        self.radius = ((ri**2+bi**2)**(0.5))/50
        self.target = [(target[0]- minx)/(maxx - minx) * ri + li, (target[1] - miny)/(maxy - miny) * bi + ti]

    def repaint(self):
        self.canv = Canvas(self.window, width=self.canvW, height=self.canvH, bg='black')
        self.canv.grid(row=2, column=0, columnspan=3, pady=20)

        #creating coordinate grid
        for i in range(1, 8):
            self.canv.create_line(0, i*50, self.canvW, i*50, fill="white")
            
        for i in range(0, 12):
            self.canv.create_line(i*50, 0, i*50, self.canvH, fill="white")


        for i in range(0, len(self.deviceX)):
            self.canv.create_line(self.myLocationX, self.myLocationY, self.deviceX[i], self.deviceY[i], fill='red', width=5, dash=(10,2))

        self.canv.create_oval(self.target[0]-self.radius, self.target[1]-self.radius, self.target[0]+self.radius, self.target[1]+self.radius, width=1, fill='red', outline='red')
        self.canv.create_text(self.target[0], self.target[1], text= "T",fill="black",font=('Helvetica 15 bold'))

        self.canv.create_oval(self.myLocationX-self.radius, self.myLocationY-self.radius, self.myLocationX+self.radius, self.myLocationY+self.radius, width=1, fill='blue', outline='blue')
        self.canv.create_text(self.myLocationX, self.myLocationY, text= "S",fill="black",font=('Helvetica 15 bold'))
        self.canv.create_oval(self.myLocationX-self.mydistance, self.myLocationY-self.mydistance, self.myLocationX+self.mydistance, self.myLocationY+self.mydistance, width=5, outline = 'green', dash=(5,5))

        for i,(x,y,d) in enumerate(zip(self.deviceX, self.deviceY, self.distances)):
            self.canv.create_oval(x-self.radius, y-self.radius, x+self.radius, y+self.radius, width=1, fill='blue', outline='blue')
            self.canv.create_text(x, y, text= str(i+1),fill="black",font=('Helvetica 15 bold'))
            self.canv.create_oval(x-d, y-d, x+d, y+d, width=5, outline = 'green', dash=(5,5))

        if self.legon:
            self.canv.create_rectangle(10, 10, 120, 100, fill="white", outline="white")

            if len(self.distances) > 9:
                legendFontSize = int(50/(len(self.distances)+1))

            if len(self.distances) + 1 < 10:
                self.canv.create_text(10, 10, text="Dist to server = " + str(round(self.mydistance/self.scale, 2)), anchor=NW, fill="black", font=('Helvetica bold', self.legendFontSize))
            else:
                self.canv.create_text(10, 90/len(self.distances), text="Dist to server = " + str(round(self.mydistance/self.scale, 2)), anchor=NW, fill="black", font=('Helvetica bold', legendFontSize))
        
            for i, dist in enumerate(self.distances):
                if len(self.distances) + 1 < 10:
                    self.canv.create_text(10, 10*(i+2), text="Dist to "+ str(i+1)+ "= "+str(round(dist/self.scale, 2)), anchor=NW, fill="black", font=('Helvetica bold', self.legendFontSize))
                else:
                    self.canv.create_text(10, 90/len(self.distances)*(i+2), text="Dist to "+ str(i+1)+ "= "+str(round(dist/self.scale,2)), anchor=NW, fill="black", font=('Helvetica bold', legendFontSize))

if __name__ == "__main__":
    mf = Mainform()
    