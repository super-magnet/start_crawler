def file_replace(file_name,rep_word,new_word):
    f_read = open(file_name)

    content = []
    count = 0
    for eachline in f_read:
        if rep_word in eachline:
            count += eachline.count(rep_word)
            eachline = eachline.replace(rep_word,new_word)
        content.append(eachline)        #采用content将原有文件内容替换后，全部缓存

    decide = input('\n文件%s中共有%s个【%s】替换为【%s】吗？\【YES/NO】：'\
                   %(file_name,count,rep_word,new_word))

    if decide in ['YES','yes','Yes']:      #用户确认替换后，将content中内容写入原文件，实现覆盖和替换
        f_write = open(file_name,'w')
        f_write.writelines(content)
        f_write.close()

    f_read.close()

file_name = input('请输入文件名：')
rep_word = input('请输入需要替换的单词或字符：')
new_word = input('请输入新的单词或字符：')
file_replace(file_name,rep_word,new_word)
