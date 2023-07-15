# importation des dependances
import sqlite3 as sq


class DataBase:
    # creation of tables an database ....
    def __init__(self):
        self.database = sq.connect('uaclib_db.db')

        # creation of tables
        self.create_book_table()
        self.create_borrowing_table()
        self.create_reservation_table
        self.create_user_table()

        # self.database.close()

    def create_user_table(self):
        self.request = """
        CREATE TABLE IF NOT EXISTS User (
	        id integer PRIMARY KEY,
	        username text NOT NULL,
	        email text NOT NULL,
	        level text NOT NULL,
	        phone text NOT NULL,
	        password text NOT NULL,
	        sex text NOT NULL
	    );"""
        self.cursor = self.database.cursor()
        self.cursor.execute(self.request)
    def create_book_table(self):
        self.request = """
                CREATE TABLE IF NOT EXISTS Books (
        	        id integer PRIMARY KEY,
        	        title text NOT NULL,
        	        subject text NOT NULL,
        	        author text NOT NULL,
        	        quantity integer NOT NULL
        	    );"""
        self.cursor = self.database.cursor()
        self.cursor.execute(self.request)

    def create_borrowing_table(self):
        self.request = """
                CREATE TABLE IF NOT EXISTS Borrowing (
        	        id integer PRIMARY KEY,
        	        username text NOT NULL,
        	        book text NOT NULL,
        	        quantity integer NOT NULL,
        	        datestart text NOT NULL,
        	        dateend text NOT NULL
        	    );"""
        self.cursor = self.database.cursor()
        self.cursor.execute(self.request)

    def create_reservation_table(self):
        self.request = """
                CREATE TABLE IF NOT EXISTS Reservation (
        	        id integer PRIMARY KEY,
        	        username text NOT NULL,
        	        book text NOT NULL,
        	        quantity integer NOT NULL,
        	        datestart text NOT NULL,
        	        dateend text NOT NULL
        	    );"""
        self.cursor = self.database.cursor()
        self.cursor.execute(self.request)

