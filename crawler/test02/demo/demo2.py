# coding=utf-8
# @File: demo2.py
# @Author: zijier
# @Desc: 聊天室服务端
# @Date: 20:34 2024/04/13
import threading
import time

import wx
from socket import *


class Server(wx.Frame):
    def __init__(self):
        # 调用父类的初始化函数
        wx.Frame.__init__(self, None, id=101, title="子杰的聊天服务端", pos=wx.DefaultPosition, size=(400, 470))
        p1 = wx.Panel(self)  # 在窗口中初始化一个面板
        # 在面板中放一些按钮，文本框，文本输入框，将这些对象统一放进一个盒子里
        box = wx.BoxSizer(wx.VERTICAL)  # 在盒子里面垂直方向自动排版
        g1 = wx.FlexGridSizer(wx.HORIZONTAL)  # 可伸缩的网格布局，水平方向
        # 创建三个按钮
        start_server_button = wx.Button(p1, size=(130, 40), label='启动')
        record_save_button = wx.Button(p1, size=(130, 40), label='聊天记录保存')
        stop_server_button = wx.Button(p1, size=(130, 40), label='停止')
        g1.Add(start_server_button, 1, wx.TOP)
        g1.Add(record_save_button, 1, wx.TOP)
        g1.Add(stop_server_button, 1, wx.TOP)
        box.Add(g1, 1, wx.ALIGN_CENTRE)  # 联合居中
        # 创建只读的文本框，显示聊天记录
        self.text = wx.TextCtrl(p1, size=(400, 400), style=wx.TE_MULTILINE | wx.TE_READONLY)
        box.Add(self.text, 1, wx.ALIGN_CENTRE)
        p1.SetSizer(box)

        # 服务器的一些属性
        self.isOn = False  # 服务器没有启动
        self.host_port = ('', 8888)
        self.server_socket = socket(AF_INET, SOCK_STREAM)
        self.server_socket.bind(self.host_port)
        self.server_socket.listen(5)
        self.session_thread_map = {}  # 存放所有的服务器会话线程，客户端名字为key， 会话线程为value

        # 给所有的按钮绑定相应的动作
        self.Bind(wx.EVT_BUTTON, self.start_server, start_server_button)  # 给启动按钮绑定一个事件，事件触发会自动调用一个函数
        self.Bind(wx.EVT_BUTTON, self.save_record, record_save_button)

    def start_server(self, event):
        print("服务器启动！")
        if not self.isOn:
            # 启动服务器的主线程
            self.isOn = True
            main_thread = threading.Thread(target=self.do_work)
            main_thread.setDaemon(True)  # 设置为守护线程
            main_thread.start()

    # 服务器运行之后的函数
    def do_work(self):
        print("服务器开始工作！")
        while self.isOn:
            session_socket, client_addr = self.server_socket.accept()
            # 服务器首先接收客户端发送过来的第一条消息，我们规定第一条消息为客户端的名字
            username = session_socket.recv(1024).decode('utf-8')  # 接受客户端名字
            # 创建一个会话线程
            session_thread = SessionThread(self, session_socket, username)
            self.session_thread_map[username] = session_thread
            session_thread.start()
            # 表示有客户端进入到聊天室
            self.show_info_and_send_client('服务端通知：', f'欢迎{username}进入到聊天室！',
                                           time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
        self.server_socket.close()

    # 在文本中显示聊天信息，同时发送消息给所有的客户端。source:信息源;data:信息
    def show_info_and_send_client(self, source, data, data_time):
        send_data = f'{source} : {data}\n时间: {data_time}\n'
        self.text.AppendText('------------------------------\n%s' % send_data)  # 在服务器的文本框显示信息
        for client in self.session_thread_map.values():
            if client.isOn:  # 当前客户端是活动
                client.user_socket.send(send_data.encode('utf-8'))

    # 服务器保存聊天内容
    def save_record(self, event):
        record = self.text.GetValue()
        with open(file='record.log', mode='w+') as f:
            f.write(record)


# 服务器会话线程的类
class SessionThread(threading.Thread):
    def __init__(self, user_socket, username, server):
        threading.Thread.__init__(self)
        self.user_socket = user_socket
        self.username = username
        self.server = server
        self.isOn = True  # 会话线程是否启动

    def run(self):
        print(f"客户端{self.username}已经和服务器连接成功，服务器开启一个会话线程！")
        while self.isOn:
            data = self.user_socket.recv(1024).decode('utf-8')
            if data == 'A^disconnect^B':  # 如果客户端点击断开按钮，先发一条消息给服务器：消息内容的规定：A^disconnect^B
                self.isOn = False
                # 有用户离开，需要在聊天室通知其他人
                self.server.show_info_and_send_client('服务端通知：', f'{self.username}离开聊天室！',
                                                      time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
            else:
                # 其他聊天信息，我们应该显示给所有的客户端，包括服务器
                self.server.show_info_and_send_client(self.username, data,
                                                      time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
        self.user_socket.close()


if __name__ == '__main__':
    app = wx.App()
    Server().Show()
    app.MainLoop()  # 循环刷新显示
