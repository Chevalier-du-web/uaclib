#importation des dependences ...
from tkinter import *

class BorrowingPage:
    def __init__(self,root,width,height):
        self.frame = Canvas(root,width=width, height=height)

        # affichage de de la page ...
        self.frame.place(x=0, y=0)