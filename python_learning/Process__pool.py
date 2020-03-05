import multiprocessing
from datetime import datetime
def do1(j):
    print('进程%d'%(j))
if __name__ == '__main__':
    print('开始时间：',datetime.now())
    pool = multiprocessing.Pool()
    for i in range(10):
        pool.apply_async(do1,(i,))
    pool.close()
    pool.join()
    print('结束时间：',datetime.now())
