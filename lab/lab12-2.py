#!/usr/bin/python3.8
# -*- coding: UTF-8 -*-
# @Time : 2021/10/7 9:11 
# @Author : keke618
# @File : lab12-2.py 
# @Software: PyCharm
import sqlite3


def select_sql():
    notice = '''
    请输入查询选项:
    输入1： 查询整个数据库
    输入2： 查询有关姓名
    输入3： 查询有关ID号
    输入4： 查询作业数
    输入0： 退出
    '''
    while True:
        conn = sqlite3.connect('homework.db')
        tab = conn.cursor()
        cur = []
        for c in tab.execute('SELECT * FROM TABINFO;'):
            cur.append(c)
        print(notice)
        select_all = input('请选择：')
        if select_all == '0':
            break
        elif select_all == '1':
            for c in cur:
                print(f'学生ID:{c[0]:<10}学生姓名:{c[1]:<10}学生作业数{c[2]:<10}')
            conn.close()
        elif select_all == '2':
            id = input('请输入id')
            c_id_list = [str(c[0]) for c in cur]
            if id not in c_id_list:
                print(f'学生ID为{id}的作业未查询到')
            else:
                for c in cur:
                    if id == str(c[0]):
                        print(f'学生ID:{c[0]:<10}学生姓名:{c[1]:<10}学生作业数{c[2]:<10}')
            conn.close()
        elif select_all == '3':
            name = input('请输入name')
            c_name_list = [str(c[1]) for c in cur]
            if name not in c_name_list:
                print(f'姓名为{name}的作业未查询到')
            else:
                for c in cur:
                    if name == str(c[1]):
                        print(f'学生ID:{c[0]:<10}学生姓名:{c[1]:<10}学生作业数{c[2]:<10}')
            conn.close()
        elif select_all == '4':
            homework = input('请输入homework')
            c_home_list = [str(c[2]) for c in cur]
            if homework not in c_home_list:
                print(f'作业数为{homework}的作业未查询到')
            else:
                for c in cur:
                    if homework == str(c[2]):
                        print(f'学生ID:{c[0]:<10}学生姓名:{c[1]:<10}学生作业数{c[2]:<10}')
            conn.close()
        else:
            print('输入错误请重试')


if __name__ == '__main__':
    select_sql()



