# coding:utf8
f = open('firstpro.txt', 'w')
f.write('Hello, World!')
f.close()

f = open('firstpro.txt')
p1 = f.read(5)
p2 = f.read()
print p1, p2
f.close()