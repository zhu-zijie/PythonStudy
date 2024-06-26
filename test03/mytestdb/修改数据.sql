-- 查看表的记录
SELECT * FROM t_student;

-- 在t_student数据库表中插入数据：NOW()，SYSDATE()，CURRENT_DATE为当前的时间，如果不是全字段插入数据，需要加入字段的名字。
INSERT INTO t_student VALUES (1, '张三', '男', 18, '2022-2-8', '物流3班', '123456@126.com');
INSERT INTO t_student VALUES (10001094, '张三', '男', 18, CURRENT_TIME, '物流3班', '123456@126.com');
INSERT INTO t_student (sno, sname, sex) VALUES (2, '李四', '男')

-- 修改表中的数据
UPDATE t_student SET sex = '女' WHERE sname = '李四';

-- 删除操作
DELETE FROM t_student WHERE sno = 1;