# coding=utf-8
# @File: demo2.py
# @Author: zijier
# @Desc: 聊天室服务端
# @Date: 20:34 2024/04/13
import threading

import wx
from socket import *


class Server(wx.Frame):
    def __init__(self):
        # 调用父类的初始化函数
        wx.Frame.__init__(self, None, id=101, title="子杰聊天客户端", pos=wx.DefaultPosition, size=(400, 470))
        p1 = wx.Panel(self)  # 在窗口中初始化一个面板
        # 在面板中放一些按钮，文本框，文本输入框，将这些对象统一放进一个盒子里
        box = wx.BoxSizer(wx.VERTICAL)  # 在盒子里面垂直方向自动排版
        g1 = wx.FlexGridSizer(wx.HORIZONTAL)  # 可伸缩的网格布局，水平方向
        # 创建两个按钮
        start_server__button = wx.Button(p1, size=(130, 40), label='启动')
        record_save__button = wx.Button(p1, size=(130, 40), label='聊天记录保存')
        stop_server_button = wx.Button(p1, size=(130, 40), label='停止')
        g1.Add(start_server__button, 1, wx.TOP)
        g1.Add(record_save__button, 1, wx.TOP)
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
        self.Bind(wx.EVT_BUTTON, self.start_server, start_server__button)  # 给启动按钮绑定一个事件，事件触发会自动调用一个函数

    def start_server(self, event):
        print("服务器启动！")
        if not self.isOn:
            # 启动服务器的主线程
            self.isOn = True
            main_thread = threading.Thread(target=self.do_work)
            main_thread.setDaemon(self)  # 设置为守护线程
            main_thread.start()

    # 服务器运行之后的函数
    def do_work(self):
        print("服务器开始工作！")
        while self.isOn:
            session_socket, client_addr = self.server_socket.accept()
            # 服务器首先接收客户端发送过来的第一条消息，我们规定第一条消息为客户端的名字
            username = session_socket.recv(1024).decode('utf-8')  # 接受客户端名字
            # 创建一个会话线程
            session_thread = SessionThread(session_socket, username, self)
            self.session_thread_map[username] = session_thread
            session_thread.start()
        self.server_socket.close()


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
            else:
                pass  # 其他聊天信息，我们应该显示给所有的客户端，包括服务器
        self.user_socket.close()


if __name__ == '__main__':
    app = wx.App()
    Server().Show()
    app.MainLoop()  # 循环刷新显示
