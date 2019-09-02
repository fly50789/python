def read():
    try:
        readfile=open("test.txt","r")
        for line in readfile:
            print(line,end='')
        readfile.close()
    except IOError:   
       print("IO IS FAIL")

def write():

      out=open("test.txt","w")
      out.write("fucking camper")
      out.write("\ncheater")
      out.close()

def main():
#    read()
    write()   

if __name__=='__main__':main()


