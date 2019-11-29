#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author:郑彬彬
# @date: 2019/9/19 15:43
# github:https://github.com/zhengbinbin

import xlwt

from login import requestJson

from datetime import date

from datetime import timedelta

import time

def get_stemp():
    date_now = (date.today() - timedelta(days=7)).strftime("%Y-%m-%d %H:%M:%S")
    time_array = time.strptime(date_now, "%Y-%m-%d %H:%M:%S")
    time_stamp = int(time.mktime(time_array))
    return time_stamp

def getGroupID(url, auth):
    """获取GroupID"""
    values = {'jsonrpc': '2.0',
              'method': 'hostgroup.get',
              'params': {'output': ["groupid", 'name'],
                         },
              'auth': auth,
              'id': '0'
              }
    output = requestJson(url, values)
    return output

def getKeys(hostid, url, auth):
    """获取所有键值，如vm.memory.size[available],我已知道需要哪些键就不需要次方法，在不知道键值的时候可以先用此方法获取所有键值"""
    values = {'jsonrpc': '2.0',
              'method': 'item.get',
              'params': {
                  'output': ['key_', 'itemid'],
                  'hostids': hostid,
              },
            'auth': auth,
            'id': '0'
    }
    output = requestJson(url, values)
    if len(output) == 0:
        return output
    else:
        print(output)

def writeLExcel(des_list):
    workBook = xlwt.Workbook(encoding='utf-8')
    workSheet = workBook.add_sheet('Windows')
    flag1 = 0
    flag2 = 0
    flag3 = 0
    flag4 = 0
    flag5 = 0
    flag6 = 0
    flag7 = 0
    flag8 = 0
    flag9 = 0
    for i in des_list:
        for dict in i:
            for key, value in dict.items():
                if key == 'hostname':
                    str_new = value.strip(':')
                    workSheet.write(flag1, 0, str_new)
                    flag1 += 1
                elif key == 'ip':
                    workSheet.write(flag2, 1, value)
                    flag2 += 1
                elif key == 'system.cpu.util[,idle]_min':
                    workSheet.write(flag3, 2, str(value) + '%')
                    flag3 += 1
                elif key == 'system.cpu.util[,idle]':
                    workSheet.write(flag4, 3, str(value) + '%')
                    flag4 += 1
                elif key == 'system.cpu.util[,idle]_max':
                    workSheet.write(flag5, 4, str(value) + '%')
                    flag5 += 1
                elif key == 'vm.memory.size[available]_min':
                    workSheet.write(flag6, 5, value)
                    flag6 += 1
                elif key == 'vm.memory.size[available]':
                    workSheet.write(flag7, 6, value)
                    flag7 += 1
                elif key == 'vm.memory.size[available]_max':
                    workSheet.write(flag8, 7, value)
                    flag8 += 1
                else:
                    workSheet.write(flag9, 8, value)
                    flag9 += 1
        workBook.save('E:\\linux.xls')
    print('写入excel成功.')


def writeWExcel(des_list):
    workBook = xlwt.Workbook(encoding='utf-8')
    workSheet = workBook.add_sheet('Windows')
    flag1 = 0
    flag2 = 0
    flag3 = 0
    flag4 = 0
    flag5 = 0
    flag6 = 0
    flag7 = 0
    flag8 = 0
    flag9 = 0
    for i in des_list:
        print(i)
        for dict in i:
            for key, value in dict.items():
                if key == 'hostname':
                    str_new = value.strip(':')
                    workSheet.write(flag1, 0, str_new)
                    flag1 += 1
                elif key == 'ip':
                    workSheet.write(flag2, 1, value)
                    flag2 += 1
                elif key == 'perf_counter[\\Processor(_Total)\\% Processor Time]_min':
                    workSheet.write(flag3, 2, str(value) + '%')
                    flag3 += 1
                elif key == 'perf_counter[\\Processor(_Total)\\% Processor Time]':
                    workSheet.write(flag4, 3, str(value) + '%')
                    flag4 += 1
                elif key == 'perf_counter[\\Processor(_Total)\\% Processor Time]_max':
                    workSheet.write(flag5, 4, str(value) + '%')
                    flag5 += 1
                elif key == 'vm.memory.size[free]_min':
                    workSheet.write(flag6, 5, value)
                    flag6 += 1
                elif key == 'vm.memory.size[free]':
                    workSheet.write(flag7, 6, value)
                    flag7 += 1
                elif key == 'vm.memory.size[free]_max':
                    workSheet.write(flag8, 7, value)
                    flag8 += 1
                else:
                    workSheet.write(flag9, 8, value)
                    flag9 += 1
        workBook.save('E:\\windows.xls')
    print('写入excel成功.')
