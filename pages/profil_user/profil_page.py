from tkinter import *

from components.style import Style


class ProfilPage:
    def __init__(self,root,width,height):
        self.frame = Canvas(root,height=height, width=width,bg='lightblue')
        Label(self.frame,text="Profil-Page",font=Style.font4_i,bg='lightblue').place(x=50,y=20)
        self.frame_info = Canvas(self.frame,width=550,height=450,bg='red')

        self.frame_info.place(x=40,y=80)

        self.frame_img = Canvas(self.frame, width=350, height=450, bg='green')

        self.frame_img.place(x=620, y=80)
        self.frame.place(x=0,y=0)