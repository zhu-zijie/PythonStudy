# coding=utf-8
# @File: demo2.py
# @Author: zijier
# @Desc: 
# @Date: 14:49 2024/03/29

import subprocess

# 创建一个子进程执行python命令
popen = subprocess.Popen('python', stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
# 往python命令中传入三条参数
popen.stdin.write('print("hello")\n'.encode('utf-8'))
popen.stdin.write('import os\n'.encode('utf-8'))
popen.stdin.write('print(os.environ)'.encode('utf-8'))
popen.stdin.close()

out = popen.stdout.read().decode('GBK')
popen.stdout.close()

print(out)
