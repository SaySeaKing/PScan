# -*- coding:utf-8 -*-

import nmap
import time

# nm = nmap.PortScanner()

#ret = nm.scan(hosts='219.143.234.0/24', arguments='-sP')

#for key in ret['scan'].keys():
#    print key
start = time.time()
ip_list = []
ip = ''
file = open('input/ip_list.txt')
for line in file.readlines():
    line = line.replace('{', '')
    line = line.replace('}', '')
    line = line.replace('ip','')
    line = line.replace('""','')
    line = line.replace(':','')
    line = line.replace('\n','')
    ip_list.append(line)
print ip_list
for i in ip_list:
    print i
    # ip += str(line) +' '
# ret = nm.scan(hosts='219.143.234.234', arguments='-sS -p 1-65535')
# print ret
end = time.time()
print end-start

