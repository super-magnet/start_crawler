from multiprocessing import Process
from datetime import datetime
def do1(j):
    print('第%d进程！'%(j))
class MyProcess(Process):
    def __init__(self,target,args):
        Process.__init__(self)
        self.target=target
        self.args=args
    def run(self):
        self.target(*self.args)
if __name__ =='__main__':
    print('开始时间：',datetime.now())
    for i in range(10):
        p1=MyProcess(target=do1,args=(i,))
        p1.start()
        p1.join()
    print('结束时间：',datetime.now())
