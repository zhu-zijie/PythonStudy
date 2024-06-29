-- 创建/替换单表视图
CREATE OR REPLACE VIEW myview01 AS SELECT empno, ename, job, deptno FROM emp WHERE deptno = 20 WITH CHECK OPTION;

-- 查看视图
SELECT * FROM myview01;

-- 在视图中插入数据
INSERT INTO myview01 (empno, ename, job, deptno) VALUES (9999, 'lili', 'CLERK', 20);
INSERT INTO myview01 (empno, ename, job, deptno) VALUES (8888, 'nana', 'CLERK', 30);

-- 创建/替换多表视图
CREATE OR REPLACE VIEW myview02 AS SELECT e.empno, e.ename, e.sal, d.deptno, d.dname FROM emp e JOIN dept d ON e.deptno = d.deptno WHERE sal > 2000;

SELECT * from myview02;

-- 创建统计视图
CREATE OR REPLACE VIEW myview03 AS SELECT e.deptno, d.dname, avg(sal), min(sal), count(*) FROM emp e JOIN dept d USING (deptno) GROUP BY e.deptno;

SELECT * FROM myview03 ORDER BY deptno;

-- 创建基于视图的视图
CREATE OR REPLACE VIEW myview04 AS SELECT * FROM myview03 WHERE deptno = 20;
SELECT * FROM myview04;


