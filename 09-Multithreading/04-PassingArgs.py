import threading
import time

def worker(threadNumber):
    print("Thread",threadNumber)
    print("Thread {} Started".format(threading.current_thread().getName()))
    time.sleep(3)
    print("Thread {} Exit".format(threading.current_thread().getName()))

for i in range(5):
    thread = threading.Thread(target=worker, args=(i,), name="Thread_"+str(i))
    thread.start()
