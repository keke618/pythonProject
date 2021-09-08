#!/usr/bin/python
# -*- coding: UTF-8 -*-
department1 = 'Python'
manager1 = "Jack"
salary1 = 20000
department2 = "security"
manager2 = "mary"
salary2 = 15000

line1 = f'department1 name:{department1:10s} manager1:{manager1:10s} salary1:{salary1:5}'
line2 = f'department2 name:{department2:10s} manager2:{manager2:10s} salary2:{salary2:5}'
length = len(line1)
print('='*length)
print(line1)
print(line2)
print('='*length)
