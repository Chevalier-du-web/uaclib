#importation des dependences ...
from tkinter import *
from tkinter import ttk
from random import randint
from PIL import ImageTk,Image
from tkinter import messagebox as mb
from backend.request_file import Request
from components.style import Style
from pages.home.home_page import HomePage


class RegisterPage:
    def __init__(self,root,width,height):
        self.width = width
        self.height = height
        self.frame = Canvas(root,width=width, height=height)

        # frame 1
        self.frame1 = Canvas(self.frame, width=width // 2, height=height, bg="lightblue")

        img = Image.open('assets/biblio.png')
        self.frame1.image = ImageTk.PhotoImage(img)
        self.frame1.create_image(0, 0, image=self.frame1.image, anchor='nw')

        Label(self.frame1, text='U A C L I B', font=('Arial', 30, 'bold'),
              bg="lightblue").place(x=200, y=400)

        Label(self.frame1, text='Regoignez toute la communaute des \nleaders de demain.\n'
                                'Cultivons-nous pour batir un monde meilleur !', font=Style.font3_b,
              bg="lightblue").place(x=40, y=460)
        self.frame1.place(x=0, y=0)

        # frame 2
        frame2 = Canvas(self.frame, width=width // 2, height=height, bg='white')

        heading = Label(frame2, text='Come and register !!', fg="#57a1f8", bg='white',
                        font=('Microsoft Yahei UI Light', 14, 'bold'))
        heading.place(x=200, y=50)

        #######username
        username_lbl = Label(frame2, text="Username", bg="white", font=("Microsoft Yahei UI Light", 11))
        username_lbl.place(x=100, y=120)

        self.username_entry = Entry(frame2, highlightthickness=0, relief=FLAT, bg="white", fg="black",
                               font=("Microsoft Yahei UI Light", 11))
        self.username_entry.place(x=210, y=120, width=250)

        username_line = Canvas(frame2, width=250, height=2.0, bg="pink", highlightthickness=0)
        username_line.place(x=210, y=142)

        #######Email
        email_lbl = Label(frame2, text="Email", bg="white", font=("Microsoft Yahei UI Light", 11))
        email_lbl.place(x=100, y=180)

        self.email_entry = Entry(frame2, highlightthickness=0, relief=FLAT, bg="white", fg="black",
                            font=("Microsoft Yahei UI Light", 11))
        self.email_entry.place(x=210, y=180, width=250)

        email_line = Canvas(frame2, width=250, height=2.0, bg="pink", highlightthickness=0)
        email_line.place(x=210, y=200)

        ######password
        password_lbl = Label(frame2, text="Password", bg="white", font=("Microsoft Yahei UI Light", 11))
        password_lbl.place(x=100, y=240)

        self.password_entry = Entry(frame2, highlightthickness=0, relief=FLAT, bg="white", fg="black",
                               font=("Microsoft Yahei UI Light", 11))
        self.password_entry.place(x=210, y=238, width=250)

        password_line = Canvas(frame2, width=250, height=2.0, bg="pink", highlightthickness=0)
        password_line.place(x=210, y=261)

        ##########level

        levels = ['Level 1', 'Level 2', 'Level 3', 'Master 1', 'Master 2', 'Doctora', 'Others']
        level_lbl = Label(frame2, text="Level", bg="white", font=("Microsoft Yahei UI Light", 11))
        self.level = ttk.Combobox(frame2, font=("Microsoft Yahei UI Light", 11), values=levels, width=28)
        self.level.current(0)
        level_lbl.place(x=100, y=295)
        self.level.place(x=210, y=293)

        level_line = Canvas(frame2, width=250, height=2.0, bg="pink", highlightthickness=0)
        level_line.place(x=210, y=318)

        #####gender
        genders = ['Male', 'Female']
        gender_lbl = Label(frame2, text="Gender", bg="white", font=("Microsoft Yahei UI Light", 11))
        self.gender = ttk.Combobox(frame2, font=("Microsoft Yahei UI Light", 11), values=genders, width=28)
        self.gender.current(0)
        gender_lbl.place(x=100, y=350)
        self.gender.place(x=210, y=350)

        level_line = Canvas(frame2, width=250, height=2.0, bg="pink", highlightthickness=0)
        level_line.place(x=210, y=374)

        ####phone
        phone_lbl = Label(frame2, text="Phone", bg="white", font=("Microsoft Yahei UI Light", 11))
        phone_lbl.place(x=100, y=400)

        self.phone_entry = Entry(frame2, highlightthickness=0, relief=FLAT, bg="white", fg="black",
                            font=("Microsoft Yahei UI Light", 11))
        self.phone_entry.place(x=210, y=400, width=250)

        phone_line = Canvas(frame2, width=250, height=2.0, bg="pink", highlightthickness=0)
        phone_line.place(x=210, y=420)
        
        ####button
        Button(frame2,width=34,pady=7,text='Register',bg='#57a1f8',fg='white',cursor='hand2',border=0,
               command=self.register).place(x=210,y=455)

        ####button
        Button(frame2, width=34, pady=7, text='Login', bg='teal', fg='white', cursor='hand2', border=0,
               command=self.frame.destroy).place(x=210, y=510)
        

        frame2.place(x=width//2, y=0)

        # affichage de de la page ...
        self.frame.place(x=0, y=0)

    def register(self):
        # HomePage(self.frame,width,height)
        # Our request here ...
        request = "INSERT INTO User(id, username, email, level, phone, password, sex) values(?,?,?,?,?,?,?)"
        id = randint(300,900)+randint(2000,9000)
        params = (id,self.username_entry.get(), self.email_entry.get(),
                  self.level.get(), self.phone_entry.get(), self.password_entry.get(),
                  self.gender.get())
        if self.username_entry.get() != '' and self.email_entry.get() != '' and self.phone_entry.get() != '' and self.phone_entry.get() != '' :
            result = Request().post_request_with_params(request,params)
            mb.showinfo("Information", "You are registed !")
            v = Request().get_request_without_params("select * from User")
            HomePage(self.frame, self.width, self.height,self.username_entry.get())
            print("database ; ",v)
            HomePage(self.frame, self.width, self.height,id,self.username_entry.get())
        else:
            mb.showwarning("Warning", "All fields are required !")
