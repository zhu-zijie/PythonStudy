## 这是一个单行注释
/*
这是一个多行注释
*/

-- 创建数据库表

CREATE TABLE t_student (
	sno INT(6),	-- 6显示长度
	sname VARCHAR(5),
	sex CHAR(1),
	age INT(3),
	enterdate DATE,
	classname VARCHAR(10),
	email VARCHAR(15)
);

-- 查看表的结构
DESC t_student;

-- 查看表的数据
SELECT * from t_student;

-- 查看表的键表语句
SHOW CREATE TABLE t_student;



