# coding=utf-8
# @File: demo5.py
# @Author: zijier
# @Desc: UDP-echo
# @Date: 9:05 PM 2024/03/23


from socket import *

# 1.创建一个服务端的socket
socket_server = socket(AF_INET, SOCK_DGRAM)

# 2.定义服务器端的IP地址和端口号
host_post = ('', 8090)  # 如果服务器是真实的物理小型服务器，IP地址有很多。任何本机的IP地址都绑定只用''

# 3.服务器端的socket来绑定地址和端口，只有绑定了地址和端口才能称为服务器端的socket
socket_server.bind(host_post)

while True:
    # 4.接受客户端发过来的数据，每次接受1kb的数据，收到的每一个数据报里面是一个元组，第一个值是数据内容，第二个值是源地址
    data = socket_server.recvfrom(1024)
    # 服务器收到数据后原封不动的返回，而且收到哪个客户端的信息就返回给那个客户端
    socket_server.sendto(data[0], data[1])
    print(data[0].decode('utf-8'))

# 5.关闭套接字，释放资源
# socket_server.close()