from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
from tkinter import scrolledtext

def click_on_off_button():
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

class ServerForm:
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

        on_off_button = Button(frame3, text="Включить сервер", command=click_on_off_button)
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
