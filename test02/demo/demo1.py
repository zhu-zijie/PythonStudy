# coding=utf-8
# @File: demo1.py
# @Author: zijier
# @Desc: 聊天室客户端
# @Date: 20:01 2024/04/13
import threading
from socket import *

import wx


# 客户端继承wx.Frame，就拥有窗口界面
class Client(wx.Frame):
    def __init__(self, c_name):
        # 调用父类的初始化函数
        wx.Frame.__init__(self, None, id=101, title=f"{c_name}的聊天客户端", pos=wx.DefaultPosition, size=(400, 470))
        p1 = wx.Panel(self)  # 在窗口中初始化一个面板
        # 在面板中放一些按钮，文本框，文本输入框，将这些对象统一放进一个盒子里
        box = wx.BoxSizer(wx.VERTICAL)  # 在盒子里面垂直方向自动排版
        g1 = wx.FlexGridSizer(wx.HORIZONTAL)  # 可伸缩的网格布局，水平方向
        # 创建两个按钮
        conn_button = wx.Button(p1, size=(200, 40), label='连接')
        disconn_button = wx.Button(p1, size=(200, 40), label='离开')
        g1.Add(conn_button, 1, wx.TOP | wx.LEFT)  # 连接按钮布局在左边
        g1.Add(disconn_button, 1, wx.TOP | wx.RIGHT)  # 断开按钮布局在右边
        box.Add(g1, 1, wx.ALIGN_CENTRE)  # 联合居中
        p1.SetSizer(box)
        # 创建聊天内容的文本框，不能写消息
        self.text = wx.TextCtrl(p1, size=(400, 250), style=wx.TE_MULTILINE | wx.TE_READONLY)
        box.Add(self.text, 1, wx.ALIGN_CENTRE)

        # 创建聊天的输入文本框，可以写
        self.input_text = wx.TextCtrl(p1, size=(400, 100), style=wx.TE_MULTILINE)
        box.Add(self.input_text, 1, wx.ALIGN_CENTRE)

        # 最后创建两个按钮，分别是发送和重置
        g2 = wx.FlexGridSizer(wx.HORIZONTAL)
        clear_button = wx.Button(p1, size=(200, 40), label="重置")
        send_button = wx.Button(p1, size=(200, 40), label="发送")
        g2.Add(clear_button, 1, wx.TOP | wx.LEFT)
        g2.Add(send_button, 1, wx.TOP | wx.RIGHT)
        box.Add(g2, 1, wx.ALIGN_CENTRE)

        p1.SetSizer(box)

        # 给所有按钮绑定点击事件
        self.Bind(wx.EVT_BUTTON, self.connect_to_server, conn_button)
        self.Bind(wx.EVT_BUTTON, self.send_to, send_button)
        self.Bind(wx.EVT_BUTTON, self.go_out, disconn_button)
        self.Bind(wx.EVT_BUTTON, self.reset, clear_button)

        # 客户端属性
        self.name = c_name
        self.isConnected = False
        self.client_socket = None

    # 连接服务器
    def connect_to_server(self, event):
        print(f"客户端{self.name}，开始连接服务器！")
        if not self.isConnected:
            server_host_port = ('localhost', 8888)
            self.client_socket = socket(AF_INET, SOCK_STREAM)
            self.client_socket.connect(server_host_port)
            # 客户端只要连接成功，马上把自己的名字发给服务器
            self.client_socket.send(self.name.encode('utf-8'))
            self.isConnected = True
            t = threading.Thread(target=self.receive_data)
            t.setDaemon(True)  # 客户端UI界面关闭，当前守护线程也自动关闭
            t.start()

    # 接受服务器发送过来的聊天数据
    def receive_data(self):
        while self.isConnected:
            try:
                data = self.client_socket.recv(1024).decode('utf-8')
                # 从服务器接收到的数据显示
                self.text.AppendText(f"{data}\n")
            except ConnectionResetError:
                print(f"客户端 {self.name} 意外断开连接。")
                self.isConnected = False
                break

    # 客户端发送消息到聊天室
    def send_to(self):
        if self.isConnected:
            info = self.input_text.GetValue()
            if info != '':
                self.client_socket.send(info.encode('utf-8'))
                # 输入框的数据如果已经发送了，输入框重新为空
                self.input_text.SetValue('')

    # 客户端离开聊天
    def go_out(self, event):
        self.client_socket.send('A^disconnect^B'.encode('utf-8'))
        # 客户端主线程也关闭
        self.isConnected = False

    # 客户端输入框的信息重置
    def reset(self, event):
        self.input_text.Clear()


if __name__ == '__main__':
    app = wx.App()
    name = input("请输入客户端的名字：")
    Client(name).Show()
    app.MainLoop()  # 循环刷新显示
