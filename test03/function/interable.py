# Iterable:可迭代对象，能通过for循环来遍历里面的元素的对象。
from collections.abc import Iterable
from collections.abc import Iterator

a = (1,)
b = [1, 2]
c = {}


def test1(args):
    if isinstance(args, Iterator):
        print("args对象是可迭代对象！")
    else:
        print("args对象不是可迭代对象！")


def test2(args):
    if isinstance(args, Iterator):
        print("args对象是迭代器！")
    else:
        print("args对象不是迭代器！")

# list,dic,str等Iterable变成Iterator，可以使用iter()

