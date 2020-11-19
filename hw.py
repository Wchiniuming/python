# -*- coding: utf-8 -*-

'''
@Author: your name
@Date: 2019-08-13 15:19:46
@LastEditTime : 2019-12-23 16:07:50
@LastEditors  : Please set LastEditors
@Description: In User Settings Edit
@FilePath: \python\hw.py
'''
# L = ['Hello', 'World', 19, 'Apple', None]
# lowerL = []

# def lowercase(l):
#     for s in l:
#         if isinstance(s, str):
#             lowerL.append(s.lower())
#         else:
#             lowerL.append(s)
#     return print(lowerL)

# lowercase(L)
# def triangle(max):
#     L=[1]
#     while len(L)<=max:
#         yield L
#         L1=[1]
#         for n in range(1,len(L)):
#             L1.append(L[n-1]+L[n])
#         L1.append(1)
#         L=L1
# g=triangle(6)
# for a in g:
#     print(a)

# ##---画图
# from turtle import *

# # 设置色彩模式是RGB:
# colormode(255)

# lt(90)

# lv = 14
# l = 120
# s = 45

# width(lv)

# # 初始化RGB颜色:
# r = 0
# g = 0
# b = 0
# pencolor(r, g, b)

# penup()
# bk(l)
# pendown()
# fd(l)

# def draw_tree(l, level):
#     global r, g, b
#     # save the current pen width
#     w = width()

#     # narrow the pen width
#     width(w * 3.0 / 4.0)
#     # set color:
#     r = r + 1
#     g = g + 2
#     b = b + 3
#     pencolor(r % 200, g % 200, b % 200)

#     l = 3.0 / 4.0 * l

#     lt(s)
#     fd(l)

#     if level < lv:
#         draw_tree(l, level + 1)
#     bk(l)
#     rt(2 * s)
#     fd(l)

#     if level < lv:
#         draw_tree(l, level + 1)
#     bk(l)
#     lt(s)

#     # restore the previous pen width
#     width(w)

# speed("fastest")

# draw_tree(l, 4)

# done()

##高阶函数---------string是不可变数据类型，所以不能直接更改其中的字符
# def normalize(name):
#     def upperN(n):
#         n[0] = n[0].upper()
#         return n
#     return map(upperN,name)

# print(list(normalize(L)))-----------string.title()
# def normalize(name):
#     newName = name[0].upper() + name[1:]
#     return newName

# L = ['adam', 'lisa', 'bart']
# print(list(map(normalize,L)))

#reduce()求积
# from functools import reduce
# L2 = [3,5,7,9]
# def prod(list):
#     return reduce(lambda x , y: x*y, list)
# print(prod(L2))

##sorted()排序
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88), ('asa', 88)]
# def by_name(t):
#     return t[0]

# def by_score(t):
#     return -t[1]

# L2 = sorted(L, key=by_name)
# L3 = sorted(L, key=by_score)
# print(L2)
# print(L3)

#类属性
class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1


# 测试:
if Student.count != 0:
    print('false!')
else:
    bart = Student('Bart')
    print(Student.count)
    if Student.count != 1:
        print('false1!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('false2!')
        else:
            print('Students:', Student.count)
            print('pass!')