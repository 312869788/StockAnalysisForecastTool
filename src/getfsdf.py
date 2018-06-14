import requests
import re

url1 = 'http://quotes.money.163.com/trade/zjlx_600600.html#01b01'
r = requests.post(url1)
title = re.findall('.*',r.text,re.S)
print(title)
for each in title:
    print(each)
print(r)
r.encoding = 'utf-8'
#p_json = r.json()
#print(p_json)