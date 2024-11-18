# coding=utf-8
# @File: demo2.py
# @Author: zijier
# @Desc: 
# @Date: 9:17 PM 2024/03/12

# 第一种
r = range(10)
print(r)
print(list(r))

# 第二种
r = range(1, 10)
print(list(r))

# 第三种
r = range(1, 10, 2)
print(list(r))
# 判断元素是否在列表中
print(8 in r)
print(9 in r)
