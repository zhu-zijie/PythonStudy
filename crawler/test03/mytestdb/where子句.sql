-- 查看emp表
SELECT * FROM emp;

-- where子句：将过滤条件放在where后面，可以筛选出我们想要的数据
SELECT * FROM emp WHERE deptno = 20;
SELECT * FROM emp WHERE deptno <> 20;

-- 默认不区分大小写，加binary可以区分
SELECT * FROM emp WHERE BINARY job = 'clerk';
SELECT * FROM emp WHERE job = 'CLERK';

-- BETWEEN AND包含的意思
SELECT * from emp WHERE sal BETWEEN 1500 AND 3000;	-- [1500,3000]

-- 逻辑运算符&&与and，||与or
SELECT * FROM emp WHERE deptno = 10 || deptno = 20;
-- IN的用法
SELECT * FROM emp WHERE job IN ('manager', 'clerk', 'president');

-- WHERE子句+模糊查询
-- 查询名字中带A的员工,%代表任意多个字符0，1，2，...
SELECT * FROM emp WHERE ename LIKE '%A%';
-- 任意一个字符
SELECT * FROM emp WHERE ename LIKE '_A%';

-- 关于null的判断
SELECT * FROM emp WHERE comm IS NULL;
SELECT * FROM emp WHERE comm IS NOT NULL;

-- 小括号的使用
SELECT * FROM emp WHERE job = 'salasman' or job = 'clerk' and sal >= 1000
SELECT * FROM emp WHERE job = 'salasman' or (job = 'clerk' and sal >= 1000)
SELECT * FROM emp WHERE (job = 'salasman' or job = 'clerk') and sal >= 1000



