#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' module comment '

__author__ = 'Ashin Ren'

#元组tuple
empty=()
print(type(empty))
#元组可以省略括号
items=1,'t',3
print(type(items))
print(items[-1])

#列表list
l=[1,'2',items]
print(l)
l.insert(2,'yy')
print(l)
del l[1]
print(l)
l.remove('yy')
print(l)
#以切片的方式插入
l[1:1]=['yu']
print(l)
#以切片的方式删除
l[1:2]=[]
print(l)
#使用切片可以强制对象使用深复制（只有当前列表会变成深复制，其它的不变）

#字典dict
d={1:'11',2:'22'}
print(d[1])
#如果各键是有效的标示符，可以使用更简单的语法
d=dict(B12=1000,C8=900,A=9)
print(d)