import re

s = '''
<div class = 'zhangsan'><span id = '1'>张三</span></div>
<div class = 'lisi'><span id = '2'>李四</span></div>
<div class = 'wangwu'><span id = '3'>王五</span></div>
<div class = 'zhaoliu'><span id = '4'>赵六</span></div> 
'''
#?P<名字>正则:可以单独从正则匹配的内容中提取内容
obj = re.compile(r"<div class = '.*?'><span id = '(?P<id>\d+)'>(?P<name>.*?)</span></div>", re.S)#让.匹配换行符

result = obj.finditer(s)
for it in result:
    print(it.group("name"))
    #print(it.group("id"))