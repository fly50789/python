from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from random import randint
#global var
ActivePlayer1=1
p1=[]
p2=[]


root=Tk()
root.title("Tic Tac:PLay 1")
style=ttk.Style()
style.theme_use('classic')
bu1=ttk.Button(root,text='')
bu1.grid(row=0,column=0,sticky='snew',ipadx=40,ipady=40)
bu1.config(command=lambda: ButtonClick(1))

bu2=ttk.Button(root,text='')
bu2.grid(row=0,column=1,sticky='snew',ipadx=40,ipady=40)
bu2.config(command=lambda: ButtonClick(2))

bu3=ttk.Button(root,text='')
bu3.grid(row=0,column=2,sticky='snew',ipadx=40,ipady=40)
bu3.config(command=lambda: ButtonClick(3))


bu4=ttk.Button(root,text='')
bu4.grid(row=1,column=0,sticky='snew',ipadx=40,ipady=40)
bu4.config(command=lambda: ButtonClick(4))

bu5=ttk.Button(root,text='')
bu5.grid(row=1,column=1,sticky='snew',ipadx=40,ipady=40)
bu5.config(command=lambda: ButtonClick(5))

bu6=ttk.Button(root,text='')
bu6.grid(row=1,column=2,sticky='snew',ipadx=40,ipady=40)
bu6.config(command=lambda: ButtonClick(6))

bu7=ttk.Button(root,text='')
bu7.grid(row=2,column=0,sticky='snew',ipadx=40,ipady=40)
bu7.config(command=lambda: ButtonClick(7))

bu8=ttk.Button(root,text='')
bu8.grid(row=2,column=1,sticky='snew',ipadx=40,ipady=40)
bu8.config(command=lambda: ButtonClick(8))

bu9=ttk.Button(root,text='')
bu9.grid(row=2,column=2,sticky='snew',ipadx=40,ipady=40)
bu9.config(command=lambda: ButtonClick(9))






def ButtonClick(id):
    print("ID:{}".format(id))
    global ActivePlayer1
    global p1
    global p2

    if (ActivePlayer1==1):
       SetLayout(id,"x")
       p1.append(id)
       root.title("player2")
       ActivePlayer1=2
       print("p1:{}".format(p1))
       autoplay()
    else:
       SetLayout(id,"0")
       p2.append(id)
       root.title("player1")
       ActivePlayer1=1
       print("p2:{}".format(p2))
    checkwinner()

def SetLayout(id,symbol):
    if id==1:
        bu1.config(text=symbol)
        bu1.state(['disabled'])
    elif id==2:
        bu2.config(text=symbol)
        bu2.state(['disabled'])
    elif id==3:
        bu3.config(text=symbol)
        bu3.state(['disabled'])
    elif id==4:
        bu4.config(text=symbol)
        bu4.state(['disabled'])
    elif id==5:
        bu5.config(text=symbol)
        bu5.state(['disabled'])
    elif id==6:
        bu6.config(text=symbol)
        bu6.state(['disabled'])
    elif id==7:
        bu7.config(text=symbol)
        bu7.state(['disabled'])
    elif id==8:
        bu8.config(text=symbol)
        bu8.state(['disabled'])
    elif id==9:
        bu9.config(text=symbol)
        bu9.state(['disabled'])
    
def checkwinner():
    winner=-1
    if((1 in p1) and (2 in p1) and (3 in p1)):
        winner=1
    if((4 in p1) and (5 in p1) and (6 in p1)):
        winner=1
    if((7 in p1) and (8 in p1) and (9 in p1)):
        winner=1
    if((1 in p1) and (4 in p1) and (7 in p1)):
        winner=1
    if((2 in p1) and (5 in p1) and (8 in p1)):
        winner=1
    if((3 in p1) and (6 in p1) and (9 in p1)):
        winner=1
    if((1 in p1) and (5 in p1) and (9 in p1)):
        winner=1
    if((3 in p1) and (5 in p1) and (7 in p1)):
        winner=1
    if((1 in p2) and (2 in p2) and (3 in p2)):
        winner=2
    if((4 in p2) and (5 in p2) and (6 in p2)):
        winner=2
    if((7 in p2) and (8 in p2) and (9 in p2)):
        winner=2
    if((1 in p2) and (4 in p2) and (7 in p2)):
        winner=2
    if((2 in p2) and (5 in p2) and (8 in p2)):
        winner=2
    if((3 in p2) and (6 in p2) and (9 in p2)):
        winner=2
    if((1 in p2) and (5 in p2) and (9 in p2)):
        winner=2
    if((3 in p2) and (5 in p2) and (7 in p2)):
        winner=2
        
    if(winner>0):
        messagebox.showinfo(title="congratulation",message="play{} is winner".format(winner) )
def autoplay():
    global p1
    global p2
    Empty=[]
    for cell in range(9):
        if(not(cell+1 in p1 or cell+1 in p2)):
            Empty.append(cell+1)
    randindex=randint(0,len(Empty)-1)       
    ButtonClick(Empty[randindex])


root.mainloop()

