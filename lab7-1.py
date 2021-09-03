import os
import re
route_result = os.popen("route -n").read()
# print(route_result)
ip = re.findall('\s(\d.*?\d)\s', route_result)
gateway = ip[1]
print('网关为：', gateway)