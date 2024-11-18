# coding=utf-8
# @File: demo4.py
# @Author: zijier
# @Desc: UDP-echo客户端
# @Date: 8:55 PM 2024/03/23
from socket import *

'''
需求：
1.客户端发送多条数据
2.客户端如果发送一个‘exit’则客户端退出
3.服务端收到什么就返回什么
'''

flag = True
# 1.创建一个套接字
client_socket = socket(AF_INET, SOCK_DGRAM)

while flag:

    # 2.定义一个接受消息的目标，8080是目标服务器的端口，127.0.0.1是目标服务器的地址
    server_host_port = ('192.168.137.1', 8090)

    # 3.准备发送数据，encode表示按照一种编码格式把数据变成字节数组bytes
    datas = input("请输入：").encode("utf-8")

    # 4.发送数据
    client_socket.sendto(datas, server_host_port)
    # 一定可以从服务器收到返回的数据，打印服务器返回的数据
    print("返回的数据是：", client_socket.recvfrom(1024)[0].decode('utf-8'))

    if ('exit' == datas.decode('utf-8')):
        flag = False

# 5.关闭套接字，其实就是释放了系统资源
client_socket.close()
