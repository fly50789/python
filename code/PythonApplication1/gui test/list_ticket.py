from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from dbconnect_class2 import db_connector

class listticket:
    def __init__(self):
        self._dbconnect=db_connector()
        self._root=Tk()
        tv=ttk.Treeview(self._root)
        tv.pack()
        tv.heading("#0",text="ID")
        tv.configure(column=('naMe','gendEr','commeNt'))
        #head是根據configue來跑的
        tv.heading("naMe",text="full name")
        tv.heading("gendEr",text="gender2")
        tv.heading("commeNt",text="comment3")
        cursor=self._dbconnect.list()
        for row in cursor:
           tv.insert('','end','#{}'.format(row["ID"]),text=row["ID"])
           tv.set('#{}'.format(row["ID"]),'naMe',row["NAME"])
           tv.set('#{}'.format(row["ID"]),'gendEr',row["GENDER"])
           tv.set('#{}'.format(row["ID"]),'commeNt',row["COMMENT"])
           print("ID {} name {} gender {} comment {}".format(row["ID"],row["NAME"],row["GENDER"],row["COMMENT"]))

        self._root=mainloop()

           

db=db_connector()

def main():
    print("list test")
    list=listticket()

if __name__=='__main__':main()
