from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from basic_test.dbconnect_class import db_connector
from dbconnect_class2 import db_connector
from list_ticket import listticket


root=Tk()
dbconnect=db_connector()

ttk.Label(root,text='Full name:').grid(row=0,column=0,pady=10,padx=10)
EntryFullname=ttk.Entry(root,width=30,font=('Arial',10))
EntryFullname.grid(row=0,column=1,columnspan=2)
root.title('ticket system')
#style
root.configure(background='#e1d8b2')
style=ttk.Style()
style.theme_use('classic')
style.configure("TLable",background="#e1d8b2")
style.configure("TButton",background="#e1d8b2")
style.configure("TRadiobutton",background="#e1d8b2")

Spangender=StringVar()
Spangender.set('male')
ttk.Radiobutton(root,text='male',variable=Spangender,value='male').grid(row=1,column=1)
ttk.Radiobutton(root,text='female',variable=Spangender,value='female').grid(row=1 ,column=2)

ttk.Label(root,text='Gender:').grid(row=1,column=0)
Textcomment=Text(root,width=30,height=15,font=('Arial',10))
Textcomment.grid(row=2,column=1,columnspan=2)
ttk.Label(root,text='comment:').grid(row=2,column=0)
buttonss=ttk.Button(root,text='summit')
buttonss.grid(row=3,column=2)
buttonLIST=ttk.Button(root,text='LIST')
buttonLIST.grid(row=3,column=3)

def Buttonclick():
   print("fuck")
   print("Full name:{}".format(EntryFullname.get()))
   print("Gender:{}".format(Spangender.get()))
   print("Textcomment:{}".format(Textcomment.get(1.0,'end')))
   msg=dbconnect.insert(EntryFullname.get(),Spangender.get(),Textcomment.get(1.0,'end'))
   messagebox.showinfo(title='add to db',message=msg)
   EntryFullname.delete(0,'end')
   Textcomment.delete(1.0,'end')
   Spangender.set('male')
   
def ButtonLIST():
    list=listticket() 

buttonss.config(command=Buttonclick)
buttonLIST.config(command=ButtonLIST)

root.mainloop()

