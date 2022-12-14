from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
from tkinter import scrolledtext

#def on_closing():
#    if messagebox.askokcancel("Выход из приложения", "Хотите выйти из приложения?"):
#        serverWindow.destroy()
        
def run_Button():
    messagebox.showinfo("Статус сервера", "Сервер запущен")

def status(event):
    if event.keysym == '1':
        canvas.itemconfig(r, fill='#708090') 
        canvas.itemconfig(y, fill='#708090') 
        canvas.itemconfig(g, fill='green')
        
    elif event.keysym == '0':
        canvas.itemconfig(r, fill='red') 
        canvas.itemconfig(g, fill='#708090') 
        canvas.itemconfig(y, fill='#708090') 

    elif event.keysym == '2':
        canvas.itemconfig(r, fill='#708090') 
        canvas.itemconfig(g, fill='#708090') 
        canvas.itemconfig(y, fill='darkorange') 

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

def openServerWindow(): 
    swHei = 600
    swWid = 800
    serverWindow = Tk()
    serverWindow.protocol("WM_DELETE_WINDOW")
    serverWindow.title("Сервер")
    serverWindow.resizable(0, 0)
    serverWindow.iconbitmap("123.ico")
    serverWindow.geometry(str(swWid)+'x'+str(swHei))

    frame1 = Frame(serverWindow, width = 400, height = 100, bg = '#E0FFFF')
    frame2 = Frame(serverWindow, width = 400, height = 100, bg = '#E0FFFF')
    frame3 = Frame(serverWindow, width = 800, height = 100, bg = '#E0FFFF')
    frame4 = Frame(serverWindow, width = 800, height = 200, bg = '#E0FFFF')

    frame1.place(relx = 0, rely = 0, relwidth = 0.5, relheight = 0.15)
    frame2.place(relx = 0.5, rely = 0, relwidth = 0.5, relheight = 0.15)
    frame3.place(relx = 0, rely = 0.15, relwidth = 1, relheight = 0.20)
    frame4.place(relx = 0, rely = 0.35, relwidth = 1, relheight = 0.65)

    mydir = ""
    IP_adres = StringVar()
    port = StringVar()

    IP_adres_label = Label(frame1, text="IP адрес:", bg = '#E0FFFF')
    port_label = Label(frame2, text="Порт:", bg = '#E0FFFF')

    IP_adres_entry = Entry(frame1, textvariable=IP_adres)
    port_entry = Entry(frame2, textvariable=port)

    IP_adres_label.pack(side = LEFT, anchor="w", padx=35, pady=30)
    IP_adres_entry.pack(side = LEFT, anchor="w", padx=10, pady=30, ipadx = 50)

    port_label.pack(side = LEFT, anchor="w", padx=35, pady=30)
    port_entry.pack(side = LEFT, anchor="w", padx=10, pady=30, ipadx = 50)

    on_off_button = Button(frame3, text="Включить сервер", command=run_Button)
    on_off_button.pack(side = TOP)

    status_servera_label = Label(frame3, text="Статус сервера:", bg = '#E0FFFF')
    status_servera_label.place(relx = 0.35, rely = 0.50)

    canvas = Canvas(frame3, width = 100, height = 40, bg = '#E0FFFF')

    r = canvas.create_oval(10, 10, 30, 30, fill="red")
    y = canvas.create_oval(40, 10, 60, 30, fill="#708090")
    g = canvas.create_oval(70, 10, 90, 30, fill="#708090")

    canvas.place(relx = 0.50, rely = 0.40)

    logs = scrolledtext.ScrolledText(frame4, height=500, width=800, bg = 'black', fg='white')
    logs.insert(END, "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?Hello WorldSed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?")
    logs.see("end")
    logs.pack(side = BOTTOM)

    canvas.bind_all("", status)
    canvas.bind_all("", status)
    canvas.bind_all("", status)
        
