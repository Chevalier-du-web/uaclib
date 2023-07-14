from tkinter import *
from tkinter import ttk

from components.style import Style


class BooksPage:
    def __init__(self,root,width,height):
        self.frame = Canvas(root,width=width, height=height,bg='lightblue')
        Label(self.frame,text="Book -page",font=Style.font4_i,bg='lightblue').place(x=50,y=20)

        # define columns
        columns = ('title', 'author', 'subject', 'quantity')

        table = ttk.Treeview(self.frame, columns=columns, show='headings')

        # define headings
        table.heading('title', text='Title')
        table.heading('author', text='Author')
        table.heading('subject', text='Subject')
        table.heading('quantity', text='Quantity')

        table.place(x=90, y=150)

        # affichage de de la page ...
        self.frame.place(x=0, y=0)