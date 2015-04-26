__author__ = 'extradikke'
import multiprocessing
from multiprocessing import Queue, Process, Value
import time


def producer_func(q, state):
    while state.value:
        q.put([55, 86, 0])
        print(state)
        time.sleep(1)


def consumer_func(q, state):
    while state.value:
        q.get()
        print(q.qsize(), q)
        if q.qsize() > 1:
            state.value = False
        time.sleep(2)


if __name__ == '__main__':
    q = Queue()
    stater = Value('b', True)
    # stater = True
    producer = Process(target=producer_func, args=(q, stater,))
    consumer = Process(target=consumer_func, args=(q, stater, ))
    producer.start()
    consumer.start()
    producer.join()
    consumer.join()



