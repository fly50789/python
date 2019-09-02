x=10005#global
var1 = 5   
def show():
    print(x)





def main():
    print("main function")
 #   x=10#local var
    
    #global x
    print('global x={}'.format( x ))
   # local x
    x=15
    print('global x={}'.format( x ))
 
    #global =5
   
    show()
  

if __name__=='__main__':main()


