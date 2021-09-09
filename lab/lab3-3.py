#!/usr/bin/python3.8
# -*- coding: UTF-8 -*-
# @Time : 2021/9/9 8:57 
# @Author : keke618
# @File : lab3-3.py 
# @Software: PyCharm
import os
ifconfig_result = os.popen("ifconfig "+" ens160").read()
print(ifconfig_result)


