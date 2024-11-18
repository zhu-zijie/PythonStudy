import re

tel_1 = '''
1482994722,
15923488821,
11131231244，
431jfmcld,
14793048210
a14235345124
'''
tel_2 = '13923488821dasd'
# 编译正则表达式之后得到一个编译对象
pattern = re.compile(r'1[3-9]\d{9}')
# search只会返回第一个匹配的结果，如果没有匹配的返回None
result1 = pattern.search(tel_1)
print(result1.group(0))  # 返回第一个匹配结果
print(result1.span(0))  # 返回第一个结果的下标

# match函数是从第一个字符开始匹配的，如果没有则返回None
result2 = pattern.match(tel_2)
print(result2.group(0))
