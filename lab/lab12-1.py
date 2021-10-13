#!/usr/bin/python3.8
# -*- coding: UTF-8 -*-
# @Time : 2021/10/12 8:11 
# @Author : keke618
# @File : lab12-1.py 
# @Software: PyCharm
import ping_ssh


def get(ip_list, username, passwd):
    for ip in ip_list:
        result = ping_ssh.xxx_ping(ip)
        if result == 0:
            res = ping_ssh.ssh_router(ip=ip, username=username, passwd=passwd,cmd='dis ip int br')
            with open('./route.txt', mode='w', encoding='utf-8') as f:
                f.write(res)
        else:
            print(f'ip为{ip}的网络不通')


if __name__ == '__main__':
    ip_list = ['192.168.80.11', '192.168.80.12', '192.168.80.110', '192.168.80.120', '192.168.80.121','172.17.21.74','47.241.228.69']
    username = 'root'
    passwd = '+q19936110'
    get(ip_list=ip_list, username=username, passwd=passwd)