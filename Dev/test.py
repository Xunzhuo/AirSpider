import time
import grequests
import requests
import threading
from multiprocessing import Pool

url = "http://www.zuowen.com"
length = 1000


def greq(urler):
    req = [grequests.get(urler)]
    rep = grequests.map(req)
    print('ok')


def mul_gre(leng):
    divde = int(length / leng)
    req = [grequests.get(url) for x in range(divde)]
    grequests.map(req)


if __name__ == '__main__':
    # tim1 = time.time()
    # [requests.get(url) for i in range(1000)]
    # tim2 = time.time()
    # T1 = tim2 - tim1

    # tim3 = time.time()
    # [greq(url) for i in range(1000)]
    # tim4 = time.time()
    # T2 = tim4 - tim3
#异步IO
    tim5 = time.time()
    x = [grequests.get(url) for x in range(length)]
    grequests.map(x)
    tim6 = time.time()
    T3 = tim6 - tim5
#多线程异步测试
    # tim7 = time.time()
    # x1 = threading.Thread(target=mul_gre, args=(10,))
    # x2 = threading.Thread(target=mul_gre, args=(10,))
    # x3 = threading.Thread(target=mul_gre, args=(10,))
    # x4 = threading.Thread(target=mul_gre, args=(10,))
    # x5 = threading.Thread(target=mul_gre, args=(10,))
    # x6 = threading.Thread(target=mul_gre, args=(10,))
    # x7 = threading.Thread(target=mul_gre, args=(10,))
    # x8 = threading.Thread(target=mul_gre, args=(10,))
    # x9 = threading.Thread(target=mul_gre, args=(10,))
    # x10 = threading.Thread(target=mul_gre, args=(10,))
    #
    # x1.start()
    # x2.start()
    # x3.start()
    # x4.start()
    # x5.start()
    # x6.start()
    # x7.start()
    # x8.start()
    # x9.start()
    # x10.start()
    #
    # x1.join()
    # x2.join()
    # x3.join()
    # x4.join()
    # x5.join()
    # x6.join()
    # x7.join()
    # x8.join()
    # x9.join()
    # x10.join()
    # tim8 = time.time()
    # T4 = tim8 - tim7
#多进程异步IO
    tim10 = time.time()
    p = Pool(6)
    for i in range(6):
        p.apply_async(mul_gre, args=(6,))
    p.close()
    p.join()
    tim11 = time.time()
    T5 = tim11 - tim10

    # print("unformal grequests used " + str(T2))
    # print("requests used " + str(T1))
    print("formal grequests used " + str(T3))
    # print("Multi-Threading Asycio " + str(T4))
    print("Multi-Process Asycio " + str(T5))
