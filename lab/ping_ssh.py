#!/usr/bin/python3.8
# -*- coding: UTF-8 -*-
# @Time : 2021/10/13 8:20 
# @Author : keke618
# @File : ping_ssh.py 
# @Software: PyCharm
from kamene.all import *
import paramiko
import time


def xxx_ping(ip):
    ping_pkt = IP(dst=ip)/ICMP() # 制造一个Ping包
    ping_result = sr1(ping_pkt, timeout=2, verbose=False) # Ping并且把返回结果复制给ping_result
    # ping_result.show() # 查看回显结果
    if ping_result:
        # print(f'{ip} 通！!')
        return 0
    else:
        # print(f'{ip} 不通！！')
        return 1

def ssh_router(ip, username, passwd, cmd):
    ssh = paramiko.SSHClient()                      # 创建SSH Client
    ssh.load_system_host_keys()                     # 加载系统SSH密钥
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())   # 添加新的SSH密钥
    try:
        ssh.connect(ip, username=username, password=passwd, timeout=5)       # SSH连接
    except Exception:
        print('无法登录到路由器，请检查配置!')
    else:
        shell = ssh.invoke_shell()      # 激活交互式shell
        shell.send(cmd + '\n')          # 发送命令
        time.sleep(1)
        result = shell.recv(1024).decode()  # 获取路由器返回的信息
        return result
    ssh.close()