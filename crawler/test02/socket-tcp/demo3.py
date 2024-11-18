# coding=utf-8
# @File: demo3.py
# @Author: zijier
# @Desc: TCP-qq聊天服务端
# @Date: 9:19 PM 2024/03/24

from socket import *

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('10.113.209.8', 8008))
server_socket.listen(1)

while True:
    new_socket, client_ip_port = server_socket.accept()

    while True:
        recv_data = new_socket.recv(1024)
        if len(recv_data) > 0:
            print("客户端：", recv_data.decode('utf-8'))
        if recv_data.decode('utf-8') == 'exit':
            print("客户端已经退出！")
            break

        # 发送数据给客户端
        send_data = input("send:")
        if len(send_data) > 0:
            new_socket.send(send_data.encode('utf-8'))
    new_socket.close()

