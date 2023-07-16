from tkinter import *
from PIL import ImageTk,Image
from  tkinter import  messagebox as mb
from backend.request_file import Request
from components.style import Style
from tkinter import filedialog, ttk
from random import randint



class AddBookPage:
    def __init__(self,root,width,height):
        self.width = width
        self.height = height
        self.frame = Canvas(root,width=width, height=height,bg='lightblue')
        Label(self.frame,text="Add book -page",font=Style.font4_i,bg='lightblue').place(x=50,y=20)

        #  fields for adding new book
        Label(self.frame, font=Style.font3_i, text='Title : ', bg='lightblue').place(x=70, y=120)
        self.title = Entry(self.frame, font=Style.font1_i)
        self.title.place(x=180, y=120)
        self.title.bind('<Return>', lambda e: self.author.focus_set())

        Label(self.frame, font=Style.font3_i, text='Author : ', bg='lightblue').place(x=70, y=160)
        self.author = Entry(self.frame, font=Style.font1_i)
        self.author.place(x=180, y=160)
        self.author.bind('<Return>', lambda e: self.level.focus_set())

        Label(self.frame, font=Style.font3_i, text='Subject : ', bg='lightblue').place(x=70, y=200)
        self.subject = Entry(self.frame, font=Style.font1_i)
        self.subject.place(x=180, y=200)
        self.subject.bind('<Return>', lambda e: self.level.focus_set())

        Label(self.frame, font=Style.font3_i, text='Quantity :', bg='lightblue').place(x=70, y=240)
        self.quantity = Spinbox(self.frame, font=Style.font1_i,from_=1,to=50,width=19)
        self.quantity.place(x=180, y=240)

        Button(self.frame,font=('Arial',12,'italic'),text='           Clear           ',command=self.clear_fields).place(x=100,y=350)
        Button(self.frame,font=('Arial',12,'italic'),text='           Add book           ',bg='teal',fg='white',
               command=self.add_book).place(x=270,y=350)


        from pages.books.book_page import BooksPage
        Button(self.frame,font=('Arial',12,'italic'),text='           back           '
               ,command=lambda: BooksPage(self.frame,width=self.width,height=self.height)).place(x=40,y=500)

        # affichage de de la page ...
        self.frame.place(x=0, y=0)

    def clear_fields(self):
        self.title.delete(0,END)
        self.author.delete(0, END)
        self.subject.delete(0, END)

    def add_book(self):

        id = randint(300, 900) + randint(2000, 9000)
        request = "INSERT INTO Books(id,title,subject,author,quantity) values(?,?,?,?,?) "
        params = (id,self.title.get(),self.subject.get(),self.author.get(),self.quantity.get())

        if self.title.get()!='' and self.author.get()!='' and self.subject.get()!='' :
            Request().post_request_with_params(request, params)
            mb.showinfo("Information","Book added succesfully !")
            self.clear_fields()
        else:
            mb.showwarning("Warning","All fields are required !")
