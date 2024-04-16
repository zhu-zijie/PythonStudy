# coding=utf-8
# @File: demo1.py
# @Author: zijier
# @Desc: 聊天室客户端
# @Date: 20:01 2024/04/13

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
        disconn_button = wx.Button(p1, size=(200, 40), label='断开')
        g1.Add(conn_button, 1, wx.TOP | wx.LEFT)  # 连接按钮布局在左边
        g1.Add(disconn_button, 1, wx.TOP | wx.RIGHT)  # 断开按钮布局在右边
        box.Add(g1, 1, wx.ALIGN_CENTRE)  # 联合居中
        p1.SetSizer(box)
        # 创建聊天内容的文本框，不能写消息
        self.text = wx.TextCtrl(p1, size=(400, 250), style=wx.TE_MULTILINE | wx.TE_READONLY)
        box.Add(self.text, 1, wx.ALIGN_CENTRE)

        # 创建聊天的输入文本框，可以写
        self.text = wx.TextCtrl(p1, size=(400, 100), style=wx.TE_MULTILINE)
        box.Add(self.text, 1, wx.ALIGN_CENTRE)

        # 最后创建两个按钮，分别是发送和重置
        g2 = wx.FlexGridSizer(wx.HORIZONTAL)
        clear_button = wx.Button(p1, size=(200, 40), label="重置")
        send_button = wx.Button(p1, size=(200, 40), label="发送")
        g2.Add(clear_button, 1, wx.TOP | wx.LEFT)
        g2.Add(send_button, 1, wx.TOP | wx.RIGHT)
        box.Add(g2, 1, wx.ALIGN_CENTRE)

        # 给所有按钮绑定点击事件
        wx.Bind(wx.EVT_BUTTON, self.connect_to_server, conn_button)

    def connect_to_server(self, event):
        pass


if __name__ == '__main__':
    app = wx.App()
    Client('张三').Show()
    app.MainLoop()  # 循环刷新显示
