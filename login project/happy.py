from tkinter import *
from PIL import ImageTk
#functionality
def on_enter(event):
    if usernameEntry.get()=='Username':
        usernameEntry.delete(0,END)
def user_enter(event):
    if passwordEntry.get()=='Password':
        passwordEntry.delete(0,END)
#gui part
login_window=Tk()
login_window.geometry('990x660+50+50')
login_window.resizable(0,0)
login_window.title('Login page')
bgImage=ImageTk.PhotoImage(file='bg.jpg')
bgLabel=Label(login_window,image=bgImage)
bgLabel.place(x=0,y=0)
heading=Label(login_window,text="USER LOGIN",font=('Microsoft Yahei Ui Light',23,'bold'),bg='white',fg='firebrick1')
heading.place(x=605,y=120)
usernameEntry=Entry(login_window,width=25,font=('Microsoft Yahei Ui Light',11,'bold'),bd=0,fg='firebrick1')
usernameEntry.place(x=605,y=200)
usernameEntry.insert(0,'Username')
usernameEntry.bind('<FocusIn>',on_enter)
frame1=Frame(login_window,width=250,height=2,bg='firebrick1').place(x=600,y=222)
passwordEntry=Entry(login_window,width=25,font=('Microsoft Yahei Ui Light',11,'bold'),bd=0,fg='firebrick1')
passwordEntry.place(x=605,y=255)
passwordEntry.insert(0,'Password')
passwordEntry.bind('<FocusIn>',user_enter)
frame2=Frame(login_window,width=250,height=2,bg='firebrick1')
frame2.place(x=600,y=282)
login_window.mainloop()
