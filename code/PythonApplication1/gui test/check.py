
from tkinter import *
from tkinter import ttk
root=Tk()
cb=ttk.Checkbutton(root,text='check test')
cb.pack()
state=StringVar()
state.set('yes')
print(state.get())

cb.config(variable=state,onvalue='very yes',offvalue='fuckoff')

print(state.get())

rbvar=StringVar()
rb1=ttk.Radiobutton(root,text='male',variable=rbvar,value='is male')
rb1.pack()




root.mainloop()