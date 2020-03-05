'''File_Name = input('请输入文件名：')
Wenjian = open(File_Name,'w')
Content = input('请输入内容【单独输入"w"保存退出】：\n')
Wenjian.write(Content)
Wenjian.close()
自己设计的程序，缺陷明显，多行输入要引入无限循环，采用模块化函数或类思维'''

#下面是参考答案方式
def file_write(file_name):
    f = open(file_name,'w')
    print('请输入内容【单独输入\':w\'保存退出】：')

    while True:
        write_some = input()
        if write_some != ':w':
            f.write('%s\n'% (write_some))
        else:
            break
    f.close()

file_name = input('请输入文件名：')
file_write(file_name)
        
