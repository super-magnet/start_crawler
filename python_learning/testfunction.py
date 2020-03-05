import math
def sums(*num):                                #自定义函数，传递元祖数字
    '''
    >>>sums(1,2,3,4,5)                         #两个测试用例
    15
    >>>sums('s',2,3,4,5)
    '''
    total = math.trunc(sum(num))           #对元组元素求和，并取整数
    return total                            #返回累计结果（必须要求，否则无法比较结果）
    #print('累加为：%f'%(total))            #若采用打印输出结果，前面不能加汉子提醒
    if __name__ == '__main__':
        import doctest                      #导入doctest模块
        doctest.testmod(verbose=False)      #调用testmod()，读取两个测试，测试上述函数
