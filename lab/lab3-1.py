#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re

mac = '166 54a2.74f7.0326 DYNAMIC Gi1/0/11'

vlanid = re.search('(\d{1,4})',mac)
print('VLAN ID    : ', vlanid.group())

# mac1 = re.search('\s(.*?)\s',mac)
mac1 = re.search('([0-9|a-f]{4}.){2}[0-9|a-f]{4}', mac)
print('MAC        : ', mac1.group())

type = re.search('\w+',mac)
print('Type       : ', type.group())

interface = re.search(r'(\w+/)(\d+)(/\d+)', mac)
print('Interface  : ', interface.group())


# mac_list = re.findall('\s(.*?)\s',mac)
# for m in mac_list:
#     print('MAC        :',m)
#
# type_list = re.findall('[D].*[C]',mac)
# for t in type_list:
#     print('Type       :',t)
#
# Interface_list = re.findall('[G].*',mac)
# for interface in Interface_list:
#     print('Interface  :',interface)
