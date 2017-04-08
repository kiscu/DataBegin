# coding:utf8
import urllib.request
import re
dStr = urllib.request.urlopen('https://hk.finance.yahoo.com/q/cp?s=%5EDJI').read()
getdStr=dStr.decode()
#在python 3中urllib.read()返回bytes对象而非str，语句功能是将dStr转换成str
#convert dStr into str, urllib.read() returns bytes objects instead of str
m = re.findall('<tr><td class="yfnc_tabledata1"><b><a href=".*?">(.*?)</a></b></td><td class="yfnc_tabledata1">(.*?)</td>.*?<b>(.*?)</b>.*?</tr>', getdStr)
if m:
    print(m)
    print('\n')
    print (len(m))
else:
    print ('not match')
