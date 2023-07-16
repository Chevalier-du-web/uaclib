#importation des dependences ...
from tkinter import *
from tkinter import ttk

from backend.request_file import Request
from components.style import Style
from pages.borrowing.add_borrow import AddBorrowingPage
from pages.reservations.add_reservation import AddReservationPage


class ReservationPage:
    def __init__(self,root,width,height):
        self.frame = Canvas(root,width=width, height=height,bg='lightblue')
        Label(self.frame,text="Reservation - Page",font=Style.font4_i,bg='lightblue').place(x=50,y=20)
        Button(self.frame,font=('Arial',12,'italic'),text='      Add new reservation      ',
               command=lambda: AddReservationPage(self.frame,width,height),bg='teal',fg='white').place(x=700,y=120)

        # define columns
        columns = ('username', 'book', 'startdate', 'enddate','quantity')

        table = ttk.Treeview(self.frame, columns=columns, show='headings')

        # define headings
        table.heading('username', text='Username')
        table.heading('book', text='Book')
        table.heading('startdate', text='Start date')
        table.heading('enddate', text='End date')
        table.heading('quantity', text='Quantity')

        table.place(x=25, y=170,width=950)

        data = Request().get_request_without_params("select * from Reservation")
        for item in data:
            table.insert("", index=0, values=(item[1], item[2], item[-2], item[-1], item[3]))
        Button(self.frame,font=('Arial',12,'italic'),text='           back           ',command=self.frame.destroy).place(x=40,y=500)

        # affichage de de la page ...
        self.frame.place(x=0, y=0)