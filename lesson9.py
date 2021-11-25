import threading
import time

class ClocclThread(threading.Thread):
    def run(self):
        for x in range(10, 0, -1):
            print(f'Time1: {x}')
            time.sleep(1)

class ClocclThread2(threading.Thread):
    def run(self):
        for x in range(10, 0, -1):
            print(f'Time2: {x}')
            time.sleep(1)

t = ClocclThread()
t2 = ClocclThread2()
t.start()
t2.start()
t.join()
t2.join()
