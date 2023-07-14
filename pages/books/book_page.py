from tkinter import *
from tkinter import ttk

from components.style import Style


class BooksPage:
    def __init__(self,root,width,height):
        self.frame = Canvas(root,width=width, height=height,bg='lightblue')
        Label(self.frame,text="Book -page",font=Style.font4_i,bg='lightblue').place(x=50,y=20)

        # itemsSearch
        items_earch = ['Title','Author','Subject']
        Label(self.frame,text="Search by",font=Style.font3_i,bg='lightblue').place(x=200,y=100)
        listCombo = ttk.Combobox(self.frame, values=items_earch,font=Style.font2_i,width=10)
        listCombo.current(0)
        listCombo.place(x=320,y=100)
        search_item = Entry(self.frame,font=Style.font2_i)
        search_item.place(x=480,y=100)
        Button(self.frame,font=('Arial',12,'italic'),text='           Search           ').place(x=740,y=100)

        # define columns
        columns = ('title', 'author', 'subject', 'quantity')

        table = ttk.Treeview(self.frame, columns=columns, show='headings')

        # define headings
        table.heading('title', text='Title')
        table.heading('author', text='Author')
        table.heading('subject', text='Subject')
        table.heading('quantity', text='Quantity')

        table.place(x=90, y=150)

        Button(self.frame,font=('Arial',12,'italic'),text='           back           ',command=self.frame.destroy).place(x=40,y=500)


        # affichage de de la page ...
        self.frame.place(x=0, y=0)