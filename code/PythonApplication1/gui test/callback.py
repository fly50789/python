from tkinter import *
from tkinter import ttk
import os


def BuClick(id):
    print("ID {}!!".format(10))
def key_press(event):
    print("copy type {}".format(event.type))


root=Tk()
style=ttk.Style()

print(os.path.dirname(__file__))
print(os.path.abspath(os.path.dirname(__file__)))
print( os.getcwd()  )
print(os.path.join(os.path.dirname(__file__), 'test.gif'))

### button test
#ttk.Button(root,text="click me",command=lambda :BuClick(10)).pack()
bu1=ttk.Button(root,text="clicking1")
bu1.pack()
bu2=ttk.Button(root,text="clicking2")
bu2.pack()

### image test

logo=PhotoImage(file="gui test\\test.gif")
Resize_logo=logo.subsample(10,10)
bu1.config(image=logo,compound=LEFT)
bu1.config(image=Resize_logo)

bu1.bind("<ButtonPress>",BuClick)


root.bind("z",key_press)

root.bind('<Control-c>',key_press)


print("{}".format(style.theme_names()))
print("{}".format(style.theme_use()))

style.theme_use('classic')
style.configure('TButton',foreground='red',font=('Arial',24))
style.configure('TButton',foreground='#0B6CA3',font=('Arial',99))
style.configure('Info.TButton',foreground='blue',font=('Arial',36,'bold'))
print("{}".format(bu2.configure))
print("{}".format(bu1.winfo_class()))

bu2.configure(style='Info.TButton')

style.map('Info.TButton',background=[('pressed','yellow'),('disabled','grey')])

bu2.state(['disabled'])


root.mainloop()
