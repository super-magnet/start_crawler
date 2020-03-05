import urllib.request
import re
import requests

def open_url(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36')
    resp = urllib.request.urlopen(req)
    html = resp.read().decode('utf-8')

    return html

def get_img(html):
    p = r'<img src="([^"]+\.jpg)"'
    imglist= re.findall(p,html)

    '''for each in imglist:
        print(each)'''
    for each in imglist:
        filename = each.split("/")[-1]
        with open(filename,'wb') as f:
           img = open_url(each)
           f.write(img)
        
        '''headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        with open(filename,'wb') as f:
            r=requests.get(each,headers = headers)
            f.write(r.content)
        
        #urllib.request.urlretrieve(each,filename)，不添加headers，则拒绝访问服务器'''
    

if __name__ == '__main__':
    url = 'https://www.mzitu.com/173994/'
    page_url = url
    for i in range(67):
        if i!=0 and i!=1:
            page_url = url+str(i)
        if i != 1:
            print(page_url) #打印爬虫内容页码
            get_img(open_url(page_url))
