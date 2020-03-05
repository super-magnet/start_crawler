#下载新浪新闻内容
import urllib.request
import re
import os
data = urllib.request.urlopen('https://news.sina.com.cn/')
html = data.read().decode('utf-8','ignore')
pat ='href="(https://news.sina.com.cn/.*?)"'
all_url = re.findall(pat,html)
i = 0
if not os.path.isdir('sina_news'):
        os.mkdir('sina_news')
os.chdir('sina_news')
for each in all_url:
    try:
        filename = each.split('/')[-1] + '.html'
        urllib.request.urlretrieve(each,filename) 
        print('--成功--')
    except urllib.error.URLError as e:
        if hasattr(e,'reason'):
            print('We failed to reach a server.')
            print('Reason:', e.reason)
        if hasattr(e, 'code'):
            print('The server couldn\'t fulfill the request.')
            print('Error code:', e.reason)
