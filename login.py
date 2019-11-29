#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author:郑彬彬
# @date: 2019/9/10 15:07
# github:https://github.com/zhengbinbin

import json
import urllib.request, urllib.parse
url = 'http://10.51.18.252/zabbix/api_jsonrpc.php'
username = 'zhengbinbin'
passwd = 'IwtOv99lEab4GoSj'

#定义通过http方式访问API地址函数
def requestJson(url, values):
    data = json.dumps(values).encode()
    req = urllib.request.Request(url, data, {'Content-Type': 'application/json-rpc'})
    try:

        response = urllib.request.urlopen(req, data)
        output = json.loads(response.read())
        message = output['result']
        #print(message)
    except Exception as e:
        response = urllib.request.urlopen(req, data)
        output = json.loads(response.read())
        message = output['result']

    return message

#API接口认证函数，登陆成功会返回一个Token
def authenticate(url, username, passwd):
    values = {'jsonrpc': '2.0',
              'method': 'user.login',
              'params': {
                  'user': username,
                  'password': passwd
              },
              'id': '0'
              }
    idvalve = requestJson(url, values)
    return idvalve

if __name__ == '__main__':
    authenticate(url, username, passwd)
