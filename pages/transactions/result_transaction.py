#importation des dependences ...
from tkinter import *
from tkinter import ttk

from components.style import Style
from pages.borrowing.add_borrow import AddBorrowingPage
from pages.reservations.add_reservation import AddReservationPage


class ResultTransactionPage:
    def __init__(self,root,width,height):
        self.frame = Canvas(root,width=width, height=height,bg='lightblue')
        Label(self.frame,text="Transactions of Mr Brandon - Page",font=Style.font4_i,bg='lightblue').place(x=50,y=20)

        # define columns
        columns = ('type', 'book', 'fromdate', 'todate')

        table = ttk.Treeview(self.frame, columns=columns, show='headings')

        # define headings
        table.heading('type', text='Category')
        table.heading('book', text='Book')
        table.heading('fromdate', text='Start date')
        table.heading('todate', text='End date')

        table.place(x=90, y=80)
        # more information
        Label(self.frame,text='Total of reservations  :  10',font=Style.font2_i,bg='lightblue').place(x=90,y=330)
        Label(self.frame,text='Total of borrowings  :  20',font=Style.font2_i,bg='lightblue').place(x=90,y=370)


        Button(self.frame,font=('Arial',12,'italic'),text='           back           ',command=self.frame.destroy).place(x=40,y=500)

        # affichage de de la page ...
        self.frame.place(x=0, y=0)