import re

# #findall:匹配字符串中所有符合正则的内容
# list = re.findall(r"\d+", "我的电话号码是：10010，我女朋友的电话号码是：10086.")
# print(list)
#
# #finditer:匹配字符串中所有的内容（返回的是迭代器），从迭代器中拿到内容需要.group()
# it = re.finditer(r"\d+", "我的电话号码是：10010，我女朋友的电话号码是：10086.")
# for i in it:
#     print(i.group())
#
# #search:找到结果就返回，返回的是match对象，拿数据需要.group
# s = re.search(r"\d+", "我的电话号码是：10010，我女朋友的电话号码是：10086.")
# print(s.group())
#
# #match:从开头开始匹配
# s = re.match(r"\d+", "我的电话号码是：10010，我女朋友的电话号码是：10086.")
# print(s.group())

#预加载正则表达式
obj = re.compile(r"\d+")
ret = obj.finditer("我的电话号码是：10010，我女朋友的电话号码是：10086.")
for it in ret:
    print(it.group())