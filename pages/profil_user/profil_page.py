from tkinter import *
from PIL import ImageTk,Image
from components.style import Style
from tkinter import filedialog


class ProfilPage:
    def __init__(self,root,width,height):
        self.frame = Canvas(root,height=height, width=width,bg='lightblue')
        #  page -title
        Label(self.frame,text="Profil-Page",font=Style.font4_i,bg='lightblue').place(x=50,y=20)

        self.frame_info = Canvas(self.frame,width=550,height=450,bg='teal')

        # infos for current user...
        Label(self.frame_info,text="Username :  Sangon Brandon",font=Style.font3_i,bg='teal',fg='white').place(x=30,y=50)
        Label(self.frame_info,text="Email :  brandon@gmail.com",font=Style.font3_i,bg='teal',fg='white').place(x=30,y=100)
        Label(self.frame_info,text="password :  Brandon123",font=Style.font3_i,bg='teal',fg='white').place(x=30,y=150)
        Label(self.frame_info,text="Level :  2",font=Style.font3_i,bg='teal',fg='white').place(x=30,y=200)
        Label(self.frame_info,text="Sex :  Male",font=Style.font3_i,bg='teal',fg='white').place(x=30,y=250)

        Button(self.frame_info,text="       back       ",font=Style.font2_b,command=self.frame.destroy).place(x=60,y=350)
        Button(self.frame_info,text="    edit profil    ",font=Style.font2_b).place(x=340,y=350)



        self.frame_info.place(x=40,y=80)


        self.frame_img = Canvas(self.frame, width=350, height=450, bg='grey')
        self.photo = 'assets/logo.png'
        img = Image.open(self.photo)
        self.frame_img.image = ImageTk.PhotoImage(img)
        self.frame_img.create_image(100, 55, image=self.frame_img.image, anchor='nw')
        Button(self.frame_img,text="    add a new image    ",font=Style.font2_b, command=self.openfile).place(x=60,y=300)

        self.frame_img.place(x=620, y=80)
        self.frame.place(x=0,y=0)
    def openfile(self):
        file = filedialog.askopenfilename()
        self.photo = str(file)
