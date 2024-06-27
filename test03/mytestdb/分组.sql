-- 统计各部门的平均工资
SELECT deptno, AVG(sal) FROM emp GROUP BY deptno;	-- 字段与多行函数不可以同时使用，除非这个字段属于分组


-- 统计各个岗位的平均工资
SELECT job, AVG(sal) FROM emp GROUP BY job;

-- 统计各个部门的平均工资，只显示平均工资大于2000以上的
SELECT deptno, AVG(sal) FROM emp GROUP BY deptno HAVING AVG(sal) > 2000 ORDER BY deptno DESC;
-- 统计各个岗位的平均工资，除了manager
-- 方法1
SELECT job, AVG(sal) FROM emp WHERE job != 'MANAGER' GROUP BY job;
-- 方法2
SELECT job, AVG(sal) FROM emp GROUP BY job HAVING job != 'MANAGER';
-- WHERE是在分组前过滤的，HAVING是在分组后过滤的

-- 固定顺序select--from--where--group by--having--order by

-- 列出工资最小值小于2000的职位
SELECT job, MIN(sal) FROM emp GROUP BY job HAVING MIN(sal) < 2000;

-- 列出平均工资大于1200的部门和工作搭配组合
SELECT deptno, job, avg(sal) FROM emp GROUP BY deptno, job HAVING AVG(sal) > 1200 ORDER BY deptno;

-- 统计人数数小于4的部门的平均工资
SELECT deptno, COUNT(ename) FROM emp GROUP BY deptno HAVING COUNT(ename) < 4;

-- 统计各部门的最高工资，排除最高工资小于3000的部门
SELECT deptno, MAX(sal) FROM emp GROUP BY deptno HAVING MAX(sal) >= 3000;