#importation des dependences ...
from tkinter import *

from PIL import ImageTk,Image

from components.style import Style
from pages.home.home_page import HomePage


class RegisterPage:
    def __init__(self,root,width,height):
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
        frame2 = Canvas(self.frame, width=width // 2, height=height,bg='white')
        
        heading=Label(frame2,text='Register',fg="#57a1f8",bg='white',font=('Microsoft Yahei UI Light',30,'bold'))
        heading.place(x=200,y=50)
        
        #######username
        username_lbl=Label(frame2,text="Your username",bg="white",font=("Microsoft Yahei UI Light",11))
        username_lbl.place(x=190,y=120)
        
        username_entry=Entry(frame2,highlightthickness=0,relief=FLAT,bg="white",fg="black",font=("Microsoft Yahei UI Light",11))
        username_entry.place(x=190,y=160,width=250)
        
        username_line= Canvas(frame2,width=250,height=2.0,bg="pink",highlightthickness=0)
        username_line.place(x=190,y=185)
        
        #######password
        password_lbl=Label(frame2,text="Your password",bg="white",font=("Microsoft Yahei UI Light",11))
        password_lbl.place(x=190,y=210)
        
        password_entry=Entry(frame2,highlightthickness=0,relief=FLAT,bg="white",fg="black",font=("Microsoft Yahei UI Light",11))
        password_entry.place(x=190,y=250,width=250)
        
        password_line= Canvas(frame2,width=250,height=2.0,bg="pink",highlightthickness=0)
        password_line.place(x=190,y=273)
        
        ##########gender
        gender_lbl=Label(frame2,text="Your gender",bg="white",font=("Microsoft Yahei UI Light",11))
        gender_lbl.place(x=190,y=300)
        
        gender_entry=Entry(frame2,highlightthickness=0,relief=FLAT,bg="white",fg="black",font=("Microsoft Yahei UI Light",11))
        gender_entry.place(x=190,y=340,width=250)
        
        gender_line= Canvas(frame2,width=250,height=2.0,bg="pink",highlightthickness=0)
        gender_line.place(x=190,y=370)
        
        #####level
        level_lbl=Label(frame2,text="Your level",bg="white",font=("Microsoft Yahei UI Light",11))
        level_lbl.place(x=190,y=400)
        
        level_entry=Entry(frame2,highlightthickness=0,relief=FLAT,bg="white",fg="black",font=("Microsoft Yahei UI Light",11))
        level_entry.place(x=190,y=440,width=250)
        
        level_line= Canvas(frame2,width=250,height=2.0,bg="pink",highlightthickness=0)
        level_line.place(x=190,y=470)
        
        ######email
        email_lbl=Label(frame2,text="Your email",bg="white",font=("Microsoft Yahei UI Light",11))
        email_lbl.place(x=190,y=500)
        
        email_entry=Entry(frame2,highlightthickness=0,relief=FLAT,bg="white",fg="black",font=("Microsoft Yahei UI Light",11))
        email_entry.place(x=190,y=540,width=250)
        
        email_line= Canvas(frame2,width=250,height=2.0,bg="pink",highlightthickness=0)
        email_line.place(x=190,y=570)
        
        ####button
        Button(frame2,width=34,pady=7,text='Register',bg='#57a1f8',fg='white',cursor='hand2',border=0,
               command=lambda:HomePage(self.frame,width,height)).place(x=200,y=600)
        
        
        
        
        
        
        
        


        frame2.place(x=width//2, y=0)

        # affichage de de la page ...
        self.frame.place(x=0, y=0)