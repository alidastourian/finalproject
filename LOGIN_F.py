import os
from tkinter import *
import SIGNUP_F
from tkinter import messagebox
from tkinter import PhotoImage


root=Tk()
root.geometry("%dx%d+%d+%d"%(800,550,100,100))
root.title("Login")
backg = PhotoImage(file = "loginb copy.png")
lbl_b=Label(root, image= backg).pack()
root.resizable(False,False)
####-----frame----------------------------------
frame=Frame(root,width=241,height=3,bg="#c4196f")
frame.place(x=500,y=165)
frame1=Frame(root,width=241,height=3,bg="#c4196f")
frame1.place(x=500,y=235)



def onsign_up(e):
    SIGNUP_F.showsignup()
    root.withdraw()

def onlogin(e):
    result=login()
    if result:
        os.system(f"python finalcrud.py")
    else:
        messagebox.showinfo("","check user and password")


def login():
    for item in SIGNUP_F.user:
        if item["user"]==txt_user.get() and item["Password"]==txt_pass.get():
            return True
    return False


##------usernameENTRY-----------------------------------------
def onenter(e):
    txt_user.delete(0,"end")

def onleave(e):
    name=txt_user.get()
    if name==(""):
        txt_user.insert(0,"UserName")

txt_user=Entry(root,width=16,border=0,bg="#00003f",fg="#fff")
txt_user.configure(font="Mj_Elit 20")
txt_user.bind("<FocusIn>",onenter)
txt_user.bind("<FocusOut>",onleave)
txt_user.insert(0,"UserName")
txt_user.place(x=500,y=130)

###------passwordENTRY-----------------------------------------
def onenter(e):
    txt_pass.delete(0,"end")

def onleave(e):
    pas=txt_pass.get()
    if pas==(""):
        txt_pass.insert(0,"Password")

txt_pass=Entry(root,width=16,border=0,bg="#00003f",fg="#fff")
txt_pass.configure(font="Mj_Elit 20")
txt_pass.bind("<FocusIn>",onenter)
txt_pass.bind("<FocusOut>",onleave)
txt_pass.insert(0,"Password")
txt_pass.place(x=500,y=200)

####-----btnlog in--------------------------------
btn_login=Button(root,text="Login",width=10,fg="#ffffff",font="arial 12 bold")
btn_login.configure(bg="#852bd4",fg="#ffffff",border=0)
btn_login.bind("<Button-1>",onlogin)
btn_login.place(x=634,y=320)
####-----btnsignup--------------------------------
btn_signupp=Button(root,text="SIGN UP",width=10,fg="#ffffff",font="arial 12 bold")
btn_signupp.configure(bg="#852bd4",fg="#ffffff",border=0)
btn_login.bind("<Button-1>",onsign_up)
btn_signupp.place(x=634,y=380)


















































root.mainloop()