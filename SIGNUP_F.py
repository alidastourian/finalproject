import os
from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage

user=[]

def showsignup():

        root = Tk()
        root.geometry("%dx%d+%d+%d" % (800, 550, 100, 100))
        root.title("SIGNUP")
        image = PhotoImage(file="signupb.png")
        lbl_bs=Label(root, image=image).pack()
        root.resizable(False, False)
        ####-----frame----------------------------------
        frame = Frame(root, width=241, height=3, bg="#c4196f")
        frame.place(x=500, y=165)
        frame1 = Frame(root, width=241, height=3, bg="#c4196f")
        frame1.place(x=500, y=225)
        frame2 = Frame(root, width=241, height=3, bg="#c4196f")
        frame2.place(x=500, y=285)
        frame3 = Frame(root, width=241, height=3, bg="#c4196f")
        frame3.place(x=500, y=347)

        def sign_up(e):
            b=False
            for item in user:
                if item["user"]==txt_user.get():
                    messagebox.showinfo("","unvalid")
                    b=True
                    break
            if b==False:
                if txt_pass.get()==txt_confirmpass.get():
                    dic={"user":txt_user.get(),"Password":txt_pass.get(),"Gmail":txt_gmail.get()}
                    user.append(dic)
                    print(user)
                else:
                    messagebox.showwarning("","fill all fildes")
        #def on_login(e):
            #if txt_user.get()==("") and txt_pass.get()==("") and txt_confirmpass.get()==("") and txt_gmail.get()==(""):
                #messagebox.showerror("","fill all fildes")
                #os.system(f"python LOGIN_F.py")


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
        ###------emailENTRY-----------------------------------------
        def onenter(e):
            txt_gmail.delete(0,"end")

        def onleave(e):
            gmaill=txt_gmail.get()
            if gmaill==(""):
                txt_gmail.insert(0,"Gmail")

        txt_gmail=Entry(root,width=16,border=0,bg="#00003f",fg="#fff")
        txt_gmail.configure(font="Mj_Elit 20")
        txt_gmail.bind("<FocusIn>",onenter)
        txt_gmail.bind("<FocusOut>",onleave)
        txt_gmail.insert(0,"Gmail")
        txt_gmail.place(x=500,y=190)

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
        txt_pass.place(x=500,y=250)

        ###------conpasswordENTRY-----------------------------------------
        def onenter(e):
            txt_confirmpass.delete(0,"end")

        def onleave(e):
            conpas=txt_confirmpass.get()
            if conpas==(""):
                txt_confirmpass.insert(0,"ConfirmPassword")

        txt_confirmpass=Entry(root,width=16,border=0,bg="#00003f",fg="#fff")
        txt_confirmpass.configure(font="Mj_Elit 20")
        txt_confirmpass.bind("<FocusIn>",onenter)
        txt_confirmpass.bind("<FocusOut>",onleave)
        txt_confirmpass.insert(0,"ConfirmPassword")
        txt_confirmpass.place(x=500,y=312)
        ####-----btnsignup--------------------------------
        btn_signupp=Button(root,text="SIGN UP",width=10,fg="#ffffff",font="arial 12 bold")
        btn_signupp.configure(bg="#852bd4",fg="#ffffff",border=0)
        btn_signupp.bind("<Button-1>",sign_up)
        btn_signupp.place(x=635,y=370)
        ####-----btnlog in--------------------------------
        #btn_login = Button(root, text="Login", width=10, fg="#ffffff", font="arial 12 bold")
        #btn_login.configure(bg="#852bd4", fg="#ffffff", border=0)
        #btn_login.bind("<Button-1>", on_login)
        #btn_login.place(x=210, y=390)









        root.mainloop()
showsignup()