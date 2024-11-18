# coding=utf-8
# @File: demo12.py
# @Author: zijier
# @Desc: 
# @Date: 4:15 PM 2024/03/15

# 推断日期

import datetime


def inputdate():
    indate = input("请输入开始日期：（20200101）").strip()
    datestr = indate[0:4] + '-' + indate[4:6] + '-' + indate[6:]
    return datetime.datetime.strptime(datestr, '%Y-%m-%d')


if __name__ == '__main__':
    print("----------推断几天后的时间----------")
    date = inputdate()
    num = int(input("请输入间隔天数："))
    date += datetime.timedelta(days=num)
    print("您推断的日期是：" + str(date).split(' ')[0])
