from tkinter import *

class UsersPage:
    def __init__(self,root,width,height):
        self.frame = Canvas(root,width=width, height=height,bg='lightblue')



        # affichage de de la page ...
        self.frame.place(x=0, y=0)