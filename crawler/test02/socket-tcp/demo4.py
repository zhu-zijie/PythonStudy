# coding=utf-8
# @File: demo4.py
# @Author: zijier
# @Desc: TCP-qq聊天客户端
# @Date: 9:28 PM 2024/03/24

from socket import *

client_socket = socket(AF_INET, SOCK_STREAM)

client_socket.connect(('10.113.209.8', 8008))

while True:
    send_data = input("send:")

    if len(send_data) > 0:
        client_socket.send(send_data.encode('utf-8'))
    if send_data == 'exit':
        client_socket.close()
        break

    # 客户端接受服务器返回的数据
    recv_data = client_socket.recv(1024)
    print("服务器：", recv_data.decode('utf-8'))

client_socket.close()
