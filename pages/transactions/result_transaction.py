#importation des dependences ...
from tkinter import *
from tkinter import ttk

from backend.request_file import Request
from components.style import Style
from pages.borrowing.add_borrow import AddBorrowingPage
from pages.reservations.add_reservation import AddReservationPage
from pages.return_book.return_book import ReturnBookPage


class ResultTransactionPage:
    def __init__(self,root,width,height,username):
        self.frame = Canvas(root,width=width, height=height,bg='lightblue')
        Label(self.frame,text=f"Transactions of Student {username} - Page",font=Style.font4_i,bg='lightblue').place(x=50,y=20)

        # define columns
        columns = ('type', 'book', 'fromdate', 'todate')

        table = ttk.Treeview(self.frame, columns=columns, show='headings')

        # define headings
        table.heading('type', text='Category')
        table.heading('book', text='Book')
        table.heading('fromdate', text='Start date')
        table.heading('todate', text='End date')

        table.place(x=90, y=80)
        data = Request().get_request_with_params('select * from Borrowing where username=?',(username,))
        data2 = Request().get_request_with_params('select * from Reservation where username=?', (username,))
        books = []
        if len(data) !=0 :
            for item in data:
                books.append(item[2])
                table.insert('',index=0, values=("Borrowing",item[2],item[-2], item[-1]))

        if len(data2) != 0:
            for item in data2:
                books.append(item[2])
                table.insert('',index=0, values=("Reservation",item[2],item[-2], item[-1]))

        Button(self.frame,font=('Arial',12,'italic'),text='           Return book           ',
               command=lambda : ReturnBookPage(self.frame,width,height,username,books),bg='teal',fg='white').place(x=700,y=340)

        # more information
        Label(self.frame,text=f'Total of reservations  :  {len(data2)}',font=Style.font2_i,bg='lightblue').place(x=90,y=330)
        Label(self.frame,text=f'Total of borrowings  :  {len(data)}',font=Style.font2_i,bg='lightblue').place(x=90,y=370)
        Label(self.frame,text=f'Total of returns  :  {len(data)}',font=Style.font2_i,bg='lightblue').place(x=90,y=410)



        Button(self.frame,font=('Arial',12,'italic'),text='           back           ',command=self.frame.destroy).place(x=40,y=500)

        # affichage de de la page ...
        self.frame.place(x=0, y=0)
