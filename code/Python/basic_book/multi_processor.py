import multiprocessing as mp
import time

def washer(dishes,output):
  for dish in dishes:
    print('washing', dish, 'dish', mp.current_process())
    output.put(dish)

def dryer(input):
  while True:
    dish = input.get()
    print('Drying', dish, 'dish', mp.current_process())
    time.sleep(5) 
    input.task_done()

def main():
    dishqueue = mp.JoinableQueue()
    dryerproc = mp.Process(target=dryer, args=(dishqueue,))
    dryerproc.daemon = True
    dryerproc.start()
    dishes = ['xxx','asa','aass']
    washer(dishes,dishqueue)
    dishqueue.join()

if __name__ == '__main__':
    main()
