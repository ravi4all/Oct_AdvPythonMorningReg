import threading
import logging


logging.basicConfig(level=logging.DEBUG, format=('(%(threadName)-10s) %(message)s'))

class MyThread(threading.Thread):

    def run(self):
        logging.debug("Running")

for i in range(5):
    obj = MyThread()
    obj.start()