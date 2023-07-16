import sqlite3 as sq
from tkinter import messagebox as mb
from backend.database_structure import DataBase

class Request:
    def __init__(self):
        self.database = sq.connect('uaclib_db.db')
        self.cursor = self.database.cursor()

    # post request methode
    def post_request_with_params(self,request,params):
        try:
            self.cursor.execute(request, params)
            self.database.commit()
        except :
            raise mb.showerror(" Warning", "A error occured !")
        # save changes
        return 0

    def post_request_without_params(self,request):

        try:
            self.cursor.execute(request)
            self.database.commit()
        except:
            raise mb.showerror(" Warning", "A error occured !")
        # save changes
        return 0

    # get request methode
    def get_request_with_params(self,request,params):
        try:
            self.cursor.execute(request, params)
            result = self.cursor.fetchall()

            # return result of request
            return result
        except:
            raise mb.showerror(" Warning", "A error occured !")


    def get_request_without_params(self,request):
        try:
            self.cursor.execute(request)
            result = self.cursor.fetchall()

            # return result of request
            return result
        except:
            raise mb.showerror(" Warning", "A error occured !")





