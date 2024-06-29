-- 定义一个没有返回值的存储过程
-- 实现：模糊查询操作
SELECT * FROM emp WHERE ename LIKE '%A%';

CREATE PROCEDURE mypro01 (name VARCHAR(10))
BEGIN
	IF name IS NULL OR name = '' THEN
		SELECT * FROM emp;
	ELSE
		SELECT * FROM emp WHERE ename LIKE CONCAT('%',name,'%');
	END IF;
END; 

-- 删除存储过程
DROP PROCEDURE mypro01;

-- 调用存储过程
CALL mypro01(NULL);
CALL mypro01('R');

-- 定义一个有返回值的存储过程
-- 参数前面的in可以不写，FOUND_ROWS()返回结果的条数
CREATE PROCEDURE mypro02 (IN name VARCHAR(10), OUT num INT(3))
BEGIN
	IF name IS NULL OR name = '' THEN
		SELECT * FROM emp;
	ELSE
		SELECT * FROM emp WHERE ename LIKE CONCAT('%',name,'%');
	END IF;
	SELECT FOUND_ROWS() INTO num;
END; 

-- 调用存储过程
CALL mypro02(NULL, @num);
SELECT @num;

CALL mypro02('R', @aaa);
SELECT @aaa;