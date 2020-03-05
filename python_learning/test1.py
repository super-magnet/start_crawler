'''file_name1 = input('请输入需要比较的第一个文件名：')
file_name2 = input('请输入需要比较的第二个文件名：')
f1 = open(file_name1,'r')
f2 = open(file_name2,'r')
count = 0
z如何对比文件中一行行的语句'''

def file_compare(file1,file2):
    f1 = open(file1)
    f2 = open(file2)
    count = 0 #统计行数
    differ = []  #统计不一样的数量


    for line1 in f1:            #迭代读取文件对象中每一行
        line2 = f2.readline()   #采用.readline()方法读取文件对象中每一行
        count += 1
        if line1 != line2：
            differ.append(count)

    f1.close()
    f2.close()
    return differ

file1 = input('请输入第一个文件名：')
file2 = input('请输入第二个文件名：')

differ = file_compare(file1,file2)

if len(differ) == 0:
    print('两个文件一样')
else:
    print('两个文件共有%s处不同'%(len(differ)))
    for each in differ:
        print('第%s行不一样' %(each))

        
