# coding=utf-8
# @File: demo3.py
# @Author: zijier
# @Desc: 
# @Date: 9:31 PM 2024/03/12

# for item in "Python":
#     print(item)
#
# for i in range(10):
#     print(i)

# for和while与else一起使用，没有碰到break就执行

# 列表的增删改
lst = [10, 20, 30]
print(lst)
lst.append(40)
print(lst)
lst2 = ["python", "hello", "world"]
lst.append(lst2)
print(lst)
# 列表的扩展
# lst.extend(lst2)
# print(lst)

# 任意地方插入
lst.insert(1, 90)
print(lst)

# 任意地方插入N个元素
lst[4:] = lst2
print(lst)

# 从列表中移除元素，如果有重复只移除第一个元素
lst.remove(30)
print(lst)

# 根据索引移除元素
lst.pop(2)
print(lst)

# 清楚列表所有的元素
# lst.clear()

# 将列表对象删除
# del lst

