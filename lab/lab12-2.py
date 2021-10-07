#!/usr/bin/python3.8
# -*- coding: UTF-8 -*-
# @Time : 2021/10/7 9:11 
# @Author : keke618
# @File : lab12-2.py 
# @Software: PyCharm
import sqlite3


# class SelectSQL(object):
#     conn = sqlite3.connect('homework.db')
#     tab = conn.cursor()
#     cur = tab.execute('''SELECT * FROM TABINFO;''')
#
#     def sqlid_select(self):
#         sid = input('请输入id号')
#         for s_id in self.cur:
#             if sid == s_id[0]:
#                 print("ID = ", s_id[0])
#                 print("NAME = ", s_id[1])
#                 print("HOMEWORK_NUM = ", s_id[2])
#
#     def name_select(self):
#         name = input('请输入名字')
#         for s_name in self.cur:
#             if name == s_name[0]:
#                 print("ID = ", s_name[0])
#                 print("NAME = ", s_name[1])
#                 print("HOMEWORK_NUM = ", s_name[2])
#
#
# if __name__ == '__main__':
#     select = SelectSQL
#     select.name_select
#
# conn = sqlite3.connect('homework.db')
# tab = conn.cursor()
# cur = tab.execute('SELECT * FROM TABINFO;')
# cur_list_id = []
# cur_list_name = []
# cur_list_homework = []
# for c in cur:
#     cur_list_id.append(c[0])
#     cur_list_name.append(c[1])
#     cur_list_homework.append(c[2])
#
#
# def select_sql_all():
#     for c in cur:
#         print("ID = ", c[0])
#         print("NAME = ", c[1])
#         print("HOMEWORK_NUM = ", c[2])
#     conn.close()


def select_sql():
    conn = sqlite3.connect('homework.db')
    tab = conn.cursor()
    cur = tab.execute('SELECT * FROM TABINFO;')
    notice = '''
    请输入查询选项:
    输入1： 查询整个数据库
    输入2： 查询有关姓名
    输入3： 查询有关ID号
    输入4： 查询作业数
    输入0： 退出
    '''
    while True:
        print(notice)
        select_all = input('请选择：')
        if select_all == '0':
            break
        elif select_all == '1':
            for c in cur:
                print("ID = ", c[0])
                print("NAME = ", c[1])
                print("HOMEWORK_NUM = ", c[2])
            conn.close()
            break
        elif select_all == '2':
            id = input('请输入id')
            for c in cur:
                if id == c[0]:
                    print("ID = ", c[0])
                    print("NAME = ", c[1])
                    print("HOMEWORK_NUM = ", c[2])
                else:
                    print(f'id为{id}的作业未查询到')
                conn.close()
            break
        elif select_all == '3':
            name = input('请输入name')
            for c in cur:
                if name == c[1]:
                    print("ID = ", c[0])
                    print("NAME = ", c[1])
                    print("HOMEWORK_NUM = ", c[2])
                else:
                    print(f'姓名为{name}的作业未查询到')
                conn.close()

            break
        elif select_all == '4':
            homework = input('请输入homework')
            for c in cur:
                if homework == c[2]:
                    print("ID = ", c[0])
                    print("NAME = ", c[1])
                    print("HOMEWORK_NUM = ", c[2])
                else:
                    print(f'作业数为{homework}的作业未查询到')
                conn.close()
            break
        else:
            print('输入错误请重试')


if __name__ == '__main__':
    select_sql()



