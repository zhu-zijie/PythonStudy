-- 查看数据
SELECT * FROM t_student;

-- 修改表的结构
-- 增加一列
ALTER TABLE t_student ADD score DOUBLE(5, 2);	-- 5为总的位数，2为小数位数
-- 增加一列放在首位
ALTER TABLE t_student ADD score DOUBLE(5, 2) FIRST;	-- 5为总的位数，2为小数位数
-- 增加一列放在sex列后面
ALTER TABLE t_student ADD score DOUBLE(5, 2) AFTER sex;	-- 5为总的位数，2为小数位数

UPDATE t_student set score = 123.23 WHERE sno = 2;

-- 删除一列
ALTER TABLE t_student DROP score;

-- 修改一列
ALTER TABLE t_student MODIFY score FLOAT(4,1);	-- MODIFY修改是列的类型，但不会修改列的名字
ALTER TABLE  t_student CHANGE score score1 DOUBLE(5,1);	-- CHANGE修改列名和列的类型的定义

-- 删除表
DROP TABLE t_student;
