import urllib.request
import urllib.parse
import json

content = input('请输入需要翻译的内容：')

##url = 'https://fanyi.baidu.com/v2transapi'
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
data = {}
data['i'] = content
data['from']='AUTO'
data['to']='AUTO'
data['smartresult']='dict'
data['client']='fanyideskweb'
data['salt']='15535307578293'
data['sign']= '64c748d8f9f8bcaf01a8f8384aad17bb'
data['ts']='1553530757829'
data['bv']='6945a57e1923a3517303cdcdb2d3d15e'
data['doctype']='json'
data['version']='2.1'
data['keyfrom']='fanyi.web'
data['action']='FY_BY_CLICKBUTTION'
data['typoResult']='false'

'''data['from'] = 'en'
data['to']='zh'
data['query']='I love you'
data['transtype']='translang'
data['simple_means_flag']='3'
data['sign']='949163.694426'
data['token']='89ae7af102769bf3e7cfeea2e44cb12a'
'''
data = urllib.parse.urlencode(data).encode('utf-8')

response = urllib.request.urlopen(url,data)
html = response.read().decode('utf-8')

target = json.loads(html)
print('翻译结果：%s' % (target['translateResult'][0][0]['tgt']))
