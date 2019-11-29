#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @author 郑彬彬
# @{DATE}
# github：https://github.com/zhengbinbin
# 下面的linux机器信息获取和windows机器信息获取需要分开进行，即执行linux机器信息获取时注释掉windows机器信息获取
import time
from login import *

from linux import *

from windows import *

from common import *


#登录zabbix获取auth
auth = authenticate(url, username, passwd)

# dict = getGroupID(url, auth)  #获取所有的groupID

# 这是linux机器获取cpu信息和内存的方法
#测试用例
#list = [{'name': '指数solr集群3:', 'host': '10.80.58.101'}, {'name': 'solrc1003:', 'host': '10.80.112.79'}, {'name': '中台预分析服务1:', 'host': '10.111.2.78'}, {'name': '舆情数据分析同步服务器3:', 'host': '10.168.117.27'}]
# list = getLHosts(url, auth)  #根据groupid获取所有linux机器nama和ip
#
# desL_list = []
# time_from = get_stemp()
# for i in list:
#     ip = i['host']
#     hostname = i['name']
#     dict1 = {'hostname': hostname}
#     dict2 = {'ip': ip}
#     hostid = getLHostid(ip, url, auth)
#     dict_items = getLItemids(hostid, url, auth)
#     mac_info = getLValue(dict_items, url, auth, time_from)
#     mac_info = getLResult(mac_info)
#     mac_info.append(dict1)
#     mac_info.append(dict2)
#     print(mac_info)
#     desL_list.append(mac_info)
# print(desL_list)
# writeLExcel(desL_list)

# 这是windows机器获取cpu信息和内存的方法
list = getWHosts(url, auth)  #根据groupid获取所有windows的机器nama和ip
desW_list = []
time_from = get_stemp()
for i in list:
    ip = i['host']
    hostname = i['name']
    dict1 = {'hostname': hostname}
    dict2 = {'ip': ip}
    hostid = getWHostid(ip, url, auth)
    dict_items = getWItemids(hostid, url, auth)
    mac_info = getWValue(dict_items, url, auth, time_from)
    mac_info = getWResult(mac_info)
    mac_info.append(dict1)
    mac_info.append(dict2)
    print(mac_info)
    desW_list.append(mac_info)
writeWExcel(desW_list)

#测试方法
# ip = '10.80.58.101'
# hostid = getLHostid(ip, url, auth)
# dict_items = getLItemids(hostid, url, auth)
# mac_info = getLValue(dict_items, url, auth, time_from)
# print(mac_info)