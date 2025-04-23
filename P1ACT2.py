import threading
from threading import Thread
import time 

class restoran:
    def __init__(self, makanan, minuman):
        self.makanan = makanan
        self.minuman = minuman
    def food(self):
        print('makanan yang disajikan : {}'.format(self.makanan))
    def drink(self):
        print('minuman yang disajikan : {}'.format(self.minuman))
    def run(self):
        self.food()
        self.drink()

if __name__ == '__main__':
    start = time.perf_counter()
    makanans = [
    'sate',
    'bakso',
    'bubur',
    'ketoprak',
    'soto ayam',

]

    minumans = [
        'ice tea',
        'jus',
        'susu',
        'lemon tea',
        'wedang',
    ]

    thread_list=[]
    for makanan in makanans:
        for minuman in minumans:
            t = Thread(target=restoran(makanan,minuman).run)
            t.start()
            thread_list.append(t)
        for thread in thread_list:
            thread.join()
        finish = time.perf_counter()
        print('waktu total : ',finish-start)

