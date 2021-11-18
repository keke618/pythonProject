# # result = 1 + 2
# # print("计算结果为：", result)
# #
# #
# # # a = [x for x in list1 if x in list2]  # 两个列表表都存在
# # # b = [y for y in (list1 + list2) if y not in a]  # 两个列表中的不同元素
# # # c = [x for x in list1 if x not in list2]  # 在list1列表中而不在list2列表中
# # # d = [y for y in list2 if y not in list1]  # 在list2列表中而不在list1列表中
# #
# # class Person:
# #     def __init__(self,name,age,sex):
# #         self.name = name
# #         self.age = age
# #         self.sex = sex
# #         self.partner = None # 另一半，是个对象
# #
# #
# #     def do_private_stuff(self):
# #         """和男/女盆友干点羞羞的事"""
# #         print("%s is doing %s in the 7th hotel." %(self.name,self.partner.name))
# #
# #
# # p1 = Person("武大郎",25,"男")
# # p2 = Person("黑姑娘",23,"女")
# # p1.partner = p2 # 两个对象要互相绑定彼此
# # p2.partner = p1
# # p1.do_private_stuff()
# # p2.do_private_stuff()
#
# class ShenXianBase:
#     def fight(self):
#         print("神仙祖宗在打架....")
#
# class MonkeyBase:
#     def fight(self):
#         print("猿猴在打架....")
#
# class ShenXian(ShenXianBase):
#     """神仙类"""
#     def fly(self):
#         print("神仙都会飞...")
#     #def fight(self):
#     #    print("神仙在打架...")
#
# class Monkey(MonkeyBase):
#     def eat_peach(self):
#         print("猴子都喜欢吃桃子...")
#
#     def fight(self):
#         print("猴子在打架...")
#
# class MonkeyKing(ShenXian,Monkey):
#     def play_goden_stick(self):
#         print("孙悟空玩金箍棒...")
#
#
# sxz = MonkeyKing()
# sxz.fight()
import re
info = '''
<sw1>dis cu
#
sysname sw1
#
vlan batch 10 20 30 40 50 100
#
cluster enable
ntdp enable
ndp enable
#
undo nap slave enable
#
drop illegal-mac alarm
#
dhcp enable
#
diffserv domain default
#
drop-profile default
#
aaa
authentication-scheme default
authorization-scheme default
accounting-scheme default
domain default
domain default_admin
local-user admin password cipher #*C>*$C`S!INZPO3JBXBHA!!
local-user admin privilege level 15
local-user admin service-type telnet
#
interface Vlanif1
#
interface Vlanif10
ip address 192.168.10.1 255.255.255.0
dhcp select interface
dhcp server dns-list 1.1.1.1
#
interface Vlanif20
ip address 192.168.20.1 255.255.255.0
dhcp select interface
dhcp server dns-list 1.1.1.1
#
interface Vlanif30
ip address 192.168.30.1 255.255.255.0
dhcp select interface
dhcp server dns-list 1.1.1.1
#
interface Vlanif40
ip address 192.168.40.1 255.255.255.0
dhcp select interface
dhcp server dns-list 1.1.1.1
#
interface Vlanif50
ip address 192.168.50.1 255.255.255.0
dhcp select interface
dhcp server dns-list 1.1.1.1
#
interface Vlanif100
ip address 10.10.10.1 255.255.255.0
#
interface MEth0/0/1
#
interface GigabitEthernet0/0/1
port link-type trunk
port trunk allow-pass vlan 2 to 4094
#
interface GigabitEthernet0/0/2
port link-type trunk
port trunk allow-pass vlan 2 to 4094
#
interface GigabitEthernet0/0/3
port link-type trunk
port trunk allow-pass vlan 2 to 4094
#
interface GigabitEthernet0/0/4
port link-type trunk
port trunk allow-pass vlan 2 to 4094
#
interface GigabitEthernet0/0/5
port link-type trunk
port trunk allow-pass vlan 2 to 4094
#
interface GigabitEthernet0/0/6
#
interface GigabitEthernet0/0/7
#
interface GigabitEthernet0/0/8
#
interface GigabitEthernet0/0/9
#
interface GigabitEthernet0/0/10
#
interface GigabitEthernet0/0/11
#
interface GigabitEthernet0/0/12
#
interface GigabitEthernet0/0/13
#
interface GigabitEthernet0/0/14
#
interface GigabitEthernet0/0/15
#
interface GigabitEthernet0/0/16
#
interface GigabitEthernet0/0/17
#
interface GigabitEthernet0/0/18
#
interface GigabitEthernet0/0/19
#
interface GigabitEthernet0/0/20
#
interface GigabitEthernet0/0/21
#
interface GigabitEthernet0/0/22
#
interface GigabitEthernet0/0/23
#
interface GigabitEthernet0/0/24
port link-type trunk
port trunk allow-pass vlan 2 to 4094
#
interface NULL0
#
user-interface con 0
user-interface vty 0 4
authentication-mode aaa
protocol inbound all
#
return
<sw1>
'''

test = re.findall(r'(<sw1>dis cu\n#\n)(.*)(<sw1>)', info, re.S)[0][1]
print(test[0][1])