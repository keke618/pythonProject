#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re

ASA = 'TCP server 172.16.1.101:443 localserver 172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO'

# 使用search函数
# server = re.search('([0-9|a-f]{3}.)(.*?)(:[0-9|a-f]{3})', ASA)
# protocol = re.search('\w+', ASA)
# localserver = re.search('([0-9|a-f]{3}.)(.*?)([0-9|a-f]{5})', ASA)
# idle = re.search('([0-9]{1}:)([0-9]{2}:)([0-9]{2})', ASA)
# bytes_num = re.search('([0-9]{8})', ASA)
# flags = re.search('[U].*[O]', ASA)
#
# localserver = localserver.group()[-17:-1]
# idle1 = idle.group()
# idle1_1 = idle1.split(':')[0]
# idle1_2 = idle1.split(':')[1]
# idle1_3 = idle1.split(':')[2]
# info = f'''
# protocol    : {protocol.group():<20}
# server      : {server.group():<20}
# localserver : {localserver:<20}
# idle        : {idle1_1}小时 {idle1_2}分钟 {idle1_3}秒
# bytes       : {bytes_num.group():<20}
# flags       : {flags.group():<20}
# '''
# print(info)

# 使用match函数方法
result = re.match('(\w+)\s+server\s+(\d+\.\d+\.\d+\.\d+:\d+)\s+localserver\s+(\d+\.\d+\.\d+\.\d+:\d+),\s+idle\s+(\d+:\d+:\d+),\s+bytes\s+(\d+),\s+flags\s+(\w+)', ASA).groups()
# print(result)
idle1 = result[3]
idle1_1 = idle1.split(':')[0]
idle1_2 = idle1.split(':')[1]
idle1_3 = idle1.split(':')[2]
info = f'''
protocol    : {result[0]:<20}
server      : {result[1]:<20}
localserver : {result[2]:<20}
idle        : {idle1_1}小时 {idle1_2}分钟 {idle1_3}秒
bytes       : {result[4]:<20}
flags       : {result[5]:<20}
'''
print(info)



# 测试
# print(localserver)
# print(flags.group())
# print(bytes_num.group())
# print(idle.group())
# print(protocol.group())
# print(server.group())
