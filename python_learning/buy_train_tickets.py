from time import *                 #调用sleep()方法
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
                return nums
            else:
                print('%s余票数量不足，无法购买！'%(name))
                return -1
        i += 1
    print('%所选日期、出发站点的票无票，或已售罄，无法购买！'%(name))
    return -1

if __name__ == '__main__':    #是主程序执行后面代码
    print('开始时间：',datetime.now())
    result = buy_ticket('张三',3,'2018-4-7 9:00','上海')
    if result>0:
        print('张三购买%d张票成功！'%(3))
    result = buy_ticket('李四',1,'2018-4-7 14:00','广州')
    if result>0:
        print('李四购买%d张票成功！'%(1))
    result = buy_ticket('王五',2,'2018-4-7 9:00','上海')
    if result>0:
        print('王五购买%d张票成功！'%(2))

    print('结束时间：',datetime.now())
    print('剩余票数为：\n')
    for gets in tickets:
        print(gets)
