import numpy as np

n1 = np.array([1, 2, 3])
print(n1)

# 创建带小数的数组
n2 = np.array([0.1, 0.2, 0.3])
print(n2)

# 创建一个二位数组
n3 = np.array([[1, 2], [3, 4]])
print(n3)

# 创建数组时指定数据类型
n4 = np.array([1, 2, 3], dtype=float)
print(n4)

# 数组复制
n5 = np.array([1, 2, 3])
n6 = np.array(n5, copy=True)
print(n6)

# 指定维数
lst = [1, 2, 3]
n7 = np.array(lst, ndmin=3)  # 最小维数
print(n7)

# 不同方式创建数组,4行3列
n8 = np.empty([4, 3], dtype=int)
print(n8)

# 创建指定维度，以0填充，输出结果默认为浮点型
n9 = np.zeros(3)
print(n9)

# 创建指定维度，以1填充
n10 = np.ones(3)
print(n10)

# 创建指定维度，以指定的数值填充
n11 = np.full(3, 8)
print(n11)

# 3行4列以8填充
n12 = np.full([3, 4], 8)
print(n12)
