#importation des dependences ...
from random import randint
from tkinter import *
from tkinter import ttk
from backend.request_file import Request
from components.style import Style
import tkcalendar as tk
from tkinter import messagebox as mb


class AddBorrowingPage:
    def __init__(self,root,width,height):
        self.width = width
        self.height = height
        self.frame = Canvas(root,width=width, height=height,bg='lightblue')
        Label(self.frame,text="New borrowing - Page",font=Style.font4_i,bg='lightblue').place(x=50,y=20)

        all_users = [x[0] for x in Request().get_request_without_params("select username from User ")]
        Label(self.frame, text="Username : ", font=Style.font2_i, bg='lightblue').place(x=90, y=120)
        self.username = ttk.Combobox(self.frame, font=Style.font1_i, values=all_users, width=20)
        self.username.current(0)
        self.username.place(x=230, y=120)

        books_available = [x[0] for x in Request().get_request_without_params("select title from Books where quantity>0")]
        Label(self.frame, text="Book : ", font=Style.font2_i, bg='lightblue').place(x=90, y=160)
        self.book = ttk.Combobox(self.frame, font=Style.font1_i, values=books_available, width=20)
        self.book.current(0)
        self.book.place(x=230, y=160)

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
        Button(self.frame, font=('Arial',12,'italic'), text='           Clear           ', command=self.clear_fields).place(x=110, y=360)

        Button(self.frame,font=('Arial',12,'italic'),text='        Add new borrow        ',command=self.add_borrow,bg='teal').place(x=297,y=360)

        from pages.borrowing.borrowing_page import BorrowingPage
        Button(self.frame,font=('Arial',12,'italic'),text='           back           ',
               command=lambda: BorrowingPage(self.frame,self.width,self.height)).place(x=40,y=500)

        # affichage de de la page ...
        self.frame.place(x=0, y=0)

    def clear_fields(self):
        self.username.delete(0,END)
    def add_borrow(self):

        id = randint(300, 900) + randint(2000, 9000)
        request = "insert into Borrowing(id, username, book, quantity, datestart, dateend) values(?,?,?,?,?,?)"
        params = (id, self.username.get(), self.book.get(), self.quantity.get(), self.fromdate.get_date(),self.todate.get_date())
        if self.username.get()!='':
            # post new borrowing
            Request().post_request_with_params(request, params)

            # update quantity of book
            own_value = Request().get_request_with_params("select quantity from Books where title=?",(self.book.get(),))
            Request().post_request_with_params('update Books set quantity=? where title=?',(int(own_value[0][0])-int(self.quantity.get()),self.book.get()))
            mb.showinfo("Information", ' Borrow added succesfully !')
            self.clear_fields()
        else:
            mb.showwarning(" Warning ", "All fields are required !")