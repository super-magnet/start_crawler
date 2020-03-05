def file_view(file_name,line_number):
    print('%s文件的前%s行内容如下：\n' % (file_name,line_number))
    f = open(file_name)
    for i in range(int(line_number)):           #注意int()函数的作用
        print(f.readline(),end=' ')
    f.close()

file_name = input('请输入要打开的文件：')
line_number = input('请输入需要显示文件的前几行：')
file_view(file_name,line_number)
