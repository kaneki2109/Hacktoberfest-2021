from tkinter import *
from tkinter import messagebox

root=Tk()
root.title('Registration Form')
root.geometry("400x300")

photo=PhotoImage(file =r"C:\Users\Dell\Pictures\dell1.png")
root.iconphoto(False, photo)


Label(root,text="REGISTRATION FORM",fg='BLACK',width=30,
      bg='orange',relief='solid',font=('Arial',15,'bold')).pack() #pack()=it is used when no place is defined for allignment

Label(root,text='App Version 1.0',fg='BLACK',relief='sunken',bg='yellow').pack(side=BOTTOM)

Label(root,text="NAME",width=15,font=('Helvetica',10,'bold')).place(x=30,y=50) #font name=helvetica

Label(root,text="EMAIL",width=15,font=('Helvetica',10,'bold')).place(x=30,y=80)

Label(root,text="ADHAAR",width=15,font=('Helvetica',10,'bold')).place(x=30,y=110)

Label(root,text="STATE",width=15,font=('Helvetica',10,'bold')).place(x=30,y=140)

var = StringVar(root)
var.set("INDIA STATE")
OptionMenu(root, var,"DELHI","RAJASTHAN","UTTARPRADESH").place(x=180,y=135)

name=StringVar()
email=StringVar()
adhaar=StringVar()


Entry(root,textvariable=name).place(x=180,y=50)
Entry(root,textvariable=email).place(x=180,y=80)
Entry(root,textvariable=adhaar).place(x=180,y=110)


def ter():
    root.destroy()

def reg():
      nm=name.get()
      em=email.get()
      adh=adhaar.get()
      st=var.get()
      print(nm,em,adh,st)

Button(root,text='Register',width=10,command=reg).place(x=80,y=190)

Button(root,text='EXIT',width=10,command=ter).place(x=180,y=190)


root.mainloop()
