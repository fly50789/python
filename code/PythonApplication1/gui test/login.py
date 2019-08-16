
from tkinter import  *
from tkinter import ttk
from tkinter import messagebox

root=Tk()
root.title("login page")
root.resizable(False,False)
l1=ttk.Label(root,text='name')
l1.grid(row=0,column=0)

etusername=ttk.Entry(root,width=30)
etusername.grid(row=0,column=1)
l2=ttk.Label(root,text='password')
l2.grid(row=1,column=0)
etpass=ttk.Entry(root,width=30)
etpass.grid(row=1,column=1)
etpass.config(show='*')

Bulogin=ttk.Button(root,text='login')
Bulogin.grid(row=2,column=1)

def Buclick():
    print("name {} pass {}".format(etusername.get(),etpass.get()))
    if 1 and 1:
        messagebox.showinfo(title="login",message="login name{} pass{}".format(etusername.get(),etpass.get()))
Bulogin.config(command=Buclick)

root.mainloop()