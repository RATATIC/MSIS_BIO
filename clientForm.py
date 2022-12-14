from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
from tkinter import scrolledtext

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

class ClientForm:
    def openClientWindow():  
        swHei = 600
        swWid = 800
        clientWindow = Tk()
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