#importation des dependences ...
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
from tkcalendar import DateEntry
from backend.request_file import Request
from components.style import Style


class ReturnBookPage:
    def __init__(self,root,width,height,username,books):
        self.width = width
        self.height = height
        self.username = username
        self.frame = Canvas(root,width=width, height=height,bg='lightblue')

        Label(self.frame,text=f"Return book - Page",font=Style.font4_i,bg='lightblue').place(x=50,y=20)

        Label(self.frame, font=Style.font3_i, text='Category : ', bg='lightblue').place(x=200, y=160)
        self.category = ttk.Combobox(self.frame, font=Style.font1_i,values=['Reservation','Borrowing'])
        self.category.current(0)
        self.category.place(x=340, y=160)

        Label(self.frame, font=Style.font3_i, text='Book : ', bg='lightblue').place(x=200, y=220)
        self.book = ttk.Combobox(self.frame, font=Style.font1_i, values=books)
        self.book.current(0)
        self.book.place(x=340, y=220)

        Label(self.frame, font=Style.font3_i, text='Quantity : ', bg='lightblue').place(x=200, y=280)
        self.quantity = Spinbox(self.frame, font=Style.font1_i,from_=1,to=10)
        self.quantity.place(x=340, y=280)

        Label(self.frame, font=Style.font3_i, text='End date : ', bg='lightblue').place(x=200, y=340)
        self.dateend = DateEntry(self.frame, font=Style.font1_i,width=20)
        self.dateend.place(x=340, y=320)

        Button(self.frame, font=('Arial', 12, 'italic'), text='           Return a book         ',
               command=self.return_book,bg='teal',fg='white').place(x=360, y=390)

        Button(self.frame, font=('Arial', 12, 'italic'), text='           back           ',
               command=self.frame.destroy).place(x=40, y=500)

        # affichage de de la page ...
        self.frame.place(x=0, y=0)

    def return_book(self):
        # add return
        from pages.transactions.result_transaction import ResultTransactionPage
        from random import randint

        id = randint(300, 900) + randint(2000, 9000)
        request = "insert into Returns(id,username,book,quantity,dateend) values(?,?,?,?,?)"
        params = (id,self.username, self.book.get(),self.quantity.get(),self.dateend.get_date())
        Request().post_request_with_params(request,params)

        if self.category.get() == "Reservation":
            try:
                quantity = Request().get_request_with_params('select quantity from Books where title=?', (self.book.get(),))
                Request().post_request_with_params('update Books set quantity=? where title=?',
                                                   (int(quantity[0][0]) + int(self.quantity.get()), self.book.get()))
                Request().post_request_with_params('delete from Reservation where book=?', (self.book.get(),))
                mb.showinfo('Information', 'Book returned succesfully !')
                ResultTransactionPage(self.frame,self.width,self.height,self.username)

            except:
                mb.showwarning('Warning', 'An error occured !')
        else:
            try:
                quantity = Request().get_request_with_params('select quantity from Books where title=?',
                                                             (self.book.get(),))
                Request().post_request_with_params('update Books set quantity=? where title=?',
                                                   (int(quantity[0][0]) + int(self.quantity.get()), self.book.get()))
                Request().post_request_with_params('delete from Borrowing where book=?', (self.book.get(),))
                mb.showinfo('Information', 'Book returned succesfully !')
                ResultTransactionPage(self.frame, self.width, self.height, self.username)

            except:
                mb.showwarning('Warning', 'An error occured !')