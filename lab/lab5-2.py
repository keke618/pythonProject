#!/usr/bin/python3.8
# -*- coding: UTF-8 -*-
# @Time : 2021/9/22 8:19 
# @Author : keke618
# @File : lab5-2.py 
# @Software: PyCharm
import requests
from pprint import pprint

if __name__ == '__main__':
    headers ={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
    }
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=pid'
    data = {
        'cname':'武汉',
        'pid':'20',
        'pageIndex':'1',
        'pageSize':'10'
    }
    res = requests.post(url=url, headers=headers, data=data).json()
    # print(res.json())
    pprint(res)
    kfc = res['Table1']
    for dic in kfc:
        if '点唱机' in dic['pro']:
            print(dic['addressDetail'])
