#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' module comment '

__author__ = 'Ashin Ren'

count=10
while count>0:
    print(count)
    count -= 1
#带else分支的while循环(for循环中也可以带else)
m=0
while m<0:
    print('pass')
else:
    print('error')

#使用for循环
for i in range(2,10,3):
    print('num:',i)