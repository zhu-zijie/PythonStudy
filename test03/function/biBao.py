# 闭包

def func_a(number_a):
    def func_b(number_b):
        print(f"内嵌的函数func_b的参数是{number_b}， 外部的函数func_a的参数是{number_a}")
        return number_b + number_a

    return func_b


result = func_a(10)  # 10传给函数func_a
print(result(10))  # 10传给内嵌函数func_b
print(result(90))  # 90传给内嵌函数func_b


# func_b就是闭包

# 闭包的应用

def creat_line(a, b):
    def line(x):
        return a * x + b

    return line


# 得到两个一元函数
l1 = creat_line(2, 2)
l2 = creat_line(3, 5)

# 在x=5时得到l1的值
print(l1(5))
# 在x=5时得到l1的值
print(l2(5))
