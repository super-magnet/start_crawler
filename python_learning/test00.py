import os
'''all_files = os.listdir('.')
for each in all_files:
    print('%s的大小是%sbytes' %(each,str(os.path.getsize(each))))
自己设计的程序能运行，但是忽略了区分‘文件’和‘路径’'''

all_files = os.listdir('.')
file_dict = dict()

for each_file in all_files:
    if os.path.isfile(each_file):
        file_size = os.path.getsize(each_file)
        file_dict[each_file] = file_size

for each in file_dict.items():
    print('%s【%d Bytes】' %(each[0],each[1]))
