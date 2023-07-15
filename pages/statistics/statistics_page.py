# importation des dependences ...
from tkinter import *
from PIL import ImageTk,Image
from components.style import Style


class StatisticsPage:
    def __init__(self, root, width, height):
        self.frame = Canvas(root, width=width, height=height,bg='lightblue')
        Label(self.frame,text="Statistics - Page",font=Style.font4_i,bg='lightblue').place(x=50,y=20)

        # all informations ...
        Label(self.frame,text="All books  : 100",font=Style.font2_i,bg='lightblue').place(x=50,y=130)
        Label(self.frame,text="Books available  : 20",font=Style.font2_i,bg='lightblue').place(x=50,y=170)
        Label(self.frame,text="Books unavailable  : 80",font=Style.font2_i,bg='lightblue').place(x=50,y=210)
        Label(self.frame,text="Total of reservations  : 100",font=Style.font2_i,bg='lightblue').place(x=50,y=250)
        Label(self.frame,text="Total of borrowings  : 100",font=Style.font2_i,bg='lightblue').place(x=50,y=290)
        Label(self.frame,text="Total of users  : 100",font=Style.font2_i,bg='lightblue').place(x=50,y=330)
        Label(self.frame,text="Total of users  : 100",font=Style.font2_i,bg='lightblue').place(x=50,y=370)


        #  add image ...
        img = Image.open('assets/stat.png')
        self.frame.image = ImageTk.PhotoImage(img)
        self.frame.create_image(400, 55, image=self.frame.image, anchor='nw')


        Button(self.frame,font=('Arial',12,'italic'),text='           back           ',command=self.frame.destroy).place(x=40,y=500)

        # affichage de de la page ...
        self.frame.place(x=0, y=0)