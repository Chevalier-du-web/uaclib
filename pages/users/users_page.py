from tkinter import *
from tkinter import ttk
from components.style import Style


class UsersPage:
    def __init__(self,root,width,height):
        self.frame = Canvas(root,width=width, height=height,bg='lightblue')
        Label(self.frame,text="All users",font=Style.font4_i,bg='lightblue').place(x=50,y=20)

        # define columns
        columns = ('id','username', 'email', 'level')

        table = ttk.Treeview(self.frame, columns=columns, show='headings')

        # define headings
        table.heading('id', text='ID')
        table.heading('username', text='Username')
        table.heading('email', text='Email')
        table.heading('level', text='Level')

        table.place(x=90,y=170)


        # affichage de de la page ...
        self.frame.place(x=0, y=0)