# result = 1 + 2
# print("计算结果为：", result)
#
#
# # a = [x for x in list1 if x in list2]  # 两个列表表都存在
# # b = [y for y in (list1 + list2) if y not in a]  # 两个列表中的不同元素
# # c = [x for x in list1 if x not in list2]  # 在list1列表中而不在list2列表中
# # d = [y for y in list2 if y not in list1]  # 在list2列表中而不在list1列表中
#
# class Person:
#     def __init__(self,name,age,sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#         self.partner = None # 另一半，是个对象
#
#
#     def do_private_stuff(self):
#         """和男/女盆友干点羞羞的事"""
#         print("%s is doing %s in the 7th hotel." %(self.name,self.partner.name))
#
#
# p1 = Person("武大郎",25,"男")
# p2 = Person("黑姑娘",23,"女")
# p1.partner = p2 # 两个对象要互相绑定彼此
# p2.partner = p1
# p1.do_private_stuff()
# p2.do_private_stuff()

class ShenXianBase:
    def fight(self):
        print("神仙祖宗在打架....")

class MonkeyBase:
    def fight(self):
        print("猿猴在打架....")

class ShenXian(ShenXianBase):
    """神仙类"""
    def fly(self):
        print("神仙都会飞...")
    #def fight(self):
    #    print("神仙在打架...")

class Monkey(MonkeyBase):
    def eat_peach(self):
        print("猴子都喜欢吃桃子...")

    def fight(self):
        print("猴子在打架...")

class MonkeyKing(ShenXian,Monkey):
    def play_goden_stick(self):
        print("孙悟空玩金箍棒...")


sxz = MonkeyKing()
sxz.fight()
