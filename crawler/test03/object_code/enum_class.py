from enum import Enum

# 当项目中需要使用十二个月时
# 枚举中：一个名字，对应一个值
Month = Enum("抬头-month", ('jan', 'feb', 'mar', 'apr', 'may', 'jun'))
# 把所有的枚举中的值遍历出来
print(Month.__members__)  # 枚举中的值自动为1开始
print(Month['may'].value)  # 根据名字得到值
print(Month(4).name)  # 根据值得到名字


class Color(Enum):
    red = 100
    green = 200
    blue = 30
    yellow = 200  # 不允许key相同或者value，如果value相同，根据value取name只能取第一个。


print(Color(200))
