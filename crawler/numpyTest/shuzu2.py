import numpy as np

n1 = np.arange(1, 11, 2)
print(n1)

# 等差数列，7500开始，10000结尾，6为创建个数
n2 = np.linspace(7500, 10000, 6)
print(n2)

# 数组元素是一个等比数列
# n3 = np.logspace(0, 63, 64, base=2, dtype=int)
# print(n3)

# 生成[0,1)之间的随机数
n4 = np.random.rand(5)
print(n4)

# 生成2行4列的随机数组
n5 = np.random.rand(2, 4)
print(n5)

# 用于从正态分布中返回随机生成的数组
n6 = np.random.randn(3)
print(n6)

# 3行4列的随机数组从正态分布中返回
n7 = np.random.randn(3, 4)
print(n7)

# 生成指定范围的随机数组,[1,3)产生十个数
n8 = np.random.randint(1, 3, 10)
print(n8)

n9 = np.random.randint(1, 3, size=(2, 3))
print(n9)

# 生成正态分布的随机数组,产生10个数，其中0为对称轴，0.1为标准差
n10 = np.random.normal(0, 0.1, 10)
print(n10)

# asarray函数的使用
n11 = np.asarray([1, 2, 3])  # 通过列表创建数组
print(n11)

# 通过列表的元组创建数组
n12 = np.asarray([(1, 2, 3), (4, 5, 6)])
print(n12)

# 通过元组创建数组
n13 = np.asarray((1, 2, 3))
print(n13)

# 通过元组的元组创建数组
n14 = np.asarray(((1, 2, 3), (4, 5, 6)))
print(n14)

# 通过元组的列表创建数组
n15 = np.asarray(([1, 2], [3, 4]))
print(n15)

# 动态数组 S1表示单个字符串是一个字符
n16 = np.frombuffer(b'zhuzijie', dtype='S1')
print(n16)

# 从迭代对象中创建数组对象
iter1 = (i for i in range(5))
n17 = np.fromiter(iter1, dtype=int)
print(n17)

# empty_like的使用，创建一个2行2列的数组
n18 = np.empty_like([[1, 2], [3, 4]])
print(n18)

# 运算
n19 = np.array([1, 2])
n20 = np.array([3, 4])
print("加法运算", n19 + n20)
print("减法运算", n19 - n20)
print("乘法运算", n19 * n20)
print("除法运算", n19 / n20)
print("幂运算", n19 ** n20)
print("比较运算", n19 > n20)

# 数组的索引
n21 = np.array([1, 2, 3, 4])
print(n21[0])
print(n21[-4])

n22 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(n22[1][2])
print(n22[1, 2])

n23 = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])
print(n23[:3])
print(n23[::-1])

# 数组重塑
n24 = np.arange(6)
n25 = n24.reshape(2, 3)
print(n25)

# 数组转置
n26 = np.arange(24)
n27 = n26.reshape(4, 6)
print(n27)
n28 = n27.T
print(n28)
n29 = n27.transpose()
print(n29)

n30 = np.array([[1, 2], [3, 4], [5, 6]])
n31 = np.array([[10, 20], [30, 40], [50, 60]])
# 水平方向增加数据(列数的增加)
print(np.hstack((n30, n31)))
# 垂直方向增加数据(行数的增加)
print(np.vstack((n30, n31)))

# 数组的删除
n32 = np.array([[1, 2], [3, 4], [5, 6]])
# 删除第三行
n33 = np.delete(n32, 2, axis=0)
print(n33)
# 删除第一列
n34 = np.delete(n32, 0, axis=1)
print(n34)
# 删除第二行第三行
n35 = np.delete(n32, (1, 2), axis=0)
print(n35)

# 数组的修改操作
n36 = np.array([[1, 2], [3, 4], [5, 6]])
n36[1] = [30, 40]
print(n36)
n36[2][1] = 88
print(n36)

# 数组的查询操作
n37 = np.arange(1, 11)
n38 = np.where(n37 > 5)
n39 = n37[np.where(n37 > 5)]
print(n39)
n40 = np.where(n37 > 5, 2, 0)  # 数组中元素大于5输出2，否则输出0
print(n40)
