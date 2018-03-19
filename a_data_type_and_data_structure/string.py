#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' module comment '

__author__ = 'Ashin Ren'

# python 中数字和字符串都是不可变的
x = 5
y = x
y += 1
print(x,y)

# python3 没有long整数类型了,**是平方
p = 5 ** 6
#q = 3L
q = 3
r = q + 2
print(p,q,r)

#高精度小数
from decimal import *
#import decimal 这样写，后面用的时候需要加decimal前缀
print(Decimal(5.1),Decimal('5.1'),float(Decimal('1.1')))
print(1.1+2.2)
print(Decimal('1.1')+Decimal('2.2'))

#复数
c = 5.4 +0.8j
print(type(c))

import random
print(random.randint(1,10))

p = 'pad'
p = 'o'.join((p[:1],p[2:]))
print(p)

line = 'The quick brown fox.'
print(line.find('q'))
print(line.index('q'))
print(line.title())
print(line.strip())

#print=sys.stdout.write(xxx)+sys.stdout.write('\n')
import sys
sys.stdout.write('www')
sys.stdout.write('rrr')

#QString 可变的字符串
from PyQt4.Qt import *
a = QString('apple')
print(type(a))