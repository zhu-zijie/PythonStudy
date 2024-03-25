# coding=utf-8
# @File: demo2.py
# @Author: zijier
# @Desc: TFTP客户端
# @Date: 9:42 PM 2024/03/23
from socket import *
import struct  # 处理python数据结构和c语言数据结构转换

file_name = input("请输入要下载的文件名：")

# 客户端的socket
s = socket(AF_INET, SOCK_DGRAM)

# 定义目标服务器的地址和端口号
host_post = ('192.168.137.1', 69)
# !H%dsb5sb 代表格式：!代表开头
data_package = struct.pack('!H%dsb5sb' % len(file_name), 1, file_name.encode('utf-8'), 0, 'octet'.encode('utf-8'), 0)

# 把数据发到目标服务器
s.sendto(data_package, host_post)

# 客户端首先创建一个空白的文件
f = open('client_' + file_name, 'ab')

while True:
    # 客户端接受从服务器发过来的数据，数据有两种：1.下载文件内容数据报，2.error信息报
    receive_data, (server_ip, server_port) = s.recvfrom(1024)
    # 把前4个字节的数据包解析出来
    operator_code, num = struct.unpack('!HH', receive_data[:4])
    if int(operator_code) == 5:  # 判断数据包是否是error信息报
        print("服务器返回：您要下载的文件不存在！")
        break
    # 如果是文件内容的数据，需要保存文件内容
    f.write(receive_data[4:])

    # 保护性代码，意味着服务器传输过来的文件已经接收完成了
    if len(receive_data) < 516:
        print("客户端下载完毕！")
        break

    # 客户端收到数据包之后，还需要发送一个确认ACK给服务器
    ack_package = struct.pack('!HH', 4, num)
    s.sendto(ack_package, (server_ip, server_port))

f.close()
s.close()
