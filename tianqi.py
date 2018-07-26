#coding=utf-8

from urllib import request
import sys
import re

def acq_html(area):
	url = 'http://www.tianqi.com/' + area
	req = request.Request(url)
	resp = request.urlopen(req, timeout=10)
	html = resp.read().decode("utf-8")
	return html

def acq_temp_now(html):
	#pattern = re.compile('weather_info.*?h2>(.*?)<.*?week">(.*?)</dd>.*?now"><b>(.*?)</b>.*?b>(.*?)</b>(.*?)<.*?shidu.*?b>(.*?)</b><b>(.*?)</b><b>(.*?)</b>(.*?)</b.*?kongqi.*?;:>(.*?)<.*?6>(.*?)</h6><span>(.*?)<.*?>(.*?)<', re.S)
	pattern = re.compile('weather_info.*?h2>(.*?)<.*?week">(.*?)</dd>.*?now"><b>(.*?)</b>.*?b>(.*?)</b>(.*?)<.*?shidu.*?b>(.*?)</b><b>(.*?)</b><b>(.*?)</b>.*?kongqi.*?;">(.*?)</.*?6>(.*?)<.*?n>(.*?)<b.*?>(.*?)<', re.S)
	now = re.findall(pattern, html)
	return now

if len(sys.argv) != 2:
	print ("Usage: tianqi.py area")
	print ("Example: tianqi.py wuhan")
	sys.exit()

list = acq_temp_now(acq_html(sys.argv[1]))
print (list[0][0])
