# coding=utf-8
# @File: demo1.py
# @Author: zijier
# @Desc: 
# @Date: 14:28 2024/03/29

import subprocess

# runcmd = subprocess.run('dir C:\\Users\\Public', encoding='GBK', shell=True)
# print(runcmd)

def run_cmd(command):
    # 初始化一个子进程执行系统命令，subprocess.PIPE接受子进程的返回信息，一定要解码
    return_cmd = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='GBK', shell=True)

    if return_cmd.returncode==0:
        print("success：")
        print(return_cmd.stdout)
    else:
        print("命令执行错误：")
        print(return_cmd)

run_cmd('dir C:\\Users\\Public')