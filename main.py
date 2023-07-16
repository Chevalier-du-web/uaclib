# Class principale de lancement du projet ....

# importations des dependances ...
from tkinter import *

from backend.database_structure import DataBase
from pages.authentication.login import LoginPage
from pages.home.home_page import HomePage


class MainApp:
    def __init__(self):
        # creation of database and tables
        DataBase()

        self.root = Tk()
        self.root.geometry("1250x670+50+17")
        self.root.title("UACLIB")
        self.root.resizable(height=False, width=False)
        # self.root.iconbitmap("")

        # Appel de la page home ....
        LoginPage(self.root, 1250, 670)

        # affichage de la fenetre principale...
        self.root.mainloop()


# instanciation de la classe principale ....

windows = MainApp()

print(windows)
