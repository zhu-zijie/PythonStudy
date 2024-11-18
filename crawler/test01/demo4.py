# coding=utf-8
# @File: demo4.py
# @Author: zijier
# @Desc: 
# @Date: 10:49 PM 2024/03/12

# 不改变列表对象
# 列表的排序，默认为升序
lst = [10, 40, 320, 23, 50, 31]
lst.sort()
print(lst)

# 降序
lst.sort(reverse=True)
print(lst)

# 产生新的对象列表
lst2 = [10, 40, 320, 23, 50, 31]
print("原列表：", lst2)
new_lst2 = sorted(lst2)
print(new_lst2)
new_lst2 = sorted(lst2, reverse=True)
print(new_lst2)
