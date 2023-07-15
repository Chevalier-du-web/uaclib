#importation des dependences ...
from tkinter import *
from PIL import ImageTk, Image

from components.style import Style
from pages.home.home_page import HomePage


class LoginPage:
    def __init__(self,root,width,height):
        self.frame = Canvas(root,width=width, height=height)

        # frame 1
        self.frame1 = Canvas(self.frame,width=width//2, height=height,bg="lightblue")

        img = Image.open('assets/biblio.png')
        self.frame1.image = ImageTk.PhotoImage(img)
        self.frame1.create_image(0, 0, image=self.frame1.image, anchor='nw')

        Label(self.frame1, text='U A C L I B', font=('Arial',30,'bold'),
              bg="lightblue").place(x=200, y=400)

        Label(self.frame1,text='Regoignez toute la communaute des \nleaders de demain.\n'
                               'Cultivons-nous pour batir un monde meilleur !',font=Style.font3_b,bg="lightblue").place(x=40,y=460)
        self.frame1.place(x=0,y=0)

        # frame 2
        frame2 = Canvas(self.frame, width=width // 2, height=height,bg='white')
        
        heading=Label(frame2,text='Login',fg="#57a1f8",bg='white',font=('Microsoft Yahei UI Light',30,'bold'))
        heading.place(x=250,y=90)
        
        
        username_lbl=Label(frame2,text="Username",bg="white",font=("Microsoft Yahei UI Light",13))
        username_lbl.place(x=190,y=200)
        
        self.username_entry=Entry(frame2,highlightthickness=0,relief=FLAT,bg="white",fg="black",font=("Microsoft Yahei UI Light",13))
        self.username_entry.place(x=190,y=240,width=250)
        self.username_entry.bind('<Return>',lambda e: self.password_entry.focus_set())
        # self.email.bind('<Return>', lambda e: self.level.focus_set())

        username_line= Canvas(frame2,width=250,height=2.0,bg="pink",highlightthickness=0)
        username_line.place(x=190,y=270)
        
        ## password
        password_lbl=Label(frame2,text="Password",bg="white",font=("Microsoft Yahei UI Light",13))
        password_lbl.place(x=190,y=300)
        
        self.password_entry=Entry(frame2,highlightthickness=0,relief=FLAT,bg="white",fg="black",font=("Microsoft Yahei UI Light",13,"bold"))
        self.password_entry.place(x=190,y=340,width=250)

        
        password_line= Canvas(frame2,width=250,height=2.0,bg="pink",highlightthickness=0)
        password_line.place(x=190,y=370)
        
        from pages.authentication.forget_password import Forgetpassword

        Button(frame2,text='i have forget my password',fg='blue',bg='white',border=0,
               font=('Microsoft Yahei UI Light',9),cursor='hand2',command=lambda:Forgetpassword(self.frame,width,height)).place(x=190,y=380)

        


        Button(frame2,width=34,pady=7,text='Login',bg='#57a1f8',fg='white',cursor='hand2',
               border=0,command=lambda:HomePage(self.frame,width,height)).place(x=200,y=420)
        
        from pages.authentication.register import RegisterPage 
        
        Button(frame2,width=34,pady=7,text='Register',bg='teal',fg='white',cursor='hand2',
               command=lambda:RegisterPage(self.frame,width,height),border=0).place(x=200,y=480)

        frame2.place(x=width//2, y=0)

        # affichage de de la page ...
        self.frame.place(x=0, y=0)