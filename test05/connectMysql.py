# 导入pymysql包
from pymysql import *

# 创建数据库连接
conn = connect(host='localhost', port=3306, user='root', password='root', db='mytestdb', charset='utf8')

# 打开游标
cur = conn.cursor()

# 执行sql语句
# 增加一条数据
# try:
#     sql = "insert into emp values (%s, %s, %s, %s, %s, %s, %s, %s)"
#     params = (9999, 'LILI', 'CLERK', 7782, '1981-01-01', 1000, 0.00, 20)
#     cur.execute(sql, params)
#     conn.commit()
#     print("增加成功！")
# except:
#     conn.rollback()
#     print("增加失败！")

# 增加多条数据
# try:
#     sql = "insert into emp values (%s, %s, %s, %s, %s, %s, %s, %s)"
#     params = [(9999, 'LILI', 'CLERK', 7782, '1981-01-01', 1000, 0.00, 20),
#               (8888, 'NANA', 'CLERK', 9999, '1982-01-01', 900, 0.00, 20),
#               (7777, 'XIAOMING', 'CLERK', 8888, '1983-01-01', 800, 0.00, 20)]
#     cur.executemany(sql, params)
#     conn.commit()
#     print("增加成功！")
# except:
#     conn.rollback()
#     print("增加失败！")

# 删除数据
# try:
#     sql = "delete from emp where ename=%s"
#     params = [('LILI'), ('NANA'), ('XIAOMING')]
#     rowcount = cur.executemany(sql, params)
#     conn.commit()
#     print("已删除" + str(rowcount) + "条数据")
# except:
#     conn.rollback()
#     print("删除失败！")

# 修改数据
try:
    sql = "update emp set sal = %s where ename=%s"
    params = [(5500, 'KING')]
    rowcount = cur.executemany(sql, params)
    conn.commit()
    print("已修改" + str(rowcount) + "条数据")
except:
    conn.rollback()
    print("修改失败！")

# 关闭游标
cur.close()

# 关闭连接
conn.close()
