#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author:郑彬彬
# @date: 2019/9/10 16:38
# github:https://github.com/zhengbinbin
from login import requestJson

def getWHosts(url, auth):
    """通过GroupID获得机器ip和name"""
    windows_list = []
    dict_group = {'windows': 9}
    for key, value in dict_group.items():
        values = {'jsonrpc': '2.0',
                  'method': 'host.get',
                  'params': {'output': ["host", 'name'],
                             'groupids':value
                             },
                  'auth': auth,
                  'id': '0'
                  }
        output = requestJson(url, values)
        for i in output:
            host = {'name': i['name'], 'host': i['host']}
            windows_list.append(host)
    return windows_list

def getWHostid(ip, url, auth):
    values = {'jsonrpc': '2.0',
              'method': 'host.get',
              'params': {'output': ["name", 'ip'],
                         'filter': {
                             'ip': ip
                         },
                    },
              'auth': auth,
              'id': '0'
            }
    output = requestJson(url, values)
    if output == None:
        print('没有该主机！')
        return output
    else:
        hostid = output[0]['hostid']
        return hostid

def getWItemids(hostid, url, auth):
    """该方法为获取windows主机的itemid"""
    dict_items = {}
    dict_keys = ['perf_counter[\Processor(_Total)\% Processor Time]', 'vm.memory.size[free]', 'vm.memory.size[total]']
    for key in dict_keys:
        values = {'jsonrpc': '2.0',
                  'method': 'item.get',
                  'params': {
                      'output': ['itemid'],
                      'hostids': hostid,
                  'filter': {
                      'key_': key,
                        },
                  },
                'auth': auth,
                'id': '0'
        }
        output = requestJson(url, values)
        if output == None:
            return output
        else:
            dict_tmp = {key: output[0]['itemid']}
            dict_items.update(dict_tmp)
    return dict_items


def getWValue(dict_items, url, auth, time_from):
    mac_info = []
    for key, value in dict_items.items():
        if key == 'perf_counter[\Processor(_Total)\% Processor Time]':
            values = {'jsonrpc': '2.0',
                      'method': 'history.get',
                      'params': {
                          #'output': ['extend'],
                          'history': 0,
                          'itemids': value,
                          'sortorder': 'DESC',
                          'time_from': time_from,
                          #'limit': 1
                      },
                      'auth': auth,
                      'id': 0
            }
        elif key == 'vm.memory.size[total]':
            values = {'jsonrpc': '2.0',
                      'method': 'history.get',
                      'params': {
                          #'output': ['extend'],
                          'history': 3,
                          'itemids': value,
                          #'time_from': 1567526400,
                          'limit': 1
                      },
                      'auth': auth,
                      'id': 0
                      }
        else:
            values = {'jsonrpc': '2.0',
                      'method': 'history.get',
                      'params': {
                          # 'output': ['extend'],
                          'history': 3,
                          'itemids': value,
                          'sortorder': 'DESC',
                          'time_from': time_from,
                          #'limit': 1
                      },
                      'auth': auth,
                      'id': 0
                      }
        output = requestJson(url, values)
        #print(output)
        if output == None:
            print('请求异常，跳过这个ip')
        else:
            values_tmp = 0
            max = 0
            min = float(output[0]['value'])
            for i in range(len(output)):
                float(output[i]['value'])
                if float(output[i]['value']) > max:
                    max = float(output[i]['value'])
                if float(output[i]['value']) < min:
                    min = float(output[i]['value'])
                values_tmp = values_tmp + float(output[i]['value'])
            values_tmp = round(values_tmp / len(output), 2)
            value_tmp = {key: values_tmp}
            value_max = {key + '_max': max}
            value_min = {key + '_min': min}
            if key == 'vm.memory.size[total]':
                mac_info.append(value_tmp)
            else:
                mac_info.append(value_tmp)
                mac_info.append(value_max)
                mac_info.append(value_min)
    return mac_info

def getWResult(mac_info):
    for i in mac_info:
        for key, value in i.items():
            if key == 'perf_counter[\\Processor(_Total)\\% Processor Time]':
                value_new = round(value, 2)
                i[key] = value_new
            elif key == 'perf_counter[\\Processor(_Total)\\% Processor Time]_max':
                round(value, 2)
                value_new = round(value, 2)
                i[key] = value_new
            elif key == 'perf_counter[\\Processor(_Total)\\% Processor Time]_min':
                round(value, 2)
                value_new = round(value, 2)
                i[key] = value_new
            else:
                value_new = round(value / 1024 / 1024 / 1024, 2)
                i[key] = value_new
    return mac_info