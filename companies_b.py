# coding:utf8
s = 'Tencent Technology Company Limited'
f = open(r'companiescopy.txt', 'a+')
f.writelines('\n')
f.writelines(s)
f.seek(0, 0)
cNames = f.readlines()
print cNames
f.close()
