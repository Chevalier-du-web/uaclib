#importation des dependences ...
from tkinter import *

class RegisterPage:
    def __init__(self,root,width,height):
        self.frame = Canvas(root,width=width, height=height)

        # frame 1
        frame1 = Canvas(self.frame,width=width//2, height=height,bg='purple')


        frame1.place(x=0,y=0)

        # frame 2
        frame2 = Canvas(self.frame, width=width // 2, height=height,bg='red')


        frame2.place(x=width//2, y=0)

        # affichage de de la page ...
        self.frame.place(x=0, y=0)