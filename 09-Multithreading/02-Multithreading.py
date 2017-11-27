import threading

def worker():
    print("Thread {} Started".format(threading.current_thread().getName()))
    for i in range(0,10000000):
        pass
    print("Thread {} Exit".format(threading.current_thread().getName()))

for i in range(5):
    thread = threading.Thread(target=worker)
    thread.start()
