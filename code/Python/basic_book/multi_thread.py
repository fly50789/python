import threading 

def do(what):
    whoami(what)

def whoami(what):
    print("thread %s say %s" % (threading.current_thread(),what))

def main():
    whoami("main program")
    for n in range(4):
        p = threading.Thread(target=do,args=("i m function %s" % n,))
        
        p.start()

if __name__=='__main__':
   main()
