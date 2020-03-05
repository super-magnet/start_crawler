import urllib.request
import os
import requests

def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36')
    response = urllib.request.urlopen(url)
    html = response.read()
    return html

'''def get_page(url):
    html = url_open(url).decode('utf-8')
    #html = response.read().decode('utf-8')
    
    a = html.find('current-comment-page')+23
    b = html.find(']',a)
    #print(html[a:b])  可以打印出来，说明获取起始页码正常
    return html[a:b] '''
    
def find_imgs(url):
    html = url_open(url).decode('utf-8')
    img_addrs = []
    a = html.find('img class="BDE_Image" src=')
    while a != -1:
        b = html.find('.jpg',a,a+200)
        if b != -1:
            img_addrs.append(html[a+27:b+4])
        else:
            b=a+28  

        a = html.find('img class="BDE_Image" src=',b)
    for each in img_addrs:
        print(each)        #打印图片地址
    return img_addrs


def save_imgs(folder,img_addrs):
    '''for each in img_addrs:
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        r=requests.get(each,headers = headers)
        filename = each.split('/')[-1]
        f = open(filename,'wb')
        f.write(r.content)
        f.close()
        '''
    for each in img_addrs:
        filename = each.split('/')[-1]
        with open(filename,'wb') as f:
            img = url_open(each)
            f.write(img)
            
    
def download_dog(folder = '法国狼犬图'):
    os.mkdir(folder)
    os.chdir(folder)
    url = 'http://tieba.baidu.com/p/5848621868'
    #page_num = int(get_page(url))
    #page_url = url +'.html'    #获取起始页网址

    img_addrs = find_imgs(url)
    save_imgs(folder,img_addrs)
    
    '''for i in range(pages):
        if i>0:
            print(page_url) #打印爬虫内容页码
            img_addrs = find_imgs(page_url)
            save_imgs(folder,img_addrs)
            if i!=1:
                page_url = url+'_'+ str(i) +'.html'
    '''
             
        
        
if __name__ =='__main__':
    download_dog()
