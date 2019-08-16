import sqlite3

class db_connector():
    a=100156
    def __init__(self):
        self._db = sqlite3.connect('ticket.db')
        self._db.row_factory=sqlite3.Row
        self._db.execute("CREATE TABLE if not exists Ticket \
           (\
           ID INTEGER PRIMARY key autoincrement,\
           NAME           TEXT    NOT NULL,\
           GENDER            TEXT     NOT NULL,\
           COMMENT            TEXT     NOT NULL\
             );")
        self._db.commit()
        

    def insert(self,name,gender,comment):
       # dbss.execute("INSERT INTO   Admins  (NAME,AGE) \
       #   VALUES ( NAME, age )");
        self._db.execute("insert into Ticket (NAME,GENDER,COMMENT) values(?,?,?)",(name,gender,comment))
       
        self._db.commit()
        return "name: {} genger :{} comment:{}".format(name,gender,comment)
    def list(self):
        cursor=self._db.execute("select * from Ticket")
        #for row in cursor:
        #    print("name {} gender {} comment {}".format(row["NAME"],row["GENDER"],row["COMMENT"]))
        return cursor

    def delete(self,name):
        self._db.row_factory=sqlite3.Row
        self._db.execute("delete from Ticket where NAME='{}'".format(name))
        self._db.commit()
    def update(self,name,age):
        self._db.execute("update Ticket set GENDER=? where NAME=?",(age,name))
        self._db.commit()
def main():

 print("database standard test")

 test_class=db_connector()
 
 test_class.insert("sheldon","male","fuckme")


 test_class._db.close()






if __name__=='__main__':main()