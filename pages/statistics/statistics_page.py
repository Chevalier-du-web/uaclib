# importation des dependences ...
from tkinter import *
from PIL import ImageTk,Image

from backend.request_file import Request
from components.style import Style


class StatisticsPage:
    def __init__(self, root, width, height):
        self.frame = Canvas(root, width=width, height=height,bg='lightblue')
        Label(self.frame,text="Statistics - Page",font=Style.font4_i,bg='lightblue').place(x=50,y=20)

        # requests
        all_books = Request().get_request_without_params('select * from Books')
        all_users = Request().get_request_without_params('select * from User')
        all_borrowings = Request().get_request_without_params('select * from Borrowing')
        all_reservations = Request().get_request_without_params('select * from Reservation')
        all_books_available = Request().get_request_without_params('select * from Books where quantity>0')
        all_returns = Request().get_request_without_params('select * from Returns')



        # all books quantities
        total_books = 0
        for item in all_books:
            total_books += item[-1]



        # all informations ...
        Label(self.frame,text=f"All books  : {len(all_books)}",font=Style.font2_i,bg='lightblue').place(x=50,y=130)
        Label(self.frame,text=f"Books available  : {len(all_books_available)}",font=Style.font2_i,bg='lightblue').place(x=50,y=170)
        Label(self.frame,text=f"Books unavailable  : {len(all_books)-len(all_books_available)}",font=Style.font2_i,bg='lightblue').place(x=50,y=210)
        Label(self.frame,text=f"Total of reservations  : {len(all_reservations)}",font=Style.font2_i,bg='lightblue').place(x=50,y=250)
        Label(self.frame,text=f"Total of borrowings  : {len(all_borrowings)}",font=Style.font2_i,bg='lightblue').place(x=50,y=290)
        Label(self.frame,text=f"Total of users  : {len(all_users)}",font=Style.font2_i,bg='lightblue').place(x=50,y=330)
        Label(self.frame,text=f"Total of quantities books  : {total_books}",font=Style.font2_i,bg='lightblue').place(x=50,y=370)
        Label(self.frame,text=f"Total of returns  : {len(all_returns)}",font=Style.font2_i,bg='lightblue').place(x=50,y=410)


        #  add image ...
        img = Image.open('assets/stat.png')
        self.frame.image = ImageTk.PhotoImage(img)
        self.frame.create_image(400, 55, image=self.frame.image, anchor='nw')


        Button(self.frame,font=('Arial',12,'italic'),text='           back           ',command=self.frame.destroy).place(x=40,y=500)

        # affichage de de la page ...
        self.frame.place(x=0, y=0)