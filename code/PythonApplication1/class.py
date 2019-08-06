class user:
    def __init__(self,username):
        print("constructor test {}".format(username))
        self._UserName=username
    def setusername(self,username):
        self._UserName=username
    def getusername(self):
        return self._UserName
class car:
    def settype(self,type):
        self._Type=type
    def gettype(self):
        return self._Type

    def setprice(self,price):
        self._Price=price
    def getprice(self):
        return self._Price

     

def main():
    print("start") 
    u1=user("gprjepg")
    #u1.setusername("sheldon")
    print(u1.getusername())
    mycar=car()
    mycar.setprice(500)
    print("car value {}".format(mycar.getprice()))


if __name__=='__main__':main()