SELECT * FROM emp e INNER JOIN dept d ON e.deptno = d.deptno;
SELECT
	e.ename,
	e.sal,
	e.empno,
	e.deptno,
	d.dname,
	s.* 
FROM
	emp e
	RIGHT JOIN dept d ON e.deptno = d.deptno
	INNER JOIN salgrade s ON e.sal BETWEEN s.losal 
	AND s.hisal;-- 自查询

SELECT
	e1.empno 员工编号,
	e1.ename 员工姓名,
	e1.mgr 领导编号,
	e2.ename 领导姓名 
FROM
	emp e1
	LEFT JOIN emp e2 ON e1.mgr = e2.empno;


-- 多行查询
-- 查询部门20中职务同部门10的雇员一样的雇员信息
SELECT * FROM emp WHERE deptno = 20 AND job IN (SELECT job FROM emp WHERE deptno = 10);
SELECT * FROM emp WHERE deptno = 20 AND job = ANY(SELECT job FROM emp WHERE deptno = 10);

-- 查询工资比所有的“SALESMAN”都高的雇员的编号，名字，工资
SELECT empno, ename, sal FROM emp WHERE sal > ALL(SELECT sal FROM emp WHERE job = 'salesman');
SELECT empno, ename, sal FROM emp WHERE sal > (SELECT MAX(sal) FROM emp WHERE job = 'salesman');

-- 查询工资低于任意一个‘clerk’的工资的雇员信息
SELECT * FROM emp WHERE sal < ANY(SELECT sal FROM emp WHERE job = 'clerk') AND job != 'clerk';
SELECT * FROM emp WHERE sal < (SELECT MAX(sal) FROM emp WHERE job = 'clerk') AND job != 'clerk';

-- 查询最高工资的员工信息（不相关子查询）
SELECT * FROM emp WHERE sal = (SELECT MAX(sal) FROM emp);

-- 查询本部门最高工资的员工（相关子查询）
SELECT * FROM emp WHERE deptno = 10 AND sal = (SELECT MAX(sal) FROM emp WHERE deptno = 10)
UNION
SELECT * FROM emp WHERE deptno = 20 AND sal = (SELECT MAX(sal) FROM emp WHERE deptno = 20)
UNION
SELECT * FROM emp WHERE deptno = 30 AND sal = (SELECT MAX(sal) FROM emp WHERE deptno = 30);

SELECT * FROM emp e WHERE sal = (SELECT MAX(sal) FROM emp WHERE deptno=e.deptno) ORDER BY deptno;

-- 查询工资高于所在岗位的平均工资的那些员工
SELECT * FROM emp WHERE job = 'clerk' and sal >= (SELECT AVG(sal) FROM emp WHERE job = 'clerk');

SELECT * FROM emp e WHERE sal >= (SELECT AVG(sal) FROM emp WHERE job = e.job);
