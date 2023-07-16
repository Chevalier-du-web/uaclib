#importation des dependences ...
import random
from tkinter import *
from tkinter import messagebox as md, ttk
from backend.request_file import Request
from components.style import Style
from PIL import ImageTk,Image





class AddUserPage:
    def __init__(self,root,width,height):
        self.frame = Canvas(root,width=width, height=height,bg='lightblue')

        # title page
        Label(self.frame,text="Add a new user",bg='lightblue',font=Style.font6_b).place(x=380,y=60)

        #  icon for delete user
        img = Image.open('assets/adduser.png')
        self.frame.image = ImageTk.PhotoImage(img)
        self.frame.create_image(100, 55, image=self.frame.image, anchor='nw')

        # entries for user that will be deleted
        Label(self.frame,font=Style.font1_i,text='Username : ',bg='lightblue').place(x=400,y=120)
        self.username = Entry(self.frame,font=Style.font1_i)
        self.username.place(x=540,y=120)
        self.username.bind('<Return>', lambda e: self.email.focus_set())

        Label(self.frame, font=Style.font3_i, text='Email : ', bg='lightblue').place(x=400, y=160)
        self.email = Entry(self.frame, font=Style.font1_i)
        self.email.place(x=540, y=160)
        self.email.bind('<Return>', lambda e: self.level.focus_set())

        diplomes = ['Level 1', 'Level 2', 'Level 3', 'Master 1', 'Master 2', 'Doctora', 'Others']
        Label(self.frame, font=Style.font3_i, text='Level : ', bg='lightblue').place(x=400, y=200)
        self.level = ttk.Combobox(self.frame, font=Style.font1_i,values=diplomes,width=18)
        self.level.current(0)
        self.level.place(x=540, y=200)
        self.level.bind('<Return>', lambda e: self.sex.focus_set())

        Label(self.frame, font=Style.font3_i, text='Sex : ', bg='lightblue').place(x=400, y=240)
        self.sex = ttk.Combobox(self.frame, font=Style.font1_i,values=['Male', 'Female'],width=18)
        self.sex.current(0)
        self.sex.place(x=540, y=240)
        self.sex.bind('<Return>', lambda e: self.password.focus_set())

        Label(self.frame, font=Style.font3_i, text='Password : ', bg='lightblue').place(x=400, y=280)
        self.password = Entry(self.frame, font=Style.font1_i)
        self.password.place(x=540, y=280)
        self.password.bind('<Return>', lambda e: self.phone.focus_set())

        Label(self.frame, font=Style.font3_i, text='Phone : ', bg='lightblue').place(x=400, y=320)
        self.phone = Entry(self.frame, font=Style.font1_i)
        self.phone.place(x=540, y=320)

        # text for warning
        Label(self.frame,text="NB : Seuls les utilisateurs inscrits "
        "\n peuvent emprunter ou reserver un  document.",font=Style.font3_b,bg='lightblue').place(x=300,y=500)

        Button(self.frame, font=('Arial', 14, 'italic'), text='           Clear           ',
               command=self.clear_data).place(x=430, y=400)
        Button(self.frame, font=('Arial', 14, 'italic'), text='           Add user           ',
               command=lambda: self.add_user()).place(x=640, y=400)

        Button(self.frame,font=('Arial',12,'italic'),text='           back           ',
               command=self.frame.destroy).place(x=40,y=500)
        # affichage de de la page ...
        self.frame.place(x=0, y=0)

    def add_user(self):
        
        id = random.randint(200,900) + random.randint(2000,9000)
        
        #request to show user added
        request="insert into User(id,username,email,level,phone,password,sex) values(?,?,?,?,?,?,?)"
        params=(id, self.username.get(),self.email.get(),self.level.get(),self.phone.get(),self.password.get(),self.sex.get())
        if self.username.get()!='' and self.email.get()!='' and self.password.get()!='' and self.password.get()!='':
            Request().post_request_with_params(request,params)            
            md.showinfo('Information','  User added successfully !  ')
            
            self.clear_data()
        else:
            md.showwarning("Warning","All fields are required")

    def clear_data(self):
        #  clear all fields

        self.username.delete(0,END)
        self.email.delete(0, END)
        self.sex.delete(0, END)
        self.phone.delete(0, END)
        self.level.delete(0, END)
        self.password.delete(0, END)
