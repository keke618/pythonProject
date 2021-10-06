#!/usr/bin/python3.8
# -*- coding: UTF-8 -*-
# @Time : 2021/9/10 9:13 
# @Author : keke618
# @File : lab8-2.py 
# @Software: PyCharm

list1 = ['aaa', 111, (4, 5), 2.01]
list2 = ['bbb', 333, 111, 3.14, (4, 5)]

list_a = [a for a in list1 if a in list2]       # 两个列表表都存在的元素
list_b = [b for b in list1 if b not in list2]   # 在list1列表中而不在list2列表中
list_c = [c for c in list2 if c not in list1]   # 在list2列表中而不在list1列表中

for P1 in list_a:
    print(f'{P1} in list1 and list2')
for P2 in list_b:
    print(f'{P2} only in list1')
for P3 in list_c:
    print(f'{P3} only in list2')



# # 常规写法
# list_a = []                   # 两个列表表都存在的元素
# for x in list1:
#     if x in list2:
#         list_a.append(x)
# # print(list_a)
#
# list_b = []                   # 在list1列表中而不在list2列表中
# for z in list1:
#     if z not in list2:
#         list_b.append(z)
# # print(list_b)
#
# list_c = []                   # 在list2列表中而不在list1列表中
# for n in list2:
#     if n not in list1:
#         list_c.append(n)
# # print(list_c)
#
# # list_d = []                 # 两个列表中的不同元素
# # for y in (list1 + list2):
# #     if y not in list_a:
# #         list_d.append(y)
# # print(list_d)
