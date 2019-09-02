import sqlite3

class db_connector():
    a=100156
    def __init__(self):
        self._db = sqlite3.connect('test1_class.db')
        self._db.row_factory=sqlite3.Row
        self._db.execute("CREATE TABLE if not exists Admins \
           (\
           ID INTEGER PRIMARY key autoincrement,\
           NAME           TEXT    NOT NULL,\
           AGE            int     NOT NULL\
             );")
        self._db.commit()
        self._testnum=100

    def insert(self,name,age):
       # dbss.execute("INSERT INTO   Admins  (NAME,AGE) \
       #   VALUES ( NAME, age )");
        self._db.execute("insert into Admins (Name,Age) values(?,?)",(name,age))
       # dbss.execute("insert into Admins (Name,Age) values(NAME,age)")
        self._db.commit()
    def list(self):
        cursor=self._db.execute("select * from Admins")
        for row in cursor:
            print("name {} age{}".format(row["NAME"],row["AGE"]))
    def delete(self,name):
        self._db.row_factory=sqlite3.Row
        self._db.execute("delete from Admins where NAME='{}'".format(name))
        self._db.commit()
    def update(self,name,age):
        self._db.execute("update Admins set AGE=? where NAME=?",(age,name))
        self._db.commit()
def main():

 print("database standard test")

 test_class=db_connector()
 
 
 
 test_class.insert("sheldon",30)
 test_class.insert("sdfgddon",330)
 test_class.insert("shehfrhpoon",3440)
 test_class.list()
 test_class.delete("sheldon")
 test_class.update("sdfgddon",100)


 test_class._db.close()
 print("test the number in class {}".format(test_class._testnum))
 print("a the number in class {}".format(test_class.a))





if __name__=='__main__':main()