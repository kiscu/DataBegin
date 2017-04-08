# coding:utf8

import urllib
import re
dStr = urllib.urlopen('https://finance.yahoo.com/quote/%5EDJI/components?p=%5EDJI').read()
m = re.findall('<tr><td class="yfnc_tabledata1"><b><a href=".*?">(.*?)</a></b></td><td class="yfnc_tabledata1">(.*?)</td>.*?<b>(.*?)</b>.*?</tr>', dStr)
if m:
    print m
    print '\n'
    print len(m)
else:
    print 'not match'
