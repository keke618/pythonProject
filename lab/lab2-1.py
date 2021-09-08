#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random

part1 = random.randint(0,255)
part2 = random.randint(0,255)
part3 = random.randint(0,255)
part4 = random.randint(0,255)

ipadd = f"{part1}.{part2}.{part3}.{part4}"

print("生成的随机IP地址是：",ipadd)

