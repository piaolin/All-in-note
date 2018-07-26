#coding=utf-8

from urllib import request
from urllib import parse
from urllib import error
import sys
import re

def tele_area_acq(url):
	req = request.Request(url)
	response = request.urlopen(req)
	html = response.read().decode('utf-8')
	pattern_31 = re.compile('mbb(.*?)cs', re.S)
	pattern_32 = re.compile('<a href="(.*?)">', re.S)
	url_all_area = re.findall(pattern_31, html)
	url_list_area = re.findall(pattern_32, url_all_area[0])
	return url_list_area

def tele_acq(list):
    tele=[]
    pattern = re.compile('<div class="page-frame-wrap page-main"(.*?)<div class="mpr"', re.S)
    pattern_1 = re.compile('<li>.*?>(.*?)</a></li>', re.S)
    for i in list:
        req = request.Request(i)
        response = request.urlopen(req)
        html = response.read().decode('utf-8')
        tele_all = re.findall(pattern, html)
        tele = tele + re.findall(pattern_1, tele_all[0])
    return tele

def page_acq(url):
    req = request.Request(url)
    response = request.urlopen(req)
    html = response.read().decode('utf-8')
    pattern_21 = re.compile('pages(.*?)<div class="mbox cs', re.S)
    pattern_22 = re.compile('<a href="(.*?)">', re.S)
    url_all = re.findall(pattern_21, html)
    url_list = re.findall(pattern_22, url_all[0])
    return url_list

tele_area_all=[]
url = 'http://www.baishicha.com/'

if (len(sys.argv) != 3 and len(sys.argv) != 4):
    print ("Usage: baishicha.py <area> <opeartor>")
    print ("Usage: baishicha.py <area> <opeartor> <tele>")
    print ("Example: baishicha.py wuhan dianxin")
    print ("Example: baishicha.py wuhan dianxin 153")
    sys.exit()
elif (len(sys.argv) == 3):
    list_area = tele_area_acq(url + sys.argv[1] + '-' + sys.argv[2])
    for i in list_area:
        url_1 = page_acq(i)
        tele_area_all += tele_acq(url_1)
elif (len(sys.argv) == 4):
    url_list = page_acq(url + sys.argv[1] + '-' + sys.argv[2] + '-' + sys.argv[3])
    tele_area_all += tele_acq(url_list)

for i in tele_area_all:
    print (i[0:7])
print (len(tele_area_all))