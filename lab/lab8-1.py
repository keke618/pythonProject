# # !/usr/bin/python3.8.6
# # -*- coding=utf-8 -*-
# from http.server import CGIHTTPRequestHandler,HTTPServer

import re
import os

netstat = os.popen("netstat -tulnp").read()
print(netstat)
httpd_port = re.search('(:[8][0])', netstat)
port = ':80'
print(httpd_port)
# while httpd_port != 80:
#     print('等待一秒重新检测')
#     if httpd_port.group() == port:
#         print('http(tcp/80)服务已打开')
#         break



