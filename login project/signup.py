from tkinter import *
from PIL import ImageTk

signup_window=Tk()
signup_window.title('Signup Page')
signup_window.resizable(False,False)
background=ImageTk.PhotoImage(file='bg.jpg')

bgLabel=Label(signup_window,image=background)
bgLabel.grid()

frame=Frame(signup_window,bg='white')
frame.place(x=554,y=100)

heading=Label(frame,text='CREATE AN ACCOUNT',font=('Microsoft Yahei Ui Light',18,'bold'),bg='white',fg='firebrick1')
heading.grid(row=0,column=0,padx=10,pady=10)

emailLabel=Label(frame,text='Email',font=('Microsoft Yahei Ui Light',10,'bold'),bg='white',fg='firebrick1')
emailLabel.grid(row=1,column=0,sticky='w',padx=25,pady=(10,0))

emailEntry=Entry(frame,width=25,font=('Microsoft Yahei Ui Light',10,'bold'),fg='white',bg='firebrick1')
emailEntry.grid(row=2,column=0,sticky='w',padx=25)

usernameLabel=Label(frame,text='Username',font=('Microsoft Yahei Ui Light',10,'bold'),bg='white',fg='firebrick1')
usernameLabel.grid(row=3,column=0,sticky='w',padx=25,pady=(10,0))

usernameEntry=Entry(frame,width=25,font=('Microsoft Yahei Ui Light',10,'bold'),fg='white',bg='firebrick1')
usernameEntry.grid(row=4,column=0,sticky='w',padx=25)

passwordLabel=Label(frame,text='Password',font=('Microsoft Yahei Ui Light',10,'bold'),bg='white',fg='firebrick1')
passwordLabel.grid(row=5,column=0,sticky='w',padx=25,pady=(10,0))

passwordEntry=Entry(frame,width=25,font=('Microsoft Yahei Ui Light',10,'bold'),fg='white',bg='firebrick1')
passwordEntry.grid(row=6,column=0,sticky='w',padx=25)

confirmpasswordLabel=Label(frame,text='Confirm Password',font=('Microsoft Yahei Ui Light',10,'bold'),bg='white',fg='firebrick1')
confirmpasswordLabel.grid(row=7,column=0,sticky='w',padx=25,pady=(10,0))

confirmpasswordEntry=Entry(frame,width=25,font=('Microsoft Yahei Ui Light',10,'bold'),fg='white',bg='firebrick1')
confirmpasswordEntry.grid(row=8,column=0,sticky='w',padx=25)

terms=Checkbutton(frame,text='I agree to the Terms and Conditions',font=('Microsoft Yahei Ui Light',10,'bold'))
terms.grid(row=9,column=0)


signup_window.mainloop()
