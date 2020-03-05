import threading
from time import *
from datetime import datetime
tickets = [['2018-4-7 8:00','北京','沈阳',10,120],
           ['2018-4-7 9:00','上海','宁波',5,100],
           ['2018-4-7 12:00','天津','北京',20,55],
           ['2018-4-7 14:00','广州','武汉',0,200],
           ['2018-4-7 16:00','重庆','西安',3,180],
           ['2018-4-7 18:00','深圳','上海',49,780],
           ['2018-4-7 18:10','武汉','长沙',10,210],]   #模拟火车票在线销售信息表

def buy_ticket(name,nums,data1,start_station):
    i =0
    sleep(1)
    for get_record in tickets:
        if get_record[0] == data1 and get_record[1] == start_station:
            if get_record[3] >= nums:
                tickets[i][3]=get_record[3]-nums
                print('%s购买%d张票成功！'%(name,nums))
                return 
            else:
                print('%s余票数量不足，无法购买！'%(name))
                return -1
        i += 1
    print('%所选日期、出发站点的票无票，或已售罄，无法购买！'%(name))
    return -1

class MThread(threading.Thread):        #新增继承Thread类的子类MThread
    def __init__(self,target,args):
        threading.Thread.__init__(self)
        self.target=target
        self.args=args
    def run(self):
        self.target(*self.args)     #线程在此执行自定义函数
        
if __name__ == '__main__':
    visitor = [('张三',3,'2018-4-7 9:00','上海'),
               ('李四',3,'2018-4-7 9:00','上海'),
               ('王五',3,'2018-4-7 9:00','上海')]       #以列表形式定义抢票访问内容

    class_do_list = []                              #定义装线程对象的空列表

    print('开始时间：',datetime.now())
    for get_r in visitor:
        '''get_one = MThread(target=buy_ticket,args=get_r)
        class_do_list.append(get_one)'''
        class_do_list.append(MThread(target=buy_ticket,args=get_r))          #把线程实例装到列表里

    for i in range(len(class_do_list)):                 #循环启动线程实例
        class_do_list[i].start()
    for i in range(len(class_do_list)):                 #循环进行线程阻塞，等待线程执行结束
        class_do_list[i].join()
    
    print('结束时间：',datetime.now())
    print('剩余票数为：\n')
    for gets in tickets:
        print(gets)

        
                                                  
