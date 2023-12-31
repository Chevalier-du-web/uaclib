#importation des dependences ...
from tkinter import *
from components.style import Style
from PIL import ImageTk,Image
from pages.books.book_page import BooksPage
from pages.borrowing.borrowing_page import BorrowingPage
from pages.profil_user.profil_page import ProfilPage
from pages.reservations.reservation_page import ReservationPage
from pages.statistics.statistics_page import StatisticsPage
from pages.transactions.transaction_page import TransactionPage
from pages.users.users_page import UsersPage


class HomePage:
    def __init__(self,root,width,height,id,username):
        self.frame = Canvas(root,width=width, height=height)
        self.siderbar = Canvas(self.frame,height=65, width=width,bg='lightgreen')
        Label(self.siderbar,text="UACLIB APP",bg='lightgreen',font=Style.font4_i).place(x=70,y=20)
        #  welcome user ...
        Label(self.siderbar, text="Votre librairie toujours pres de vous !", bg='lightgreen', font=Style.font3_i).place(x=400, y=20)

        # USer name logged
        Label(self.siderbar, text=f"Welcome {username}", bg='lightgreen', font=Style.font4_i).place(x=900, y=20)
        #  add image ...
        img = Image.open('assets/user.png')
        self.siderbar.image = ImageTk.PhotoImage(img)
        self.siderbar.create_image(1200, 15, image=self.siderbar.image, anchor='nw')

        self.siderbar.place(x=0,y=0)

        self.menu =Canvas(self.frame,height=height-65, width=width//5,bg='grey')
        # liste des menus ...

        Label(self.menu,text="Services",font=Style.font5_b,bg='grey',fg='white').place(x=55,y=45)
        # profil page ..
        btn_profil = Button(self.menu, text="Profil",font=Style.font1_i,
                            command=lambda: ProfilPage(self.body,width-(width//5),height-65,id))
        btn_profil.place(x=6, y=120,width=width//5-8)

        # list of users ...
        btn_users = Button(self.menu, text="Users",   font=Style.font1_i, command=lambda: UsersPage(self.body,width-(width//5),height-65))
        btn_users.place(x=6, y=175, width=width // 5 - 8)

        # # list of books ...
        btn_books = Button(self.menu, text="Books", font=Style.font1_i,
                           command=lambda: BooksPage(self.body,width-(width//5),height-65))
        btn_books.place(x=6, y=230, width=width // 5 - 8)

        # # list of borrowings ...
        btn_borrowing = Button(self.menu, text="Borrowing", font=Style.font1_i,
                               command=lambda: BorrowingPage(self.body,width-(width//5),height-65))
        btn_borrowing.place(x=6, y=285, width=width // 5 - 8)

        # list of reservations ...
        btn_reservation = Button(self.menu, text="Reservation", font=Style.font1_i,
                                 command=lambda: ReservationPage(self.body,width-(width//5),height-65))
        btn_reservation.place(x=6, y=340, width=width // 5 - 8)

        # list of transactions ...
        btn_transaction = Button(self.menu, text="Transactions", font=Style.font1_i,
                                 command=lambda: TransactionPage(self.body,width-(width//5),height-65))
        btn_transaction.place(x=6, y=395, width=width // 5 - 8)

        # list of Statistics and rapports ...
        btn_statistics = Button(self.menu, text="Statistics", font=Style.font1_i,
                                command=lambda: StatisticsPage(self.body,width-(width//5),height-65))
        btn_statistics.place(x=6, y=450, width=width // 5 - 8)

        # logout button ...
        btn_statistics = Button(self.menu, text="Logout", font=Style.font1_i,
                                command=lambda: self.transition(width,height))
        btn_statistics.place(x=6, y=505, width=width // 5 - 8)

        # quit app ...
        btn_statistics = Button(self.menu, text="Exit", font=Style.font1_i, command=root.destroy)
        btn_statistics.place(x=6, y=560, width=width // 5 - 8)






        self.menu.place(x=0,y=65)

        # contenu de la page
        self.body = Canvas(root,width=width-(width//5),height=height-65,bg='lightblue')
        Label(self.body,text="Rejoignez-nous pour enrichir vos connaissances",
              bg='lightblue',font=Style.font5_b).place(x=120, y=50)
        img = Image.open('assets/onb2.PNG')
        self.body.image = ImageTk.PhotoImage(img)
        self.body.create_image(280, 20, image=self.body.image, anchor='nw')

        Label(self.body, text="Le savoir est le pouvoir, cultivons nous, lisons !!!",
              bg='lightblue', font=Style.font5_b).place(x=120, y=465)


        self.body.place(x=width//5,y=65)
        # affichage de de la page ...
        self.frame.place(x=0, y=0)
    def hello(self):
        print("hello you !")
    def transition(self,width,height):
        from pages.authentication.login import LoginPage

        self.body.destroy()
        LoginPage(self.frame, width, height)