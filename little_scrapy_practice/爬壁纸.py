#爬多种类型壁纸
#import requests
import urllib.request
import re
import os

def open_url(url):  #定义函数，模拟浏览器访问目标网址
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36')
    resp = urllib.request.urlopen(req)
    html = resp.read().decode("gbk")
    return html

def get_url_list(html):  #定义函数，将单张图片html地址保存在列表中
    #img_src = r'img id="bigImg" src="(.*?+\.jpg)"'
    img_html_url = 'a href="(/tupian/\d{5}\.html)"'
    url_list = re.findall(img_html_url,html)
    for each in url_list:
        print(each)
    '''for each in img_list:
        filename = each.split("/")[-1]
        urllib.request.urlretrieve(each,filename)'''
    return url_list



def get_img_url(img_html_url,url_base):  #定义函数，获取单张大图url地址
    img_html = open_url(img_html_url)
    img_url_pat = 'img src="(.*?\.jpg)" data-pic'
    img_url = re.findall(img_url_pat,img_html)
    img_url = url_base + img_url[0]
    print(img_url)
    return img_url
    
    
    
def download_img(folder = '壁纸图'):   #主函数，访问服务器
    if not os.path.isdir(folder):
        os.mkdir(folder)
    os.chdir(folder)
    url_base = 'http://pic.netbian.com'
    for i in range(10):
        if i==0:
            continue
        elif i==1:
            url = url_base + '/'
        else:
            url = url_base + '/index_' + str(i) + '.html'
        html = open_url(url)
        url_list = get_url_list(html)   #获取所有图片html_url
        for each in url_list:
            #filename = each.split("-1")[-1]
            img_html_url = url_base + str(each)
            img_url = get_img_url(img_html_url,url_base)  #获取图片存储地址
            filename = img_url.split("/")[-1]
            urllib.request.urlretrieve(img_url,filename)
            '''with open(filename,'wb') as f:
                headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
                r=requests.get(img_url,headers = headers)
                f.write(r.content)
                '''

if __name__ == '__main__':
    download_img()
