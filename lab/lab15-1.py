#!/usr/bin/python3.8
# -*- coding: UTF-8 -*-
# @Time : 2021/10/24 14:35
# @Author : keke618
# @File : lab15-1.py
# @Software: PyCharm

import sqlite3
import paramiko
import os
import hashlib
import time
import re


def create_db(dbname, table_name):
    if os.path.exists(dbname):
        os.remove(dbname)
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    cursor.execute(
        f"CREATE TABLE {table_name}(ip varchar(40), config varchar(99999), md5value varchar(99999))"
        # "CREATE TABLE %s(ip varchar(40), config varchar(99999), md5value varchar(99999))"%table_name
    )
    conn.close()


def ssh_router(ip, username, passwd, cmd='dis cu', port=22):
    ssh = paramiko.SSHClient()  # 创建SSH Client
    ssh.load_system_host_keys()  # 加载系统SSH密钥
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 添加新的SSH密钥
    try:
        ssh.connect(ip, username=username, password=passwd, timeout=5, compress=True)  # SSH连接
    except Exception:
        print('无法登录到路由器，请检查配置!')
    else:
        shell = ssh.invoke_shell()  # 激活交互式shell
        shell.send(cmd + '\n')  # 发送命令
        time.sleep(1)
        result = shell.recv(65535).decode()  # 获取路由器返回的信息
        return result
    ssh.close()


def get_config_md5(ip, username, password):
    config_raw = ssh_router(ip, username, password)
    config = re.findall(r'(<sw1>dis cu\n#\n)(.*)(<sw1>)', config_raw, re.S)[0][1]
    md_obj = hashlib.md5()
    md_obj.update(config.encode())
    md5_value = md_obj.hexdigest()      # 16进制格式的hash值
    return config, md5_value


def write_config_md5_to_db():
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    for device in device_list:
        config, md5_value = get_config_md5(device, username, password)
        cursor.execute(f"SELECT * FROM {table_name} WHERE 'md5value' = '{md5_value}'")
        db = cursor.fetchall()  # 获取查询结果集中所有（剩余）的行，返回一个列表
        if db:
            cursor.execute(f"select * from {table_name} where 'ip' = '{device}'")
            ipadd = cursor.fetchall()
            if not ipadd:
                cursor.execute(f"""INSERT INTO {table_name}(ip,config,md5value) 
                               VALUES (?,?,?);""", (device, config, md5_value))
        else:
            cursor.execute(cursor.execute(f"UPDATE {table_name} SET md5value={md5_value} WHERE ip = {device}"))
    conn.commit()
    cursor.execute(f"select * from {table_name}")
    db_results = cursor.fetchall()
    for x in db_results:
        print(x[0], x[2])
    conn.close()


if __name__ == '__main__':
    dbname = 'config_route.db'
    table_name = 'config_md5'
    username = 'admin'
    password = 'admin123'
    device_list=['192.168.80.111','192.168.80.112']
    create_db(dbname,table_name)
    write_config_md5_to_db()