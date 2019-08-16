
from tkinter import *
from tkinter import ttk
root=Tk()

frame=ttk.Frame(root)
frame.pack()
frame.config(height=200,width=200)
frame.config(relief=RIDGE)
ttk.Button(frame,text='click frame1').grid(row=0,column=0)
ttk.Button(frame,text='click2 frame1').grid(row=0,column=3)

frame2=ttk.Frame(root)
frame2.pack()
frame2.config(height=200,width=200,relief=RIDGE,padding=(50,50))

ttk.Button(frame2,text='click frame2').pack()
ttk.Button(frame2,text='click2 frame2').pack()

ttk.LabelFrame(height=100,width=100,text='third frame').pack()

root.mainloop()