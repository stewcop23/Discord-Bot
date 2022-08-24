from ast import arg
from operator import is_
from threading import Thread
import time

def wait(sec):
    time.sleep(sec*60)
    print('aok')
    
args=[0.1]

wait_thread = Thread(target=wait,args=args)
wait_thread.start()
while True:
        print('done')
        time.sleep(0.5)