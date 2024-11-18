# coding=utf-8
# @File: demo1.py
# @Author: zijier
# @Desc: TCP服务端
# @Date: 8:36 PM 2024/03/24
from socket import *

# 1.创建server-socket
server_socket = socket(AF_INET, SOCK_STREAM)

# 2.绑定一个IP和端口
host_port = ('10.113.209.8', 8088)
server_socket.bind(host_port)

# 3.服务器的Socket监听，listen让Socket处于被动，就可以接受客户端的连接请求
# listen(n)表示服务器在拒绝客户端请求之前，允许n个连接请求挂起，n其实就是排队的客户端的数量
server_socket.listen(1)

# 4.等待客户端的连接请求，当前函数是线程阻塞的函数，accept返回两个值，第一个：新的socket
new_socket, client_addr = server_socket.accept()

# 5.服务器接受客户端发送过来的数据，recv一般用于TCP协议的接收数据，recvfrom用于UDP
data = new_socket.recv(1024)
print("服务器端接受的数据是：", data.decode('utf-8'))

# 6.服务器端发送数据给客户
new_socket.send('Thank you!'.encode('utf-8'))

# 7.关闭套接字
# new_socket就意味着当前客户端的服务已经完成
new_socket.close()
# 整个服务器全部关闭
server_socket.close()
