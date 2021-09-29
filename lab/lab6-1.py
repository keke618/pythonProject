#!/usr/bin/python
# -*- coding: UTF-8 -*-
# import os
# os.mkdir('test')
# os.chdir('test')
# f1 = open('aaa', 'w')
# f1.write('I love Networking !\n')
# f1.write('I am teacher yin!')
# f1.close()
#
# f2 = open('bbb', 'w')
# f2.write('I love playing !\n')
# f2.close()
#
# f3 = open('ccc', 'w')
# f3.write('I love Python and Networking \n')
# f3.write('I am super learner !')
# f3.close()
#
# os.mkdir('Networking')

import os


def find_file_name():
    file_name_list = []
    for file_path, file_dir, file_files in os.walk(os.getcwd()):
        for name in file_files:
            file_name_list.append(name)
    return file_name_list


def search_content(file_list):
    key = 'Networking'
    for file in file_list:
        with open(file, 'r', encoding='utf-8') as f:
            if key in f.read():
                print(file)


if __name__ == '__main__':
    os.chdir('test')
    print('文件中包含"Networking"关键字的文件为：')
    # print(find_file_name())
    search_content(find_file_name())


# import os
# print('文件中包含"Networking"的文件：')
# os.chdir('test')
# key = "Networking"
# for file_dir in os.listdir(os.getcwd()):    # 遍历得到当前路径下所有文件的文件名
#     path_f = os.path.abspath(file_dir)      # 获得这些文件的绝对路径
#     if os.path.isfile(path_f):              # 判断是否时文件 不是则跳过
#         with open(file_dir, 'r', encoding='utf-8') as f:
#             if key in f.read():
#                 print(file_dir)
#         # f = open(file=file_dir, mode='r')   # 打开文件 只读
#         # if key in f.read():                 # 如果文件里面有networking 则打印文件名
#         #     print(file_dir)
#         # f.close()                           # 关闭文件


