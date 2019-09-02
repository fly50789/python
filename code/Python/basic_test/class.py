class user:
    def __init__(self,username):
        print("constructor test {}".format(username))
        self._UserName=username
    def setusername(self,username):
        self._UserName=username
    def getusername(self):
        return self._UserName

### old class
class car:
    def __init__(self,**kwargs):
        self._Data=kwargs
    def settype(self,type):
        self._Type=type
    def gettype(self):
        return self._Type

    def setprice(self,price):
        self._Price=price
    def getprice(self):
        return self._Price
####     

#kwargs example
class car:
    def __init__(self,**kwargs):
        self._Data=kwargs   
    def gettype(self):
        return self._Data["type"]  
    def getprice(self):
        return self._Data["price"]  



def main():
    print("start") 
    u1=user("gprjepg")
    #u1.setusername("sheldon")
    print(u1.getusername())
    mycar=car(type="BMW",price=50000)
    

    print("car value {}".format(mycar.getprice()))


if __name__=='__main__':main()