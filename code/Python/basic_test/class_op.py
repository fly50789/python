class op:
    def add(self,x,y):
        return x+y
    def sub(self,x,y):
        return x-y
#inherit
#override rule => root first elif use parent(super)
class multiop(op):
    def div(self,x,y):
        return x/y  
    def add(self,x,y):
        #return super().add(x,y)*100
        return 99999




def main():
    print("start") 
    mu_test=multiop()
    print("value add test {}".format(mu_test.add(3,5)))
    print("value div test {}".format(mu_test.div(3,5)))
    



if __name__=='__main__':main()