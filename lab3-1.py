#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re

mac = '166 54a2.74f7.0326 DYNAMIC Gi1/0/11'

vlanid_list = re.findall('166',mac)

for vlanid in vlanid_list:
    print('VLAN ID    :',vlanid)

mac_list = re.findall('\s(.*?)\s',mac)
for m in mac_list:
    print('MAC        :',m)

type_list = re.findall('[D].*[C]',mac)
for t in type_list:
    print('Type       :',t)

Interface_list = re.findall('[G].*',mac)
for interface in Interface_list:
    print('Interface  :',interface)