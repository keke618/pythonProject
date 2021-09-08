#!/usr/bin/python3.8
# -*- coding: UTF-8 -*-
# @Time : 2021/9/8 10:17
# @Author : keke618
# @File : cw2.py
# @Software: PyCharm
department1 = 'Python'
manager1 = "Jack"
salary1 = 20000
department2 = "security"
manager2 = "mary"
salary2 = 15000

# 方法一
line1 = 'department1 name:%-10s manager1:%-10s salary1:%5d'%(department1,manager1,salary1)
line2 = 'department2 name:%-10s manager2:%-10s salary2:%5d'%(department2,manager2,salary2)

# # 方法二
# line1 = 'Department1 name:{0:10} Manager1:{1:10} Salary1:{2:5}'.format(department1, manager1, salary1)
# line2 = 'Department2 name:{0:10} Manager2:{1:10} Salary2:{2:5}'.format(department2, manager2, salary2)
# # 方法三
# line1 = f'department1 name:{department1:10s} manager1:{manager1:10s} salary1:{salary1:5}'
# line2 = f'department2 name:{department2:10s} manager2:{manager2:10s} salary2:{salary2:5}'

length = len(line1)
print('='*length)
print(line1)
print(line2)
print('='*length)


# - 指定左对齐
# + 表示输出的数字总要带着符号；整数带+，负数带-。
# 0 表示宽度不足时补充 0，而不是补充空格。