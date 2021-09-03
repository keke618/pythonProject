# import os
# os.mkdir('test')
# os.chdir('test')
# f1 = open('aaa','w')
# f1.write('I love Networking !\n')
# f1.write('I am teacher yin!')
# f1.close()
#
# f2 = open('bbb', 'w')
# f2.write('I love playing !\n')
# f2.close()
#
# f3 = open('ccc','w')
# f3.write('I love Python and Networking \n')
# f3.write('I am super learner !')
# f3.close()
#
# os.mkdir('Networking')

import os


def find_file_name():
    file_name_list = []
    for file_path , file_dir , file_files in os.walk(os.getcwd()):
        for name in file_files:
            file_name_list.append(name)
    return file_name_list


def search_content(file_list):
    key = 'Networking'
    for file in file_list:
        with open(file , 'r', encoding='utf-8') as f:
            if key in f.read():
                print(file)


if __name__ == '__main__':
    os.chdir('test')
    print('文件中包含"Networking"关键字的文件为：')
    # print(find_file_name())
    search_content(find_file_name())



