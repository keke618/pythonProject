#!/usr/bin/python3.8
# -*- coding: UTF-8 -*-
# @Time : 2021/9/15 9:04 
# @Author : keke618
# @File : cw3.py 
# @Software: PyCharm
import re
s = 'Port-channel1.189 192.168.10.25 YES CONFIG up'
result = re.match('(\w+-\w+.\d+)\s+(\d+.\d+.\d+.\d+)\s+\w+\s+\w+\s+(\w+)', s).groups()
info = f'''
接口      :{result[0]:<15}
IP地址    :{result[1]:<15}
状态      :{result[2]:<15}
'''
print(info)

