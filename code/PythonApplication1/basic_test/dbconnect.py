import sqlite3
dbss = sqlite3.connect('test1.db')   
def creat_table(table_name):
    dbss.execute("CREATE TABLE if not exists Admins \
       (\
       ID INTEGER PRIMARY key autoincrement,\
       NAME           TEXT    NOT NULL,\
       AGE            int     NOT NULL\
         );")
def insert(name,age):
   # dbss.execute("INSERT INTO   Admins  (NAME,AGE) \
   #   VALUES ( NAME, age )");
    dbss.execute("insert into Admins (Name,Age) values(?,?)",(name,age))
   # dbss.execute("insert into Admins (Name,Age) values(NAME,age)")
    dbss.commit()
def list():
    cursor=dbss.execute("select * from Admins")
    for row in cursor:
        print("name {} age{}".format(row["NAME"],row["AGE"]))
def delete(name):
    dbss.row_factory=sqlite3.Row
    dbss.execute("delete from Admins where NAME='{}'".format(name))
    dbss.commit()
def update(name,age):
    dbss.execute("update Admins set AGE=? where NAME=?",(age,name))
    dbss.commit()
def main():

 print("database standard test")

 
 dbss.row_factory=sqlite3.Row
 
 creat_table("Adminnn")
 insert("sheldon",30)
 insert("sdfgddon",330)
 insert("shehfrhpoon",3440)
 list()
 delete("sheldon")
 update("sdfgddon",100)


 dbss.close()





if __name__=='__main__':main()