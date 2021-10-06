# # !/usr/bin/python3.8.6
# # -*- coding=utf-8 -*-
# from http.server import CGIHTTPRequestHandler,HTTPServer

import os
from time import sleep


while True:
    netstat = os.popen("netstat -tulnp | grep '80' | grep tcp").read()
    if '80' not in netstat:
        print('等待一秒重新开始监控')
        sleep(1)
    if '80' in netstat:
        print('HTTP(TCP/80)服务已打开')
        break



