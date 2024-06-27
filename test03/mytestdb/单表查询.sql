-- 对emp表进行查询
SELECT * FROM emp;	-- *代表所有的数据
-- 显示部分列
SELECT empno, ename, sal FROM emp;
-- 显示部分行
SELECT * FROM emp WHERE sal > 2000;
-- 显示部分行部分行
SELECT empno, ename, job, mgr FROM emp WHERE sal > 2000;

-- 起别名,as可以省略，''和""可以省略，有特殊符号时不可以省略
SELECT empno 员工编号, ename 姓名, sal 工资 FROM emp;
SELECT empno AS 员工编号, ename AS 姓名, sal AS 工资 FROM emp;

-- 算术运算符
SELECT empno, ename, sal, sal + 1000 AS '涨薪后', deptno FROM emp WHERE sal < 2500;

-- 去重操作
SELECT DISTINCT job FROM emp;
SELECT DISTINCT job, deptno FROM emp;	-- 对后面所有列的组合去重，而不是单独一列去重

-- 排序
SELECT * FROM emp ORDER BY sal;	-- 默认按照升序来排列的
SELECT * FROM emp ORDER BY sal DESC;	-- ASC升序，DESC降序
SELECT * FROM emp ORDER BY sal ASC, deptno DESC;	-- sal升序的同时，deptno降序排列

