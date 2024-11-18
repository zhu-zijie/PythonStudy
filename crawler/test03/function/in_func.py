from functools import reduce

# map: 把一个可迭代对象中的每一个元素转换成一个新的对象，最后返回一个迭代器

lst = [1, 2, 3, 4, 5, 10, 7, 8]
it = map(lambda x: x ** 2, lst)

# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

print(list(it))

# reduce: 把一个可迭代对象中每一个元素做聚合处理，最后返回一个聚合之后的值
print(reduce(lambda x, y: x + y, lst))  # 累加


def getMax(x, y):
    if x > y:
        return x
    else:
        return y


print(reduce(getMax, lst))

# filter: 把一个可迭代对象中的元素做过滤操作，如果func返回值为True则留下，否则过滤掉。

emps = [  # 员工的列表
    {'name': '张三', 'age': 18, 'salary': 3000},
    {'name': '李四', 'age': 28, 'salary': 5000},
    {'name': '王五', 'age': 38, 'salary': 4000}
]

print(list(filter(lambda x: x['age'] > 18, emps)))

# max和min
print(max(emps, key=lambda x: x['salary']))
print(min(emps, key=lambda x: x['salary']))


# sorted: 把一个可迭代对象里面的每一个元素做排序，返回一个列表。

print(sorted(emps, key=lambda x:x['age'], reverse=True))

