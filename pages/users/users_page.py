from tkinter import *
from tkinter import ttk
from backend.request_file import Request
from components.style import Style
from pages.users.add_user import AddUserPage
from pages.users.delete_user import DeleteUserPage


class UsersPage:
    def __init__(self,root,width,height):
        self.frame = Canvas(root,width=width, height=height,bg='lightblue')
        Label(self.frame,text="All users",font=Style.font4_i,bg='lightblue').place(x=50,y=20)

        Button(self.frame,font=('Arial',12,'italic'),text='           Add new user           ',
               command=lambda:AddUserPage(self.frame,width=width,height=height)).place(x=90,y=120)
        Button(self.frame, font=('Arial', 12, 'italic'), text='           Delete user           ',
               command=lambda:DeleteUserPage(self.frame,width=width,height=height)).place(x=310, y=120)

        # define columns
        columns = ('id','username', 'email', 'level')

        table = ttk.Treeview(self.frame, columns=columns, show='headings')

        # define headings
        table.heading('id', text='ID')
        table.heading('username', text='Username')
        table.heading('email', text='Email')
        table.heading('level', text='Level')

        table.place(x=90,y=170)

        Button(self.frame,font=('Arial',12,'italic'),text='           back           ',command=self.frame.destroy).place(x=40,y=500)
        
        #request to show all the users
        request="select * from User"
        data=Request().get_request_without_params(request)
        print(f"datas {data}")
        for item in data :
               table.insert('',index=0,values=(item[0], item[1], item[2], item[3]))
       
        # affichage de de la page ...
        self.frame.place(x=0, y=0)