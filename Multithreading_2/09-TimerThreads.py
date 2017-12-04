import threading
import time
import logging

logging.basicConfig(level=logging.DEBUG, format=('(%(threadName)-10s) %(message)s'))

def delayed():
    logging.debug("Running")

# Timer starts its work after a delay, and can be canceled at any point within that delay time period.
t1 = threading.Timer(3, delayed)
t1.setName("Thread-1")

# t2 = threading.Timer(3, delayed)
# t2.setName("Thread-2")

t2 = threading.Timer(1, delayed)
t2.setName("Thread-2")

logging.debug("Starting Timers")
t1.start()
t2.start()

logging.debug("Waiting before cancellation %s"%(t2.getName()))
# time.sleep(2)
# time.sleep(5)
logging.debug("Canceling %s"%(t2.getName()))
t2.cancel()
logging.debug("Done")
