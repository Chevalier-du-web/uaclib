#importation des dependences ...
from tkinter import *

from PIL import ImageTk,Image


class AddUserPage:
    def __init__(self,root,width,height):
        self.frame = Canvas(root,width=width, height=height,bg='lightblue')

        img = Image.open('assets/adduser.png')
        self.frame.image = ImageTk.PhotoImage(img)
        self.frame.create_image(100, 55, image=self.frame.image, anchor='nw')
        Button(self.frame,font=('Arial',12,'italic'),text='           back           ',
               command=self.frame.destroy).place(x=40,y=500)
        # affichage de de la page ...
        self.frame.place(x=0, y=0)