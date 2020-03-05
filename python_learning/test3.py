def file_view(file_name,line_number):
    if line_number.strip() == ':':    #字符串strip()函数的作用，删除前后空格，即判断输如为‘：’
        begin = '1'
        end = '-1'

    (begin,end) = line_number.split(':')    #字符串split()函数的作用

    if begin == '':
        begin = '1'
    if end == '':
        end = '-1'

    if begin == '1' and end =='-1':
        prompt = '的全文'
    elif begin == '1': 
        prompt = '从开始到%s' % end
    elif end == '-1':
        prompt = '从%s开始到结束'% begin
    else:
        prompt = '从第%s行到第%s行' %(begin,end)

    print('%s文件%s的内容如下：\n' % (file_name,prompt))

    begin = int(begin) -1
    end = int(end)
    lines= end - begin

    f = open(file_name)

    for i in range(begin):           #用于消耗begin之前的内容
        f.readline()

    if lines < 0:
        print(f.read())
    else:
        for j in range(lines):
            print(f.readline(), end = ' ')
    f.close()
    

file_name = input('请输入要打开的文件：')
line_number = input('请输入需要显示的行数【格式如 13:21 或：21或21：或：】：')
file_view(file_name,line_number)
