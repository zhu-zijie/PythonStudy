-- 查询员工的编号，姓名，部门编号
SELECT * FROM emp;
SELECT empno, ename, deptno FROM emp;

-- 多表查询 交叉连接cross join
SELECT * FROM emp CROSS JOIN dept;	-- 笛卡尔乘积：没有实际意义，有理论意义

-- 自然连接：natural join，natural可以省略
SELECT * FROM emp NATURAL JOIN dept;	-- 自动匹配同名的列，同名列只展示一次

SELECT empno, ename, sal, dname, loc FROM emp NATURAL JOIN dept;
-- 缺点：查询字段的时候，没有指定字段所属的数据库表，效率低
-- 解决：指定表名
SELECT emp.empno, emp.ename, emp.sal, dept.dname, dept.loc FROM emp NATURAL JOIN dept;

-- 缺点：表名太长
-- 解决：表起别名
SELECT e.empno, e.ename, e.sal, d.dname, d.loc FROM emp e NATURAL JOIN dept d;

-- 自然连接 natural join 缺点：自动匹配表中所有的同名列，但是我们有时候希望只匹配部分同名列
-- 解决：using子句
SELECT * FROM emp e JOIN dept d USING (deptno);	-- 这里不能写natural join了，这里是内连接

-- USING缺点：关联的字段必须同名
-- 解决：内连接 - ON子句
SELECT * FROM emp e INNER JOIN dept d ON (e.deptno = d.deptno);

-- 外连接：除了显示匹配的数据外，还可以显示不匹配的数据 OUTER可以省略

-- 左外连接：left outer join
SELECT * FROM emp e LEFT OUTER JOIN dept d ON e.deptno = d.deptno;

-- 右外连接：right outer join 右面的那个表的信息即使不匹配也可以查看出效果
SELECT * FROM emp e RIGHT OUTER JOIN dept d ON e.deptno = d.deptno;

-- 全外连接 full outer join	-- 这个语法在mysql中不支持，在oracle中支持
-- SELECT * FROM emp e FULL OUTER JOIN dept d ON e.deptno = d.deptno;

-- 解决mysql中不支持全外连接的问题 UNION并集
SELECT * FROM emp e LEFT OUTER JOIN dept d ON e.deptno = d.deptno UNION SELECT * FROM emp e RIGHT OUTER JOIN dept d ON e.deptno = d.deptno;