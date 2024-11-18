# coding=utf-8
# @File: demo1.py
# @Author: zijier
# @Desc: TFTP服务端
# @Date: 9:35 PM 2024/03/23
from socket import *
import struct

# 服务器端的socket
s = socket(AF_INET, SOCK_DGRAM)

# 绑定IP和端口
s.bind(('192.168.137.1', 69))


def download(filename, client_ip, client_port):
    # 创建一个新的socket，负责发送文件内容的数据包到客户端
    new_socket = socket(AF_INET, SOCK_DGRAM)
    # 文件内容数据包的计数器
    num = 1
    # 定义服务客户端退出的标签
    flag = True
    try:
        f = open(filename, 'rb')
    except:
        # H表示python的Integer转成c的没有字符的short
        error_package = struct.pack('!HH5sb', 5, 5, 'error'.encode('utf-8'), 0)
        new_socket.sendto(error_package, (client_ip, client_port))
        # exit()  # 退出服务器
        flag = False
        print("该用户要下载的文件不存在！")

    # 如果文件存在，那么需要把文件的内容切成一个个的数据包发送给客户端，一个数据包包含的数据内容为512字节
    while flag:
        # 从文件内容中读取512字节的内容
        read_data = f.read(512)
        # 创建一个数据报
        data_package = struct.pack('!HH', 3, num) + read_data
        # 发送数据包
        new_socket.sendto(data_package, (client_ip, client_port))
        if len(read_data) < 512:
            print(f"客户端{client_ip}文件下载完成！")
            break
        # 服务器接受ACK的确认数据
        receive_ack = new_socket.recvfrom(1024)
        operator_code, ack_num = struct.unpack('!HH', receive_ack[0])
        print(f"客户端{client_ip}的确认信息是{ack_num}")
        num += 1
        # 保护性代码
        if int(operator_code) != 4 or int(ack_num) < 1:
            break
    new_socket.close()


def server():
    while True:
        # 服务器等着客户端发送过来的数据，然后等着接收
        receive_data, (client_ip, client_port) = s.recvfrom(1024)
        print(receive_data, client_ip, client_port)
        # 判断数据包是否是：客户端请求的数据包
        if struct.unpack('!b5sb', receive_data[-7:]) == (0, b'octet', 0):
            # 得到操作码的值
            operator_code = struct.unpack('!H', receive_data[:2])
            # 得到文件名
            file_name = receive_data[2:-7].decode('utf-8')
            if operator_code[0] == 1:
                print("客户端想下载：%s" % file_name)
                download(file_name, client_ip, client_port)


if __name__ == '__main__':
    server()
