#!/usr/bin/python3.8
# -*- coding: UTF-8 -*-
# @Time : 2021/10/6 8:08 
# @Author : keke618
# @File : lab9-2&3.py 
# @Software: PyCharm
import paramiko


def xxx_ssh(ip, username, port, passwd, cmd):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, port=port, username=username, password=passwd, timeout=5, compress=True)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    x = stdout.read().decode()
    return x


if __name__ == '__main__':
    print(xxx_ssh('192.168.80.10', 'root', '22', 'redhat', 'ls'))
    print(xxx_ssh('192.168.80.10', 'root', '22', 'redhat', 'pwd'))
