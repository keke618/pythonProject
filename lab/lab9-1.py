#!/usr/bin/python3.8
# -*- coding: UTF-8 -*-
# @Time : 2021/9/14 15:33 
# @Author : keke618
# @File : lab9-1.py 
# @Software: PyCharm

import logging
from kamene.all import *
logging.getLogger("kamene.runtime").setLevel(logging.ERROR) # 关闭不必要的报错


def xxx_ping(ip):
    ping_pkt = IP(dst=ip)/ICMP() # 制造一个Ping包
    ping_result = sr1(ping_pkt, timeout=2, verbose=False) # Ping并且把返回结果复制给ping_result
    # ping_result.show() # 查看回显结果
    if ping_result:
        print(f'{ip} 通！!')
    else:
        print(f'{ip} 不通！！')


if __name__ == '__main__':
    host = ['192.168.80.11', '192.168.80.12', '192.168.80.110', '192.168.80.120', '192.168.80.121']
    for ip in host:
        xxx_ping(ip)



