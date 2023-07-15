# importation des dependences ...
from tkinter import *
from tkinter import messagebox as mb
from PIL import ImageTk,Image

from components.style import Style
from pages.transactions.result_transaction import ResultTransactionPage


class TransactionPage:
    def __init__(self, root, width, height):
        self.width = width
        self.height = height
        self.frame = Canvas(root, width=width, height=height,bg='lightblue')

        Label(self.frame,text="Transaction - Page",font=Style.font4_i,bg='lightblue').place(x=50,y=20)
        Label(self.frame,text="Get all transactions by user",font=Style.font2_i,bg='lightblue').place(x=50,y=60)

        img = Image.open('assets/transaction.png')
        self.frame.image = ImageTk.PhotoImage(img)
        self.frame.create_image(380, 55, image=self.frame.image, anchor='nw')

        Label(self.frame, text="Username : ", font=Style.font2_i, bg='lightblue').place(x=375, y=280)
        self.username = Entry(self.frame, font=Style.font2_i)
        self.username.place(x=378, y=320)
        Button(self.frame,font=('Arial',12,'italic'),text='            Search transaction            ',
               command=self.search_user).place(x=380,y=380)

        Button(self.frame,font=('Arial',12,'italic'),text='           back           ',
               command=self.frame.destroy).place(x=40,y=500)
        # affichage de de la page ...
        self.frame.place(x=0, y=0)

    def search_user(self):
        # mb.showerror("Information", "User not founded !")
        ResultTransactionPage(self.frame,self.width,self.height)
