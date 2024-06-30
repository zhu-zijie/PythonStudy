# 导入pymysql包
from pymysql import *

# 创建数据库连接
conn = connect(host='localhost', port=3306, user='root', password='root', db='mytestdb', charset='utf8')

# 打开游标
cur = conn.cursor()

# 执行sql语句
# 查询数据

sql = "select empno, ename, job, sal from emp where deptno = %s"
params = (20)
rowcount = cur.execute(sql, params)
# result = cur.fetchone()  # 取一条数据
# result = cur.fetchmany(3)  # 取三条数据
result = cur.fetchall()  # 取所有的数据
for i in result:
    print(i)
# print(result)

# 关闭游标
cur.close()

# 关闭连接
conn.close()
