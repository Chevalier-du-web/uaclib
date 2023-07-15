#importation des dependences ...
from tkinter import *
from tkinter import ttk


class RegisterPage:
    def __init__(self,root,width,height):
        self.frame = Canvas(root,width=width, height=height)

        # frame 1
        frame1 = Canvas(self.frame,width=width//2, height=height,bg="pink")
        
        


        frame1.place(x=0,y=0)

        # frame 2
        frame2 = Canvas(self.frame, width=width // 2, height=height,bg='white')
        
        heading=Label(frame2,text='Come and register !!',fg="#57a1f8",bg='white',font=('Microsoft Yahei UI Light',14,'bold'))
        heading.place(x=200,y=50)
        
        #######username
        username_lbl=Label(frame2,text="Username",bg="white",font=("Microsoft Yahei UI Light",11))
        username_lbl.place(x=100,y=120)
        
        username_entry=Entry(frame2,highlightthickness=0,relief=FLAT,bg="white",fg="black",font=("Microsoft Yahei UI Light",11))
        username_entry.place(x=210,y=120,width=250)
        
        username_line= Canvas(frame2,width=250,height=2.0,bg="pink",highlightthickness=0)
        username_line.place(x=210,y=142)
        
        #######Email
        email_lbl=Label(frame2,text="Email",bg="white",font=("Microsoft Yahei UI Light",11))
        email_lbl.place(x=100,y=180)
        
        email_entry=Entry(frame2,highlightthickness=0,relief=FLAT,bg="white",fg="black",font=("Microsoft Yahei UI Light",11))
        email_entry.place(x=210,y=180,width=250)
        
        email_line= Canvas(frame2,width=250,height=2.0,bg="pink",highlightthickness=0)
        email_line.place(x=210,y=200)
        
        ######password
        password_lbl=Label(frame2,text="Password",bg="white",font=("Microsoft Yahei UI Light",11))
        password_lbl.place(x=100,y=240)
        
        password_entry=Entry(frame2,highlightthickness=0,relief=FLAT,bg="white",fg="black",font=("Microsoft Yahei UI Light",11))
        password_entry.place(x=210,y=238,width=250)
        
        password_line= Canvas(frame2,width=250,height=2.0,bg="pink",highlightthickness=0)
        password_line.place(x=210,y=261)
        
        ##########level
        
        levels = ['Level 1', 'Level 2', 'Level 3', 'Master 1', 'Master 2', 'Doctora', 'Others']
        level_lbl=Label(frame2,text="Level",bg="white",font=("Microsoft Yahei UI Light",11))
        level = ttk.Combobox(frame2, font=("Microsoft Yahei UI Light",11),values=levels,width=28)
        level_lbl.place(x=100,y=295)
        level.place(x=210,y=293)
        
        level_line= Canvas(frame2,width=250,height=2.0,bg="pink",highlightthickness=0)
        level_line.place(x=210,y=318)
        
        #####gender
        genders = ['Male', 'Female']
        gender_lbl=Label(frame2,text="Gender",bg="white",font=("Microsoft Yahei UI Light",11))
        gender = ttk.Combobox(frame2, font=("Microsoft Yahei UI Light",11),values=genders,width=28)
        gender_lbl.place(x=100,y=350)
        gender.place(x=210,y=350)
        
        level_line= Canvas(frame2,width=250,height=2.0,bg="pink",highlightthickness=0)
        level_line.place(x=210,y=374)
        
        
        ####phone
        phone_lbl=Label(frame2,text="Phone",bg="white",font=("Microsoft Yahei UI Light",11))
        phone_lbl.place(x=100,y=400)
        
        phone_entry=Entry(frame2,highlightthickness=0,relief=FLAT,bg="white",fg="black",font=("Microsoft Yahei UI Light",11))
        phone_entry.place(x=210,y=400,width=250)
        
        phone_line= Canvas(frame2,width=250,height=2.0,bg="pink",highlightthickness=0)
        phone_line.place(x=210,y=420)
        
        ####button
        Button(frame2,width=30,pady=7,text='Register',bg='#57a1f8',fg='white',cursor='hand2',border=0).place(x=200,y=500)
        
        
        
        
        
        
        
        


        frame2.place(x=width//2, y=0)

        # affichage de de la page ...
        self.frame.place(x=0, y=0)