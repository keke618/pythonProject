#!/usr/bin/python3.8
# -*- coding: UTF-8 -*-
# @Time : 2021/9/23 8:34 
# @Author : keke618
# @File : get_kfc.py 
# @Software: PyCharm
import requests
import pprint
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/87.0.4280.141 Safari/537.36 '
}
url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'

for i in range(1, 21):
    data = {
        'cname': '武汉',
        'pid': '',
        'pageIndex': i,
        'pageSize': '10'
    }
    res = requests.post(url=url, data=data, headers=headers).json()
    # pp = pprint.PrettyPrinter(indent=2, width=80)
    with open('get_kfc.json', 'a') as f:
        # print(pp.pformat(res), file=f)
        print(res, file=f)

