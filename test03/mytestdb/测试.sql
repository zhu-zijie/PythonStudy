SELECT *
FROM emp e
INNER JOIN dept d
ON e.deptno = d.deptno;

SELECT e.ename, e.sal, e.empno, e.deptno, d.dname, s.*
FROM emp e
RIGHT JOIN dept d
ON e.deptno = d.deptno
INNER JOIN salgrade s
ON e.sal BETWEEN s.losal AND s.hisal;

-- 自查询
SELECT e1.empno 员工编号, e1.ename 员工姓名, e1.mgr 领导编号, e2.ename 领导姓名 FROM emp e1 LEFT JOIN emp e2 on e1.mgr = e2.empno;