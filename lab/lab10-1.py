#!/usr/bin/python3.8
# -*- coding: UTF-8 -*-
# @Time : 2021/10/6 8:26 
# @Author : keke618
# @File : lab10-1.py
# @Software: PyCharm
import paramiko
import time


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


if __name__ == '__main__':
    ip = '192.168.80.110'
    username = 'user-ssh'
    passwd = 'huawei123'
    cmd = 'dis ip int br'
    print(ssh_router(ip, username, passwd, cmd))
