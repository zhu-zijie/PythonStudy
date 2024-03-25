# coding=utf-8
# @File: demo1.py
# @Author: zijier
# @Desc: 
# @Date: 10:23 PM 2024/03/11

# 不希望字符串中的转义符起作用，就使用原字符，在前面加上r或R

# 关键字
import keyword

print(keyword.kwlist)

# 变量
name = '玛丽亚'
print('标识', id(name))
print('类型', type(name))
print('值', name)

# 进制
# 二进制0b, 八进制0o, 十六进制0x

print(11 / 2)
print(11 // 2)  # 整除
print(2 ** 3)  # 2的3次方

# 交换变量的值
a, b = 10, 20
print("交换之前：", a, b)
a, b = b, a
print("交换之后：", a, b)

a = int(input("请输入第一个整数："))
b = int(input("请输入第二个整数："))
print(str(a) + "大于等于" + str(b) if a >= b else str(a) + "小于" + str(b))

