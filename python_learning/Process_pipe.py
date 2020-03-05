from multiprocessing import Process,Pipe
def do_send(conn_s,j):                                            #自定义发送消息函数
    print('为啥打印不出来？\n')
    conn_s.send({'发送序号':j,'鲫鱼':[18,10.5],'鲤鱼':[8,6.2]})   #send发送一条字典
    conn_s.close()                                                #关闭发送链接

if __name__ == '__main__':
    receive_conn,send_conn=Pipe()                               #管道对象返回两个连接对象
    i=0                                                         #发送条数计数变量
    while i<2:                                              #发送两条
            i += 1
            pp=Process(target=do_send,args=(send_conn,i,))
            pp.start()
            pp.join()
            print('接收数据%s成功！'%(receive_conn.recv()))
            
