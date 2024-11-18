# coding=utf-8
# @File: demo13.py
# @Author: zijier
# @Desc: 
# @Date: 8:22 PM 2024/03/15
import time


def show_info():
    print("请输入提示数字，执行相应的操作：0.退出 1.查看登录日志")


def read_logininfo():
    with open(file="login.txt", mode='r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if line == '':
                break
            else:
                print(line, end='')


def write_logininfo(username):
    print(username)
    with open(file="login.txt", mode='a', encoding='utf-8') as file:
        s = f"用户名；{username}, 登陆时间：{time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))}"
        file.write(s)
        file.write('\n')


if __name__ == '__main__':
    username = input("请输入用户名：")
    pwd = input("请输入密码：")
    if "admin" == username and "admin" == pwd:
        print("登陆成功！！！")
        write_logininfo(username)
        show_info()
        num = int(input("请输入操作数字："))
        while True:
            if num == 0:
                print("退出成功！！！")
                break
            elif num == 1:
                print("查看日志！！！")
                read_logininfo()
                num = int(input("请输入操作数字："))
            else:
                print("您输入的数字错误！！！")
                show_info()
                num = int(input("请输入操作数字："))
    else:
        print("登陆的用户名或密码错误！！！")
