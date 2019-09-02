import _thread
import time

def counter(Threadname):
    count=10
    while(count>=0):

        print("{},count:{}".format(Threadname,count))
        time.sleep(0.5)
        count-=1
def main():
    print("start")
    #counter("test")
    try:
        _thread.start_new_thread(counter,("Thread1",))
        _thread.start_new_thread(counter,("Thread2",))
        print("thread is start")
    except:
        print("unable start thread")
    while 1:
        pass



if __name__=='__main__':main()