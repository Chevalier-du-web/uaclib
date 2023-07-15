#importation des dependences ...
from tkinter import *
from tkinter import ttk

from components.style import Style
import tkcalendar as tk
from tkinter import messagebox as mb
class AddBorrowingPage:
    def __init__(self,root,width,height):
        self.frame = Canvas(root,width=width, height=height,bg='lightblue')
        Label(self.frame,text="New borrowing - Page",font=Style.font4_i,bg='lightblue').place(x=50,y=20)

        Label(self.frame,text="Username : ",font=Style.font2_i,bg='lightblue').place(x=90,y=120)
        self.username = Entry(self.frame,font=Style.font2_i)
        self.username.place(x=230,y=120)

        books_available = ['Python code',"C# book",'Football','Play poker']
        Label(self.frame, text="Book : ", font=Style.font2_i, bg='lightblue').place(x=90, y=160)
        self.level = ttk.Combobox(self.frame, font=Style.font1_i, values=books_available, width=20)
        self.level.current(0)
        self.level.place(x=230, y=160)

        Label(self.frame, text="Quantity : ", font=Style.font2_i, bg='lightblue').place(x=90, y=200)
        self.quantity = Spinbox(self.frame, font=Style.font2_i,from_=1,to=20,width=19)
        self.quantity.place(x=230, y=200)

        Label(self.frame, text="From : ", font=Style.font2_i, bg='lightblue').place(x=90, y=240)
        self.fromdate = tk.DateEntry(self.frame, font=Style.font2_i,width=19)
        self.fromdate.place(x=230, y=240)


        Label(self.frame, text="To : ", font=Style.font2_i, bg='lightblue').place(x=90, y=280)
        self.todate = tk.DateEntry(self.frame, font=Style.font2_i,width=19)
        self.todate.place(x=230, y=280)

        #  buttons valadation
        Button(self.frame,font=('Arial',12,'italic'),text='           Clear           ',command=self.clear_filds).place(x=110,y=360)

        Button(self.frame,font=('Arial',12,'italic'),text='        Add new borrow        ',command=self.add_borrow).place(x=297,y=360)

        Button(self.frame,font=('Arial',12,'italic'),text='           back           ',command=self.frame.destroy).place(x=40,y=500)

        # affichage de de la page ...
        self.frame.place(x=0, y=0)

    def clear_filds(self):
        self.username.delete(0,END)
    def add_borrow(self):
        mb.showinfo("Information", ' Borrow added succesfully !')
        self.clear_filds()
