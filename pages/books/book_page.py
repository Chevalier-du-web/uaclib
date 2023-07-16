from tkinter import *
from tkinter import ttk

from backend.request_file import Request
from components.style import Style
from pages.books.add_book import AddBookPage


class BooksPage:
    def __init__(self,root,width,height):
        self.frame = Canvas(root,width=width, height=height,bg='lightblue')
        Label(self.frame,text="Book -page",font=Style.font4_i,bg='lightblue').place(x=50,y=20)

        # itemsSearch
        items_earch = ['All','Title','Author','Subject']
        Label(self.frame,text="Search by",font=Style.font3_i,bg='lightblue').place(x=200,y=100)
        self.listCombo = ttk.Combobox(self.frame, values=items_earch,font=Style.font2_i,width=10)
        self.listCombo.current(0)
        self.listCombo.place(x=320,y=100)
        self.search_item = Entry(self.frame,font=Style.font2_i)
        self.search_item.place(x=480,y=100)
        Button(self.frame,font=('Arial',12,'italic'),text='           Search           ',command=self.search_book).place(x=740,y=100)

        # define columns
        columns = ('title', 'author', 'subject', 'quantity')

        table = ttk.Treeview(self.frame, columns=columns, show='headings')

        # define headings
        table.heading('title', text='Title')
        table.heading('author', text='Author')
        table.heading('subject', text='Subject')
        table.heading('quantity', text='Quantity')

        table.place(x=90, y=150)
        #  insert data from table ..
        data = Request().get_request_without_params("select * from Books")
        for item in data:
            table.insert("",index=0,values=(item[1], item[3], item[2], item[-1]))

        Button(self.frame,font=('Arial',12,'italic'),text='           Add new book           ',bg='teal',fg='white',
               command=lambda: AddBookPage(self.frame,width,height)).place(x=695,y=390)


        # affichage de de la page ...
        self.frame.place(x=0, y=0)

    def search_book(self):
        # define columns
        columns = ('title', 'author', 'subject', 'quantity')

        table = ttk.Treeview(self.frame, columns=columns, show='headings')

        # define headings
        table.heading('title', text='Title')
        table.heading('author', text='Author')
        table.heading('subject', text='Subject')
        table.heading('quantity', text='Quantity')

        table.place(x=90, y=150)

        #  insert filter data from table ...
        match self.listCombo.get() :
            case "All":
                data = Request().get_request_without_params("select * from Books")
            case "Title":
                data = Request().get_request_with_params("select * from Books where title=? ", (self.search_item.get(),))
            case "Author" :
                data = Request().get_request_with_params("select * from Books where author=? ", (self.search_item.get(),))
            case _:
                data = Request().get_request_with_params("select * from Books where subject=? ", (self.search_item.get(),))

        for item in data:
            table.insert("", index=0, values=(item[1], item[3], item[2], item[-1]))
