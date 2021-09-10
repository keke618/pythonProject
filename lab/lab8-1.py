# !/usr/bin/python3.8.6
# -*- coding=utf-8 -*-
# from CGIHTTPRequestHandler import HTTPServer
# port = 80
# httpd = HTTPServer(('',port), CGIHTTPRequestHandler)
# print('Starting simple httpd on port: ' + str(httpd.server_port))
# httpd.serve_forever()
import re
import os

netstat = os.popen("netstat -tulnp").read()
print(netstat)
httpd_port = re.search('(:[8][0])', netstat)
port = ':80'
while httpd_port != 80:
    print('等待一秒重新检测')
    if httpd_port.group() == port:
        print('http(tcp/80)服务已打开')
        break
