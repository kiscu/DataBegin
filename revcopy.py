# coding:utf8
f1 = open(r'companies.txt')
cNames = f1.readlines()
for i in range(0, len(cNames)):
    cNames[i] = str(i+1) + ' ' + cNames[i]
f1.close()
f2 = open(r'scompanies.txt', 'w')
f2.writelines(cNames)
f2.close()