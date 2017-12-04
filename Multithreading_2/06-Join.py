# Daemon Vs Non-Daemon Thread
# To wait until a daemon thread has completed its work,
# use the join() method.

import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG, format=('[%(levelname)s] (%(threadName)-9s) %(message)s'))

def daemon():
    logging.debug("Starting")
    time.sleep(5)
    for x in range(10000000):
        pass
    print("Completed Iterations...",x)
    logging.debug("Exiting")

thread_1 = threading.Thread(target=daemon, name='Daemon')
thread_1.setDaemon(True)

def non_daemon():
    logging.debug("Starting")
    time.sleep(3)
    logging.debug("Exiting")


thread_2 = threading.Thread(target=non_daemon, name="Non-Daemon")

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()

print(thread_1.isAlive())
# thread_1.join(2)
print(thread_1.isAlive())
