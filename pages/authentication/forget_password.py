#importation des dependences ...
from tkinter import *

class Forgetpassword:
    def __init__(self,root,width,height):
        self.frame = Canvas(root,width=width, height=height)

        # frame 1
        frame1 = Canvas(self.frame,width=width//2, height=height,bg='pink')


        frame1.place(x=0,y=0)

        # frame 2
        frame2 = Canvas(self.frame, width=width // 2, height=height,bg='white')
        
        heading=Label(frame2,text='You have forget your password?? dont worry ...',fg="#57a1f8",bg='white',font=('Microsoft Yahei UI Light',13,'bold'))
        heading.place(x=100,y=90)
        
        
        
        username_lbl=Label(frame2,text="Enter your username",bg="white",font=("Microsoft Yahei UI Light",13))
        username_lbl.place(x=190,y=200)
        
        username_entry=Entry(frame2,highlightthickness=0,relief=FLAT,bg="white",fg="black",font=("Microsoft Yahei UI Light",13))
        username_entry.place(x=190,y=240,width=250)
        
        username_line= Canvas(frame2,width=250,height=2.0,bg="pink",highlightthickness=0)
        username_line.place(x=190,y=270)
        
        
        Button(frame2,width=30,pady=7,text='Submit',bg='#57a1f8',fg='white',cursor='hand2',border=0).place(x=200,y=420)


        frame2.place(x=width//2, y=0)

        # affichage de de la page ...
        self.frame.place(x=0, y=0)