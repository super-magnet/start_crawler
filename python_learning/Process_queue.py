from multiprocessing import Process,Queue
q_object=Queue(5)           #创建5个元素的队列实例
def SendData(qObject,data): #发送函数，通过队列对象qObject发送data消息
    qObject.put(data)
def receiveData(qObject):   #接收函数，通过队列对象qObject接收消息
    if qObject.empty()>0:   #队列为空时，不接收消息
        print('队列信息为空！')
    else:
        show_data=qObject.get()
        print('输出%s'%(show_data))     #输出消息

if __name__=='__main__':
    send_data=[0,'Tom',10,'China']   #发送的数据
    for i in range(5):
        send_data[0] = i              #对列表第一个元素值进行修改
        p1=Process(target=SendData,args=(q_object,send_data))
        p1.start()
        p1.join()
        p2=Process(target=receiveData,args=(q_object,))
        p2.start()
        p2.join()
        
