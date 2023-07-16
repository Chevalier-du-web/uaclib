#importation des dependences ...
from tkinter import *
from tkinter import messagebox as md
from backend.request_file import Request
from components.style import Style
from PIL import ImageTk,Image




class DeleteUserPage:
    def __init__(self,root,width,height):
        self.width = width
        self.height = height
        self.frame = Canvas(root,width=width, height=height,bg='lightblue')

        # title page
        Label(self.frame,text="Delete a user",bg='lightblue',font=Style.font6_b).place(x=380,y=60)

        #  icon for delete user
        img = Image.open('assets/delete.png')
        self.frame.image = ImageTk.PhotoImage(img)
        self.frame.create_image(100, 55, image=self.frame.image, anchor='nw')

        # entries for user that will be deleted
        Label(self.frame,font=Style.font3_i,text='Username : ',bg='lightblue').place(x=400,y=200)
        self.user_delete = Entry(self.frame,font=Style.font3_i)
        self.user_delete.place(x=540,y=200)

        # text for warning
        Label(self.frame,text="NB : une fois qu'un client est "
        "supprimee,\n il ne pourra plus emprunter un  document.",font=Style.font3_b,bg='lightblue').place(x=300,y=450)

        Button(self.frame, font=('Arial', 14, 'italic'), text='           Clear           ',
               command=self.clear_data).place(x=430, y=300)
        Button(self.frame, font=('Arial', 14, 'italic'), text='           Delete           ',
               command=lambda: self.delete_user()).place(x=640, y=300)
        from pages.users.users_page import UsersPage

        Button(self.frame,font=('Arial',12,'italic'),text='           back           ',
               command=lambda:UsersPage(self.frame,self.width,self.height)).place(x=40,y=500)
        # affichage de de la page ...
        self.frame.place(x=0, y=0)

    def delete_user(self):
        
        
        request="delete from User where username=?"
        params=( self.user_delete.get(),)
        if self.user_delete.get()!='' :
            Request().post_request_with_params(request,params)
            md.showinfo('Information','  User delete successfully !  ')
        else:
            md.showwarning("Warning","Field is empty!!")
            
        
        self.clear_data()

    def clear_data(self):
        self.user_delete.delete(0,END)