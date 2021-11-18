#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time : 2021/10/27 0:10
# @Author : XXX
# @Site : 
# @File : 123.py
# @Software: PyCharm
	import  sqlite3
import  paramiko
import  re
import hashlib
import time
import os


def createdb(dbname,tablename):
    if os.path.exists(dbname):
        os.remove(dbname)
    conn=sqlite3.connect(dbname)
    cursor=conn.cursor()
    cursor.execute("create table %s(ip varchar(40),config varchar(99999),md5value varchar (999))"%tablename)


def get_config_md5(ip,username,password):
    config_raw = ssh_router(ip,username,password)
    # print(config_raw)
    config = re.findall(r'(?<=display current-configuration).*?(?=return)', config_raw, re.S)[0]

    mdobj=hashlib.md5()
    mdobj.update(config.encode())
    md5_value = mdobj.hexdigest()
    return config,md5_value


def ssh_router(ip,username,password,cmd='dis cu',port=22):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(hostname=ip,username=username,password=password,timeout=5,compress=True)
    except Exception:
        print("no connect!")
    else:
        shell = ssh.invoke_shell()
        shell.send('display current-configuration' + '\n')
        time.sleep(3)
        for i in range(4):
            shell.send(b' ')
            time.sleep(0.5)
        result = shell.recv(65535).decode()
        result = re.sub(r'---- More ----.*?(?=[a-z])','',result,re.S)
        return result
    ssh.close()


def write_config_md5_to_db():
    conn = sqlite3.connect(dbname)
    cursor = conn.cursor()
    for device in device_list:
        config, md5_value = get_config_md5(device, username, password)
        cursor.execute(f"select * from {tablename} where 'md5value' = '{md5_value}'")
        db = cursor.fetchall()
        if not db:
            cursor.execute(f"select * from {tablename} where 'ip' = '{device}'")

            ipadd = cursor.fetchall()
            if not ipadd:
                cursor.execute(f"""INSERT INTO {tablename}(ip,config,md5value) 
                               VALUES (?,?,?);""", (device, config, md5_value))
            else:
                print('Delete!')
                cursor.execute(cursor.execute(f"UPDATE {tablename} SET md5value={md5_value} WHERE ip = {device}"))
    conn.commit()
    cursor.execute("select * from %s" % tablename)
    db_results = cursor.fetchall()
    for x in db_results:
        print(x[0], x[2])
    conn.close()

if __name__ == '__main__':
    dbname = 'routerconfig.db'
    tablename = 'wanghao'
    username = 'admin'
    password = 'admin123'
    device_list=['192.168.21.101','192.168.21.102']
    createdb(dbname,tablename)
    write_config_md5_to_db()
