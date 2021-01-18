
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from PIL import ImageTk,Image
root=Tk()

class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("LOGIN SYSTEM")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False,False)
        #self.bg=ImageTk.PhotoImage(file="D:\\shreya\\authenticated login mlh\\login system.png")
        #self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        Frame_login=Frame(self.root)
        Frame_login.place(x=350,y=100,height=340,width=500)
        title=Label(Frame_login,text="Login Here", font=("Impact",35,"bold")).place(x=160,y=20)
        desc=Label(Frame_login,text="Accountant Employee Login Area",font=("Gouddy old style",15,"bold")).place(x=110,y=100)
        lbl_user=Label(Frame_login,text="Username",font=("Gouddy old style",15,"bold")).place(x=90,y=140)
        self.txt_user=Entry(Frame_login,font=("times new roman",15))
        self.txt_user.place(x=90,y=170,width=350,height=35)
        
        lbl_user=Label(Frame_login,text="Password",font=("Gouddy old style",15,"bold")).place(x=90,y=210)
        self.txt_pass=Entry(Frame_login,font=("times new roman",15))
        self.txt_pass.place(x=90,y=240,width=350,height=35)
        
        forget_btn=Button(Frame_login,text="Forgot Password?",cursor="hand2").place(x=90,y=280)
        Login_btn=Button(self.root,command=self.login_function,cursor="hand2",text="Login").place(x=510,y=420,width=180,height=40)
        
    def login_function(self):
        if self.txt_pass.get()=="" or self.txt_user.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.txt_pass.get()!="123456" or self.txt_user.get()!="Shreya":
            messagebox.showerror("Error","Incorrect username/password",parent=self.root)
        else:
            messagebox.showinfo("Welcome",f"Welcome {self.txt_user.get()}\nYour password is :{self.txt_pass.get()}",parent=self.root)
            

obj=Login(root)
root.mainloop()






