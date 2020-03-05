#多线程爬虫
import urllib.request
import re
import urllib.error
import threading


headers = ('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36')
opener = urllib.request.build_opener()
opener.addheaders = [headers]
urllib.request.install_opener(opener)

class T1(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        try:
            for i in range(1,10,2):
                url = r'https://www.qiushibaike.com/text/page/' + str(i)+'/'
                data = urllib.request.urlopen(url)
                html = data.read().decode('utf-8','ignore')
                #print(html)
                pat = '<div class="content">.*?<span>(.*?)</span>.*?</div>'
                data_list = re.compile(pat,re.S).findall(html)
                for j in range(len(data_list)):
                    print('第'+str(i)+'页第'+str(j)+'个段子是：')
                    print(data_list[j])
        except urllib.error.URLError as e:
            if hasattr(e,'reason'):
                print('We failed to reach a server.')
                print('Reason:', e.reason)
            elif hasattr(e,'code'):
                print('The server couldn\'t fulfill your request')
                print('Error code:', e.code)
                

class T2(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
         try:
             for i in range(2,10,2):
                url = r'https://www.qiushibaike.com/text/page/' + str(i)+'/'
                data = urllib.request.urlopen(url)
                html = data.read().decode('utf-8','ignore')
                #print('第'+str(i)+'个html是'+html)
                pat = '<div class="content">.*?<span>(.*?)</span>.*?</div>'
                data_list = re.compile(pat,re.S).findall(html)
                for j in range(len(data_list)):
                    print('第'+str(i)+'页第'+str(j)+'个段子是：')
                    print(data_list[j])
         except urllib.error.URLError as e:
            if hasattr(e,'reason'):
                print('We failed to reach a server.')
                print('Reason:', e.reason)
            elif hasattr(e,'code'):
                print('The server couldn\'t fulfill your request')
                print('Error code:', e.code)

if __name__ == '__main__':
    t1 = T1()
    t1.start()
    t2 = T2()
    t2.start()
