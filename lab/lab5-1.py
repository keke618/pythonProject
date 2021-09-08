#!/usr/bin/python
# -*- coding: UTF-8 -*-
asa_conn = "TCP Student 192.168.189.167:32806 Teacher 137.78.5.128:65247 , idle 0:00:00, bytes 74 , flags UIO\n TCP Student 192.168.189.167:80 Teacher 137.78.5.128:65233 , idle 0:00:03, bytes 334516 , flags UIO"
asa_dir = {}
# 将字符串分割为需要的两组数据
asa_list = asa_conn.split('\n')
asa_list1 = asa_list[0].split(' ')
asa_list2 = asa_list[1].split(' ')

# 将对应数据所在列表位置获取
student_num = asa_list1.index('Student') + 1
teacher_num = asa_list1.index('Teacher') + 1
bytes_num = asa_list1.index('bytes') + 1
flags_str = asa_list1.index('flags') + 1

student_num2 = asa_list2.index('Student') + 1
teacher_num2 = asa_list2.index('Teacher') + 1
bytes_num2 = asa_list2.index('bytes') + 1
flags_str2 = asa_list2.index('flags') + 1

# 处理IP和端口结合的数据
student_list = asa_list1[student_num].split(':')
teacher_list = asa_list1[teacher_num].split(':')

student_list2 = asa_list2[student_num2].split(':')
teacher_list2 = asa_list2[teacher_num2].split(':')

# 将数据导入字典
asa_dir[(student_list[0], student_list[1], teacher_list[0], teacher_list[1])] = (asa_list1[bytes_num], asa_list1[flags_str])
asa_dir[(student_list2[0], student_list2[1], teacher_list2[0], teacher_list2[1])] = (asa_list2[bytes_num2], asa_list2[flags_str2])
print('分析后的字典为：')
print(asa_dir)

# 数据格式化打印
info = f'''
格式化输出如下：
    src : {student_list[0]:20}  |    src_p : {student_list[1]:10}  |    dst : {teacher_list[0]:20}  |    dsp_t : {teacher_list[1]}
  bytes : {asa_list1[bytes_num]:20}  |    flags : {asa_list1[flags_str]}
==================================================================================================================================
    src : {student_list2[0]:20}  |    src_p : {student_list2[1]:10}  |    dst : {teacher_list2[0]:20}  |    dsp_t : {teacher_list2[1]}
  bytes : {asa_list2[bytes_num2]:20}  |    flags : {asa_list2[flags_str2]}
==================================================================================================================================
'''
print(info)
# print(asa_list1)
# print(asa_list2)


