#importation des dependences ...
from tkinter import *
from tkinter import messagebox as md
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
        self.user_delete = Entry(self.frame,font=Style.font1_i)
        self.user_delete.place(x=540,y=120)

        Label(self.frame, font=Style.font3_i, text='Email : ', bg='lightblue').place(x=400, y=160)
        self.user_delete = Entry(self.frame, font=Style.font1_i)
        self.user_delete.place(x=540, y=160)

        Label(self.frame, font=Style.font3_i, text='Level : ', bg='lightblue').place(x=400, y=200)
        self.user_delete = Entry(self.frame, font=Style.font1_i)
        self.user_delete.place(x=540, y=200)

        Label(self.frame, font=Style.font3_i, text='Sex : ', bg='lightblue').place(x=400, y=240)
        self.user_delete = Entry(self.frame, font=Style.font1_i)
        self.user_delete.place(x=540, y=240)

        Label(self.frame, font=Style.font3_i, text='Password : ', bg='lightblue').place(x=400, y=280)
        self.user_delete = Entry(self.frame, font=Style.font1_i)
        self.user_delete.place(x=540, y=280)

        Label(self.frame, font=Style.font3_i, text='Phone : ', bg='lightblue').place(x=400, y=320)
        self.user_delete = Entry(self.frame, font=Style.font1_i)
        self.user_delete.place(x=540, y=320)

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
        md.showinfo('Information','  User added successfully !  ')
        self.clear_data()

    def clear_data(self):
        self.user_delete.delete(0,END)