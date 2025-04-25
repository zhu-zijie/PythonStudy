"""
快速排序 - 选择枢轴对元素进行划分，左边都比枢轴小右边都比枢轴大
"""


def quick_sort(items, comp=lambda x, y: x <= y):
    items = list(items)[:]
    _quick_sort(items, 0, len(items) - 1, comp)
    return items


def _quick_sort(items, start, end, comp):
    if start < end:
        pos = _partition(items, start, end, comp)
        _quick_sort(items, start, pos - 1, comp)
        _quick_sort(items, pos + 1, end, comp)


def _partition(items, start, end, comp):
    pivot = items[end]
    i = start - 1
    for j in range(start, end):
        if comp(items[j], pivot):
            i += 1
            items[i], items[j] = items[j], items[i]
    items[i + 1], items[end] = items[end], items[i + 1]
    return i + 1


def main():
    """主函数"""
    # 整数列表排序示例
    items1 = [6, 8, 7, 9, 3, 5, 2, 1, 4]
    print("原始整数列表:", items1)
    sorted_items1 = quick_sort(items1)
    print("排序后列表:", sorted_items1)

    # 字符串列表排序示例
    items2 = ['apple', 'orange', 'banana', 'pear', 'grape']
    print("\n原始字符串列表:", items2)
    sorted_items2 = quick_sort(items2)
    print("排序后列表:", sorted_items2)

    # 字符串列表按长度排序示例
    print("\n按长度排序字符串列表:")
    sorted_items3 = quick_sort(items2, comp=lambda x, y: len(x) <= len(y))
    print("排序后列表:", sorted_items3)

    # 自定义对象排序示例
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        def __repr__(self):
            return f"Person({self.name}, {self.age})"

    persons = [
        Person("张三", 25),
        Person("李四", 22),
        Person("王五", 35),
        Person("赵六", 18)
    ]

    print("\n按年龄排序人员列表:")
    sorted_persons = quick_sort(persons, comp=lambda x, y: x.age <= y.age)
    print("排序后列表:", sorted_persons)


if __name__ == '__main__':
    main()
