#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random

num_list = []
for figure in range(1,101):
    num = random.randint(1,100)
    num_list.append(num)

print("生成的100个整数是：",num_list)
fig = 0
for i in num_list:
    fig = fig + i
print("100个整数之和",fig)
print("100个整数中最大值",max(num_list))
print("100个整数中最小值",min(num_list))

