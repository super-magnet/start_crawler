import urllib.request
import random

url = 'http://45.32.164.128/ip.php'
#url = 'http://ip.chinaz.com/getip.aspx'     #random.choice(iplist)
iplist = ['218.64.69.79:8080','124.160.56.76:37511','101.231.234.38:8080']
proxy_support = urllib.request.ProxyHandler({'http:':'118.24.151.76:8118'})
opener = urllib.request.build_opener(proxy_support)
opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36')]
urllib.request.install_opener(opener)
response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')

print(html)
