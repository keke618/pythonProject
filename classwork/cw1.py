#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Q1
print('Today is 2021-9-28')
# Q2
str1 = 'python'
str2 = f'{str1[2:]}-{str1[0:2]}'
print(str2)
# Q3
word = "scallywag"
sub_word = word[2:6]
print(sub_word)
# Q4
url = 'https://sc.chinaz.com/jianli/210904053071.htm'
url = url.split('/')[-1]
url = url.split('.')[0]
print(url)
