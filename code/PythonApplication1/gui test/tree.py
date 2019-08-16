from tkinter import *
from tkinter import ttk

root=Tk()

tv=ttk.Treeview()
tv.pack()
tv.insert('','0','item1',text='sheldon')
tv.insert('','1','item2',text='sheldon2')
tv.insert('','0','item3',text='sheldon3')
tv.move('item2','item1','0')
tv.move('item3','item1','end')
tv.insert('item1','0','item4',text='sheldon4')

tv.item('item1',open=True)
tv.detach('item4')
tv.move('item4','','end')
#tv.delete('item4')
tv.configure(column=('age'))
tv.column('age',width=160,anchor='center')
tv.column('#0',width=180,anchor='center')
tv.heading('#0',text='name')
tv.heading('age',text='AGE')

tv.set('item1','age','28')


def tvselect(event):
    print(tv.selection())
tv.bind('<<TreeviewSelect>>',tvselect)


root.mainloop()
