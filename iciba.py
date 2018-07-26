#coding='utf-8'
from urllib import request
from urllib import parse
import re

sentence = input("Please input the sentence you want to translate:")
data = parse.quote(sentence)

url = "http://www.iciba.com/" + data
headers = {'Host': 'www.iciba.com',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
'Referer': url,
'Cookie': 'iciba_u_rand=b30658f82b5e428a242d4268afb00118%40111.176.49.89; iciba_u_rand_t=1518168746; is_new_index=1; BAIDU_SSP_lcr=https://www.baidu.com/link?url=eHgzjW7m49LaMUS1OQc_G55FqfSmk_nSG--HJXIXIq3&wd=&eqid=a958c70600025252000000045a7d6aa7; UM_distinctid=16179e8b0ec382-0b9d70392e2efa-4c322172-144000-16179e8b0ed69e; CNZZDATA1257391275=767329200-1518166139-null%7C1518166139; screen-skin=screen-blue; cbdownload_num=1; cbdownload_time=download; search-history=%E6%88%91%E5%BE%88%E5%B8%85; c_word_history=%e6%88%91%e5%be%88%e4%b8%91; CNZZDATA1256556802=1257563741-1518168761-http%253A%252F%252Fwww.iciba.com%252F%7C1518168761',
'Connection': 'close',
'Upgrade-Insecure-Requests': '1'
}
req = request.Request(url, headers = headers)
response = request.urlopen(req)
html = response.read().decode("utf-8")
#print(html)
pattern = re.compile('<div.*?in-base.*?#333333;">(.*?)</div>', re.S)
result = re.findall(pattern, html)
if result:
    for i in result:
        print(i)
else:
    pattern = re.compile('prop.*?<span>(.*?)</span>.*?<span>(.*?)</span>', re.S)
    result = re.findall(pattern, html)
    for i in result:
        print(i)
