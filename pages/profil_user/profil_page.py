from tkinter import *
from PIL import ImageTk,Image

from backend.request_file import Request
from components.style import Style
from tkinter import filedialog, ttk


class ProfilPage:
    def __init__(self,root,width,height, username):
        self.frame = Canvas(root,height=height, width=width,bg='lightblue')
        #  getting data ...
        request = "select * from User where username=?"
        params = (username,)
        data = Request().get_request_with_params(request,params)
        print(data)


        #  page -title
        Label(self.frame,text=f"Profil-Page       ID : {data[0][0]}",font=Style.font4_i,bg='lightblue').place(x=50,y=20)

        self.frame_info = Canvas(self.frame,width=550,height=450,bg='teal')

        # infos for current user...
        Label(self.frame_info,text=f"Username :  {data[0][1]}",font=Style.font3_i,bg='teal',fg='white').place(x=60,y=50)
        Label(self.frame_info,text=f"Email :  {data[0][2]}",font=Style.font3_i,bg='teal',fg='white').place(x=60,y=100)
        Label(self.frame_info,text=f"password :  {data[0][5]}",font=Style.font3_i,bg='teal',fg='white').place(x=60,y=150)
        Label(self.frame_info,text=f"Level :  {data[0][3]}",font=Style.font3_i,bg='teal',fg='white').place(x=60,y=200)
        Label(self.frame_info,text=f"Sex :  {data[0][-1]}",font=Style.font3_i,bg='teal',fg='white').place(x=60,y=250)
        Label(self.frame_info,text=f"Phone :  {data[0][4]}",font=Style.font3_i,bg='teal',fg='white').place(x=60,y=300)


        Button(self.frame_info,text="       back       ",font=Style.font2_b,command=self.frame.destroy).place(x=60,y=350)
        Button(self.frame_info,text="    edit profil    ",font=Style.font2_b,command=self.edit_user).place(x=340,y=350)



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

    def edit_user(self):
        self.frame_edit = Canvas(self.frame, width=550, height=450, bg='teal')

        # infos for current user...
        Label(self.frame_edit, text=f"Username :  ", font=Style.font3_i, bg='teal', fg='white').place(x=60,y=50)
        self.username = Entry(self.frame_edit,font=Style.font2_i)
        self.username.place(x=200,y=50)

        Label(self.frame_edit, text=f"Email :  ", font=Style.font3_i, bg='teal', fg='white').place(x=60,y=100)
        self.email = Entry(self.frame_edit, font=Style.font2_i)
        self.email.place(x=200, y=100)

        Label(self.frame_edit, text=f"password :  ", font=Style.font3_i, bg='teal', fg='white').place(x=60,y=150)
        self.password = Entry(self.frame_edit, font=Style.font2_i)
        self.password.place(x=200, y=150)

        diplomes = ['Level 1', 'Level 2', 'Level 3', 'Master 1', 'Master 2', 'Doctora', 'Others']
        Label(self.frame_edit, font=Style.font3_i, text='Level : ', bg='teal').place(x=60, y=200)
        self.level = ttk.Combobox(self.frame_edit, font=Style.font1_i, values=diplomes, width=20)
        self.level.current(0)
        self.level.place(x=200, y=200)

        Label(self.frame_edit, text=f"Sex :  ", font=Style.font3_i, bg='teal', fg='white').place(x=60,y=250)
        self.sex = ttk.Combobox(self.frame_edit, font=Style.font1_i, values=['Male', 'Female'], width=20)
        self.sex.current(0)
        self.sex.place(x=200, y=250)

        Label(self.frame_edit, text=f"Phone :  ", font=Style.font3_i, bg='teal', fg='white').place(x=60,y=300)
        self.phone = Entry(self.frame_edit, font=Style.font2_i)
        self.phone.place(x=200, y=300)

        Button(self.frame_edit, text="       back       ", font=Style.font2_b, command=self.frame.destroy).place(x=60,y=350)
        Button(self.frame_edit, text="    Save profil    ", font=Style.font2_b,command=self.save_profil).place(x=340, y=350)

        self.frame_edit.place(x=40, y=80)

    def save_profil(self):
        request = ""

