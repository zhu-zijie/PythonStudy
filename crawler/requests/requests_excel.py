import openpyxl

# 创建工作簿对象
# wb = openpyxl.Workbook()
# 获取活动工作表
# sheet = wb.active
# 获取指定单元格
# cell = sheet['A1']
# 向单元格写入数据
# cell.value = 'hello, world'
# 一次性写入一行数据
# lst = ['姓名', '年龄', '性别', '成绩']
# sheet.append(lst)
# 一次性写入多行数据
# lsts = [
#     ['张三', 18, '男', 98],
#     ['李四', 20, '女', 88],
#     ['王五', 22, '男', 78],
#     ['赵六', 24, '女', 68],
# ]
# for lst in lsts:
#     sheet.append(lst)
# 保存
# wb.save('test.xlsx')

# 读取数据
wb = openpyxl.load_workbook('test.xlsx')
# 获取活动工作表
sheet = wb.active
# 获取指定单元格内容
cell = sheet['A1']
value = cell.value

# 获取A系列的所有单元格
column = sheet['A']
for col in column:
    print(col.value)
# 获取第三行的所有单元格
row = sheet[3]
for cell in row:
    print(cell.value)

print('--------------------------')
# 获取A-D列所有的单元格
columns = sheet['A:D']
for col in columns:
    for cell in col:
        print(cell.value)
        