import threading

def worker_1():
    for i in range(0,100000000):
        pass
    print("Worker_1 Called...")

def worker_2():
    print("Worker_2 Called")

# worker_1()
# worker_2()

thread_1 = threading.Thread(target=worker_1)
thread_1.start()

thread_2 = threading.Thread(target=worker_2)
thread_2.start()
