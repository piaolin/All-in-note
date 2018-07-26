from urllib import request
#from urllib import parse
import re

word = input("Please input the word you don't know:")
url = "http://www.youdao.com/w/" + word
headers = {'Host': 'www.youdao.com',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
'Referer': 'http://www.youdao.com/w/eng/fun/',
'Cookie': 'YOUDAO_MOBILE_ACCESS_TYPE=1; DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; OUTFOX_SEARCH_USER_ID=540153678@111.176.49.89; JSESSIONID=abcX43G7Olh6BdjIqJ5fw; ___rl__test__cookies=1518162804337; OUTFOX_SEARCH_USER_ID_NCOO=820310262.605182; _ntes_nnid=36cb32c6805b20321ff23417fb07484d,1518162772291; search-popup-show=2-9',
'Connection': 'close',
'Upgrade-Insecure-Requests': '1'
}
req = request.Request(url, headers=headers)
response = request.urlopen(req)
html = response.read().decode("utf-8")
pattern = re.compile('<div.*?trans-container">.*?<ul>(.*?)</ul>.*?webTrans"', re.S)
explain = re.findall(pattern, html)
#print(html)
for i in explain:
    i = i.replace("<li>", "")
    i = i.replace("</li>", "")
    print(i)