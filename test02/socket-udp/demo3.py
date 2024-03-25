# coding=utf-8
# @File: demo3.py
# @Author: zijier
# @Desc: UDP服务端
# @Date: 8:39 PM 2024/03/23

from socket import *

# 1.创建一个服务端的socket
socket_server = socket(AF_INET, SOCK_DGRAM)

# 2.定义服务器端的IP地址和端口号
host_post = ('192.168.137.1', 8090)

# 3.服务器端的socket来绑定地址和端口，只有绑定了地址和端口才能称为服务器端的socket
socket_server.bind(host_post)

# 4.接受客户端发过来的数据，每次接受1kb的数据，最大接受一次接受64kb的数据，收到的每一个数据报里面是一个元组，第一个值是数据内容，第二个值是源地址
data = socket_server.recvfrom(1024)
print(data[0].decode('utf-8'))

# 5.关闭套接字，释放资源
socket_server.close()
