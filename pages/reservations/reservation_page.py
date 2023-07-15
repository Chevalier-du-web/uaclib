#importation des dependences ...
from tkinter import *
from tkinter import ttk

from components.style import Style
from pages.borrowing.add_borrow import AddBorrowingPage
from pages.reservations.add_reservation import AddReservationPage


class ReservationPage:
    def __init__(self,root,width,height):
        self.frame = Canvas(root,width=width, height=height,bg='lightblue')
        Label(self.frame,text="Reservation - Page",font=Style.font4_i,bg='lightblue').place(x=50,y=20)
        Button(self.frame,font=('Arial',12,'italic'),text='      Add new reservation      ',
               command=lambda: AddReservationPage(self.frame,width,height)).place(x=678,y=120)

        # define columns
        columns = ('id', 'username', 'email', 'level')

        table = ttk.Treeview(self.frame, columns=columns, show='headings')

        # define headings
        table.heading('id', text='Username')
        table.heading('username', text='Book')
        table.heading('email', text='Start date')
        table.heading('level', text='End date')

        table.place(x=90, y=170)

        Button(self.frame,font=('Arial',12,'italic'),text='           back           ',command=self.frame.destroy).place(x=40,y=500)

        # affichage de de la page ...
        self.frame.place(x=0, y=0)