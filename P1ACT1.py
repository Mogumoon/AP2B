import threading
import time

class myThread:
    def number(self):
        for i in range(1,21):
            print("the number is :", i)
            time.sleep(1)
    def double(self):
        for i in range(1,21):
            print("the double number is :", 2*i)
            time.sleep(1)
    def square(self):
        for i in range(1,21):
            print("the square number is :", i*i)
            time.sleep(1)

if __name__ == '__main__':
    start = time.perf_counter()
    obj=myThread()
    thread1 = threading.Thread(target=obj.number)
    thread2 = threading.Thread(target=obj.double)
    thread3 = threading.Thread(target=obj.square)

    thread1.start()
    time.sleep(0.2)
    thread2.start()
    time.sleep(0.2)
    thread3.start()
    time.sleep(0.2)


    thread1.join()
    thread2.join()
    thread3.join()

    finsih = time.perf_counter()
    print('waktu yang dibutuhkan : ',  finsih-start)