def openClientWindow():  
    swHei = 600
    swWid = 800
    clientWindow = Toplevel(window)
    clientWindow.protocol("WM_DELETE_WINDOW")
    clientWindow.title("Клиент")
    clientWindow.resizable(0, 0)
    clientWindow.wm_attributes("-topmost", 1)
    clientWindow.iconbitmap("123.ico")
    clientWindow.geometry(str(swWid)+'x'+str(swHei))

    frame0 = Frame(clientWindow, width = 800, height = 100, bg = '#E0FFFF')
    frame1 = Frame(clientWindow, width = 400, height = 100, bg = '#E0FFFF')
    frame2 = Frame(clientWindow, width = 400, height = 100, bg = '#E0FFFF')
    frame4 = Frame(clientWindow, width = 800, height = 100, bg = '#E0FFFF')
    frame5 = Frame(clientWindow, width = 800, height = 200, bg = '#E0FFFF')
    frame6 = Frame(clientWindow, width = 800, height = 100, bg = '#E0FFFF')
    frame7 = Frame(clientWindow, width = 400, height = 100, bg = '#E0FFFF')
    frame8 = Frame(clientWindow, width = 400, height = 100, bg = '#E0FFFF')

    frame0.place(relx = 0, rely = 0, relwidth = 1, relheight = 0.055)
    frame1.place(relx = 0, rely = 0.04, relwidth = 0.5, relheight = 0.15)
    frame2.place(relx = 0.5, rely = 0.04, relwidth = 0.5, relheight = 0.15)
    frame6.place(relx = 0, rely = 0.13, relwidth = 1, relheight = 0.055)
    frame7.place(relx = 0, rely = 0.17, relwidth = 0.5, relheight = 0.15)
    frame8.place(relx = 0.5, rely = 0.17, relwidth = 0.5, relheight = 0.15)
    frame4.place(relx = 0, rely = 0.32, relwidth = 1, relheight = 0.1)
    frame5.place(relx = 0, rely = 0.38, relwidth = 1, relheight = 0.65)

    mydir = ""
    IP_adres = StringVar()
    port = StringVar()
    X = StringVar()
    Y = StringVar()

    IP_server_label = Label(frame0, text="IP адрес севера: 192.168.0.1", bg = '#E0FFFF')
    IP_adres_label = Label(frame1, text="IP адрес:", bg = '#E0FFFF')
    port_label = Label(frame2, text="Порт:", bg = '#E0FFFF')
    coordin_label = Label(frame6, text="Координаты:", bg = '#E0FFFF')
    x_label = Label(frame7, text="X:", bg = '#E0FFFF')
    y_label = Label(frame8, text="Y:", bg = '#E0FFFF')

    IP_adres_entry = Entry(frame1, textvariable=IP_adres)
    port_entry = Entry(frame2, textvariable=port)
    x_entry = Entry(frame7, textvariable=X)
    y_entry = Entry(frame8, textvariable=Y)

    IP_server_label.pack(side = LEFT, anchor="w", padx=300, pady=10)

    IP_adres_label.pack(side = LEFT, anchor="w", padx=35, pady=30)
    IP_adres_entry.pack(side = LEFT, anchor="w", padx=10, pady=30, ipadx = 50)

    port_label.pack(side = LEFT, anchor="w", padx=35, pady=30)
    port_entry.pack(side = LEFT, anchor="w", padx=10, pady=30, ipadx = 50)

    coordin_label.pack(side = LEFT, anchor="w", padx=35, pady=10)

    x_label.pack(side = LEFT, anchor="w", padx=35, pady=30)
    x_entry.pack(side = LEFT, anchor="w", padx=10, pady=30, ipadx = 50)

    y_label.pack(side = LEFT, anchor="w", padx=35, pady=30)
    y_entry.pack(side = LEFT, anchor="w", padx=10, pady=30, ipadx = 50)

    status_servera_label = Label(frame4, text="Статус подключения:", bg = '#E0FFFF')
    status_servera_label.place(relx = 0.35, rely = 0.10)

    canvas = Canvas(frame4, width = 100, height = 40, bg = '#E0FFFF')

    r = canvas.create_oval(10, 10, 30, 30, fill="#708090")
    y = canvas.create_oval(40, 10, 60, 30, fill="#708090")
    g = canvas.create_oval(70, 10, 90, 30, fill="#708090")

    canvas.place(relx = 0.50, rely = 0)
    
    logs = scrolledtext.ScrolledText(frame5, height=500, width=800, bg = 'black', fg='white')
    logs.insert(END, "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?Hello WorldSed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?")
    logs.see("end")
    logs.pack(side = BOTTOM)

srvBtn = Button(window, text="Сервер", image = pixel, height = 50, width = 200, compound="c", command = openServerWindow)
srvBtn.grid(row=0, column=0, columnspan=2, padx= 0.1*wWid, pady=20)

clnBtn = Button(window, text="Клиент", image = pixel, height = 50, width = 200, compound="c", command = openClientWindow)
clnBtn.grid(row=0, column=2, columnspan=2, padx= 0.1*wWid, pady=20)

canv = Canvas(window, width=600, height=400, bg='black')
#label_c = Label(window, text="MAP", bg="green", image = pixel, height = 0.75*wHei, width = 0.75*wWid)
#label_c.grid(row=3, column=0, rowspan=3, columnspan=4, pady=20)
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