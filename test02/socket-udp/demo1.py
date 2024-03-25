# coding=utf-8
# @File: demo1.py
# @Author: zijier
# @Desc: 
# @Date: 7:33 PM 2024/03/23

import socket

# 创建套接字(Socket)TCP协议
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 创建套接字(Socket)UDP协议
s2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print(s1)
