# coding=utf-8
# @File: demo2.py
# @Author: zijier
# @Desc: TCP客户端
# @Date: 8:52 PM 2024/03/24
from socket import *

client_socket = socket(AF_INET, SOCK_STREAM)
# 客户端发送连接的请求（不是传输数据）

# 目标服务器的IP和端口
server_ip_port = ('10.113.209.8', 8088)
client_socket.connect(server_ip_port)

send_data = input("请输入：")
client_socket.send(send_data.encode('utf-8'))

# 接受服务器返回的数据
recv_data = client_socket.recv(1024)

print("客户端接受的服务器的数据为：", recv_data.decode('utf-8'))