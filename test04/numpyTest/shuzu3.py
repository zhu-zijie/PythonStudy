import numpy as np

n1 = np.mat('1 2; 3 4')
print(type(n1))

n2 = np.mat([[1, 2], [3, 4]])
print(type(n2))

n3 = np.mat(np.zeros((3, 3)))
print(n3)

n4 = np.mat(np.zeros((2, 4)))
print(n4)

# 1-8之间随机数
n5 = np.mat(np.random.randint(1, 8, size=(3, 5)))
print(n5)

# 对角矩阵
n6 = np.mat(np.eye(2, 2), dtype=int)
print(n6)
n7 = np.mat(np.eye(4, 4), dtype=int)
print(n7)

# 对角线矩阵
a = [1, 2, 3]
n8 = np.mat(np.diag(a))
print(n8)

# 矩阵的加减乘除
n9 = np.mat([[1, 2], [3, 4], [5, 6]])
print(n9)
n10 = np.mat([1, 2])
print(n9 + n10)
print(n9 - n10)
print(n9 / n10)
print(n9 * n10.T)

# 数组的相乘与数组的点积
n11 = np.array([[1, 2], [3, 4], [5, 6]])
n12 = np.array([1, 2])
print('数组的乘积:', n11 * n12)
print('数组的点积:', np.dot(n11, n12))
# 矩阵的相乘*(点积)，矩阵对应元素相乘np.multiply

n13 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
n14 = np.array([10, 10, 10])
print(np.add(n13, n14))
print(np.subtract(n13, n14))
print(np.multiply(n13, n14))
print(np.divide(n13, n14))

# 倒数
n15 = np.array([0.2, 0.4, 0.8])
print(np.reciprocal(n15))

# 四舍五入
n16 = np.array([1.313, 5.243, 7.743, -8.245])
print(n16)
print("四舍五入取整：", np.around(n16))
print("保留小数点后两位：", np.around(n16, decimals=2))

# 向上取整与向下取整
print(np.ceil(n16))
print(np.floor(n16))

# 三角函数
n17 = np.array([0, 30, 45, 60, 90])
print(np.around(np.sin(n17 * np.pi / 180), decimals=2))
print(np.around(np.cos(n17 * np.pi / 180), decimals=2))
print(np.around(np.tan(n17 * np.pi / 180), decimals=2))

n18 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(n18)
print(n18.sum())
# 数组元素行的和
print(n18.sum(axis=0))
# 数组元素列的和
print(n18.sum(axis=1))
# 平均值
print(n18.mean())
# 行的平均值
print(n18.mean(axis=0))
# 列的平均值
print(n18.mean(axis=1))
# 数组中的最大值
print(n18.max())
# 行的最大值
print(n18.max(axis=0))
# 列的最大值
print(n18.max(axis=1))

# 加权平均
n19 = np.array([1, 2, 3, 4, 5])
n20 = np.array([10, 20, 30, 40, 50])
print("加权平均：", np.average(n19, weights=n20))

# 中位数
n21 = np.array([1, 2, 3, 4, 5, 6])
print("中位数：", np.median(n21))

# 方差
n22 = np.array([1, 2, 3])
print("方差：", n22.var())

# 标准差
print("标准差：", n22.std())

# 数组的排序
n23 = np.array([[4, 2, 7], [6, 7, 1], [8, 4, 7]])
print(n23)
print("数组的排序：", np.sort(n23))
print("按行排序：", np.sort(n23, axis=0))
print("按列排序：", np.sort(n23, axis=1))

# argsort()排序
n24 = np.array([8, 4, 9, 0, 2, 5, 1])
n25 = np.argsort(n24)
print(n25)
# 排序后的重构操作
print(n24[n25])

# lexsort排序
math = np.array([112, 115, 118, 104, 108, 115])
en = np.array([112, 110, 109, 102, 105, 103])
total = np.array([619, 610, 654, 632, 602, 630])
sort_total = np.lexsort((en, math, total))  # 总成绩>数学>英语
print(sort_total)
lst = [[total[i], math[i], en[i]] for i in sort_total]
n26 = np.array(lst)
print(n26)
