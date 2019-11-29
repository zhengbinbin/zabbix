#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author:郑彬彬
# @date: 2019/11/18 10:22
# github:https://github.com/zhengbinbin

from datetime import date
from datetime import timedelta
import time

def get_stemp():
    date_now = (date.today() - timedelta(days=7)).strftime("%Y-%m-%d %H:%M:%S")
    time_array = time.strptime(date_now, "%Y-%m-%d %H:%M:%S")
    time_stamp = int(time.mktime(time_array))
    return time_stamp

get_stemp()
