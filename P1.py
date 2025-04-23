import threading
from threading import Thread
import time

#Kasus Olah 1000 Data
class olahData:
    def __init__(self, rentang):
        self.rentang = rentang
    def readData(self):
        print("[1] Read data ke : {}".format(self.rentang))
    def sortData(self):
        print("[2] Read data ke : {}".format(self.rentang))
    def exportData(self):
        print("[3] Read data ke : {}".format(self.rentang))
        time.sleep(1)
    def run(self):
        self.readData()
        self.sortData()
        self.exportData()

if __name__ == '__main__':
    start = time.perf_counter()
    rentangs = [
        '1-100000',
        '100001-200000',
        '200001-300000',
        '300001-400000',
        '400001-500000',
        '500001-600000',
        '600001-700000',
        '700001-800000',
        '800001-900000',
        '900001-1000000',
    ]
Thread_list=[]
for rentang in rentangs :
    t = Thread(target=olahData(rentang).run)
    t.start()
    time.sleep(0.1)
    Thread_list.append(t)
for thread in Thread_list:
    thread.join()
finish = time.perf_counter()
print('waktu total : ', finish-start)
