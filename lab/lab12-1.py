#!/usr/bin/python3.8
# -*- coding: UTF-8 -*-
# @Time : 2021/10/6 9:25 
# @Author : keke618
# @File : lab12-1.py 
# @Software: PyCharm
import sqlite3

homework_info = [
    {'id': '001', 'name': '梁栋', 'homework_num': 12},
    {'id': '002', 'name': '张毅', 'homework_num': 11},
    {'id': '003', 'name': '万前', 'homework_num': 12},
    {'id': '004', 'name': '李政', 'homework_num': 11},
    {'id': '005', 'name': '周煜林', 'homework_num': 11},
]

# 连接到数据库 数据库文件是“homework.db”
# 如果数据库不存在的话，将会自动创建一个 数据库
conn = sqlite3.connect('homework.db')
print("Opened database successfully")

# 创建一个游标 tab
tab = conn.cursor()
# 执行一条语句,创建表
tab.execute(
    '''CREATE TABLE TABINFO
     (ID INT PRIMARY KEY     NOT NULL,
      NAME           TEXT    NOT NULL,
      HOMEWORK_NUM            INT     NOT NULL);
    '''
)
print("Table created successfully")


for homework in homework_info:
    id = homework['id']
    name = homework['name']
    homework_num = homework['homework_num']
    # 执行一条语句,插入记录
    tab.execute(f"INSERT INTO TABINFO (ID,NAME,HOMEWORK_NUM) VALUES ({id},'{name}',{homework_num})")

conn.commit()
conn.close()