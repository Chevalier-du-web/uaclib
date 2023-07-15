#importation des dependences ...
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox as mb

from backend.request_file import Request
from components.style import Style


class Forgetpassword:
    def __init__(self,root,width,height):
        self.frame = Canvas(root,width=width, height=height)

        # frame 1
        self.frame1 = Canvas(self.frame, width=width // 2, height=height, bg="lightblue")

        img = Image.open('assets/biblio.png')
        self.frame1.image = ImageTk.PhotoImage(img)
        self.frame1.create_image(0, 0, image=self.frame1.image, anchor='nw')

        Label(self.frame1, text='U A C L I B', font=('Arial', 30, 'bold'),
              bg="lightblue").place(x=200, y=400)

        Label(self.frame1, text='Regoignez toute la communaute des \nleaders de demain.\n'
                                'Cultivons-nous pour batir un monde meilleur !', font=Style.font3_b,
              bg="lightblue").place(x=40, y=460)
        self.frame1.place(x=0, y=0)

        # frame 2
        frame2 = Canvas(self.frame, width=width // 2, height=height,bg='white')
        
        heading=Label(frame2,text='You have forget your password?? dont worry ...',fg="#57a1f8",bg='white',font=('Microsoft Yahei UI Light',13,'bold'))
        heading.place(x=100,y=90)
        
        
        
        username_lbl=Label(frame2,text="Enter your username",bg="white",font=("Microsoft Yahei UI Light",13))
        username_lbl.place(x=190,y=200)
        
        self.username_entry=Entry(frame2,highlightthickness=0,relief=FLAT,bg="white",fg="black",font=("Microsoft Yahei UI Light",13))
        self.username_entry.place(x=190,y=240,width=250)
        
        username_line= Canvas(frame2,width=250,height=2.0,bg="pink",highlightthickness=0)
        username_line.place(x=190,y=270)
        
        
        Button(frame2,width=34,pady=7,text='Submit',bg='#57a1f8',fg='white',cursor='hand2',border=0,
               command=self.forget_pass).place(x=200,y=340)

        Button(frame2, width=34, pady=7, text='back', bg='teal', fg='white', cursor='hand2', border=0,
               command=self.frame.destroy).place(x=200, y=400)


        frame2.place(x=width//2, y=0)

        # affichage de de la page ...
        self.frame.place(x=0, y=0)

    def forget_pass(self):
        request = "select * from User where username=?"
        params = (self.username_entry.get(),)
        data = Request().get_request_with_params(request, params)

        if len(data) == 0 :
            mb.showwarning("Warning ", "User not founded !")
        else:
            mb.showinfo('Forget password ',f'Your password is : {data[0][5]}')