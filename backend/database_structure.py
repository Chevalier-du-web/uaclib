# importation des dependances
import sqlite3 as sq


class DataBase:
    def __init__(self):
        self.database = sq.connect('uaclib_db.db')

        self.database.close()

    def create_user_table(self):
        self.request = """
        CREATE TABLE IF NOT EXISTS User (
	        id integer PRIMARY KEY,
	        username text NOT NULL,
	        email text NOT NULL,
	        level text NOT NULL,
	        phone text NOT NULL,
	        password text NOT NULL,
	        sex text NOT NULL,
	    );"""
        self.cursor = self.database.cursor()
        self.cursor.execute(self.request)
    def create_
