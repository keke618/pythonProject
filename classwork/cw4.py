#!/usr/bin/python3.8
# -*- coding: UTF-8 -*-
# @Time : 2021/9/22 9:23 
# @Author : keke618
# @File : cw4.py 
# @Software: PyCharm
import re
from pprint import pprint

asa_conn = "TCP Student 192.168.189.167:32806 Teacher 137.78.5.128:65247, idle 0:00:00, bytes 74 , flags UIO\n TCP Student 192.168.189.167:80 Teacher 137.78.5.128:65233 , idle 0:00:03, bytes 334516 , flags UIO"
asa_Dict = {}
