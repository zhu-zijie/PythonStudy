-- 函数的举例
SELECT empno, ename, LOWER(ename), UPPER(ename), sal from emp;	-- 多行函数
-- 函数的功能：封装了特定的一些功能，我们拿过来直接使用，可以实现对应的功能

-- 多行函数
SELECT MAX(sal), MIN(sal), COUNT(sal), SUM(sal), AVG(sal) FROM emp;

-- 字符串函数
SELECT ename, LENGTH(ename), SUBSTRING(ename, 2, 3) FROM emp;
-- SUBSTRING()字符串提取，2：从字符下标为2开始，截取长度3。下标从1开始。
-- 数值函数
SELECT ABS(-3), CEIL(5.3), FLOOR(5.9), ROUND(3.14) FROM DUAL;	-- DUAL实际就是一个伪表
SELECT ABS(-3), CEIL(5.3), FLOOR(5.9), ROUND(3.14);	-- 如果没有where条件的话，from dual可以省略不写
-- 日期与时间类函数
SELECT * FROM emp;
SELECT CURDATE(), CURTIME();	-- CURDATE()年月日，CURTIME()时分秒
SELECT NOW(), SYSDATE() FROM DUAL;	-- NOW()返回当前的时间，SYSDATE()时刻系统的时间，都表示年月日时分秒

-- 插入一条数据
INSERT INTO emp VALUES (9999, 'lili', 'SALESMAN', 7698, NOW(), 1000, NULL, 30);

-- 流程函数
-- if相关
SELECT empno, ename, sal, IF(sal>=2500,'高薪','底薪') AS '薪资等级' FROM emp;	-- IF ELSE双分支结构
SELECT empno, ename, sal, comm, sal+IFNULL(comm,0) FROM emp;	-- 如果comm是null,那么取值为0.单分支
SELECT NULLIF(1,1), NULLIF(1,2) FROM DUAL;	-- 如果value1等于value2,则返回null;否则返回value1
-- case相关
-- case等值判断
SELECT empno, ename, job,
CASE job
	WHEN 'CLERK' THEN '店员'
	WHEN 'SALESMAN' THEN '销售'
	WHEN 'MANAGER' THEN '经理'
	ELSE '其它'
END, sal FROM emp;

-- case区间判断
SELECT empno, ename, sal,
CASE 
	WHEN sal <= 1000 THEN 'A'
	WHEN sal <= 2000 THEN 'B'
	WHEN sal <= 3000 THEN 'C'
	ELSE 'D'
END '工资等级',
deptno FROM emp;

-- 其他函数
SELECT DATABASE(), USER(), VERSION() FROM DUAL;

-- max(),min(),count()针对所有的类型，sum(),avg()只针对数值类型有效
SELECT MAX(sal), MIN(sal), COUNT(sal), SUM(sal), AVG(sal) FROM emp;
SELECT MAX(comm), MIN(comm), COUNT(comm), SUM(comm), AVG(comm) FROM emp;
