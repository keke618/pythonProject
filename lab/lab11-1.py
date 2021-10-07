#!/usr/bin/python3.8
# -*- coding: UTF-8 -*-
# @Time : 2021/10/6 8:33 
# @Author : keke618
# @File : lab11-1.py 
# @Software: PyCharm

from kamene.all import *


class PingKamene:
    def __init__(self, dst):
        self.dst = dst

    def ping1(self):
        ping_pkt = IP(dst=self.dst) / ICMP()
        ping_result = sr1(ping_pkt, timeout=2, verbose=False)
        if ping_result:
            print(f'{self.dst} 通！!')
        else:
            print(f'{self.dst} 不通！！')


if __name__ == '__main__':
    ping = PingKamene(dst='192.168.10.11')
    ping.ping1()
