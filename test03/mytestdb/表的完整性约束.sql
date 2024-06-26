SELECT * FROM t_student;

CREATE TABLE t_student(
	sno INT(6) PRIMARY KEY auto_increment,	-- 6显示长度，学号为主键，需要自增
	sname VARCHAR(5) NOT NULL,
	sex CHAR(1) DEFAULT('男') CHECK(sex = '男' || sex = '女'),
	age INT(3) CHECK(age >= 18 && age <= 50),
	enterdate DATE,
	classname VARCHAR(10),
	email VARCHAR(15) UNIQUE
);

-- 删除表
DROP TABLE t_student;

-- 添加数据
INSERT INTO t_student VALUES (1, '张三', '女', 18, NOW(), '物流3班', '123456@126.com');
INSERT INTO t_student VALUES (NULL, '王五', '女', 18, NOW(), '物流3班', '123456@126.com');	-- 报错，邮箱重复了，主键浪费一次
INSERT INTO t_student VALUES (DEFAULT, '赵六', '男', 23, NOW(), '物流3班', '234567@126.com');
INSERT INTO t_student (sname, enterdate) VALUES ('李四', NOW())
-- 如果主键没有设定值，或者可以用null，default都可以完成主键自增的效果
-- 如果sql报错，可能主键就浪费了，后续插入的主键不连号，我们主键也不要求连号的


CREATE TABLE t_student(
	sno INT(6) auto_increment,	-- 6显示长度
	sname VARCHAR(5) NOT NULL,
	sex CHAR(1) DEFAULT('男'),
	age INT(3),
	enterdate DATE,
	classname VARCHAR(10),
	email VARCHAR(15),
	CONSTRAINT pk_stu PRIMARY KEY (sno),		-- pk_stu主键约束的名字
	CONSTRAINT ck_stu_sex CHECK (sex = '男' || sex = '女'),
	CONSTRAINT ck_stu_age CHECK (age >= 18 && age <= 50),
	CONSTRAINT uq_stu_email UNIQUE (email)
);


CREATE TABLE t_student(
	sno INT(6),	-- 6显示长度
	sname VARCHAR(5) NOT NULL,
	sex CHAR(1) DEFAULT('男'),
	age INT(3),
	enterdate DATE,
	classname VARCHAR(10),
	email VARCHAR(15)
);
-- 在创建表以后添加约束
ALTER TABLE t_student ADD CONSTRAINT pk_stu PRIMARY KEY (sno);	-- 添加主键约束
ALTER TABLE t_student MODIFY sno INT(6) auto_increment;	-- 修改自增条件
ALTER TABLE t_student ADD CONSTRAINT ck_stu_sex CHECK (sex = '男' || sex = '女');
ALTER TABLE t_student ADD CONSTRAINT ck_stu_age CHECK (age >= 18 && age <= 50);
ALTER TABLE t_student ADD CONSTRAINT uq_stu_email UNIQUE (email);


-- 查询表的结构
DESC t_student;