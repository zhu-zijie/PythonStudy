-- 先建父表：班级表
CREATE TABLE t_class(
	cno INT(4) PRIMARY KEY auto_increment,
	cname VARCHAR(10) NOT NULL,
	room CHAR(4)
)

-- 添加班级数据
INSERT INTO t_class VALUES (NULL, 'java001', 'r803')
INSERT INTO t_class VALUES (NULL, 'java002', 'r341')
INSERT INTO t_class VALUES (NULL, '大数据001', 'r103')

-- 一次性添加多条数据
INSERT INTO t_class VALUES (NULL, 'java001', 'r803'), (NULL, 'java002', 'r341'), (NULL, '大数据001', 'r103')

-- 查询班级表
SELECT * FROM t_class;

-- 学生表删除
DROP TABLE t_student;

-- 创建学生表(子表)
CREATE TABLE t_student(
	sno INT(6) PRIMARY KEY auto_increment,	-- 6显示长度
	sname VARCHAR(5) NOT NULL,
	classno INT(4),	-- 取值参考t_class表中的cno字段
	CONSTRAINT fk_stu_classno FOREIGN KEY (classno) REFERENCES t_class (cno)
);

-- 添加学生的信息
INSERT INTO t_student VALUES (NULL, '张三', 1), (NULL, '李四', 1), (NULL, '王五', 2);
ALTER TABLE t_student ADD CONSTRAINT fk_stu_classno FOREIGN KEY (classno) REFERENCES t_class (cno);

-- 删除学生的信息，此时删除不了，有学生使用了当前班级号
DELETE FROM t_class where cno = 1;

-- CASCADE级联操作,操作主表时影响从表的外键信息
-- 先删除之前的外键信息
ALTER TABLE t_student DROP FOREIGN KEY fk_stu_classno;
-- 重新添加外键约束
ALTER TABLE t_student ADD CONSTRAINT fk_stu_classno FOREIGN key (classno) REFERENCES t_class (cno) on UPDATE CASCADE on DELETE CASCADE;
-- 试试更新
UPDATE t_class SET cno = 8 where cno = 1;
-- 试试更新
DELETE FROM t_class WHERE cno = 8;

-- set null置空操作
-- 先删除之前的外键信息
ALTER TABLE t_student DROP FOREIGN KEY fk_stu_classno;
-- 重新添加外键约束
ALTER TABLE t_student ADD CONSTRAINT fk_stu_classno FOREIGN key (classno) REFERENCES t_class (cno) on UPDATE SET NULL on DELETE SET NULL;
-- 试试更新
UPDATE t_class SET cno = 8 where cno = 2;

-- 级联操作可以与置空操作混着使用