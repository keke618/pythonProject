#!/usr/bin/python3.8
# -*- coding: UTF-8 -*-
# @Time : 2021/9/9 8:57 
# @Author : keke618
# @File : lab3-3.py 
# @Software: PyCharm
import os
import re
ifconfig_result = os.popen("ifconfig "+" eth0").read()
print(ifconfig_result)
# windows直接用下面数据
# ifconfig_result = '''
# eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
#         inet 172.17.21.74  netmask 255.255.192.0  broadcast 172.17.63.255
#         inet6 fe80::216:3eff:fe06:c29a  prefixlen 64  scopeid 0x20<link>
#         ether 00:16:3e:06:c2:9a  txqueuelen 1000  (Ethernet)
#         RX packets 12760634  bytes 12226198574 (11.3 GiB)
#         RX errors 0  dropped 0  overruns 0  frame 0
#         TX packets 6475573  bytes 11686436753 (10.8 GiB)
#         TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
# '''
IP = re.search('([0-9]{3}.)([0-9]{2}.){2}([0-9]{2})', ifconfig_result)
NETMASK = re.search('([0-9]{3}.){3}[0]', ifconfig_result)
BROADCAST = re.search('([0-9]{3}.)([0-9]{2}.){2}([0-9]{3})', ifconfig_result)
MAC = re.search('([0-9|a-f]{2}:){5}([0-9|a-f]{2})', ifconfig_result)
info = f'''
IPADD     : {IP.group():<20}
NETMASK   : {NETMASK.group():<20}
BROADCAST : {BROADCAST.group():<20}
MAC       : {MAC.group():<20}
'''
print(info)

