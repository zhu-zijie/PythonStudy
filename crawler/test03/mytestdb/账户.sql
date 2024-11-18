-- 创建账户表
CREATE TABLE account (
	id INT PRIMARY KEY auto_increment,
	uname VARCHAR(10) NOT NULL,
	balance DOUBLE
);

-- 查看账户表
SELECT * FROM account;
-- 在表中插入数据
INSERT INTO account VALUES (NULL, '丽丽', 2000), (NULL, '小刚', 2000);

-- 丽丽给小刚转200元
UPDATE account SET balance = balance - 200 WHERE id = 1;
UPDATE account SET balance = balance + 200 WHERE id = 2;
-- 默认一个DML语句是一个事务，所以上面的操作执行了2个事务

-- 必须让上面的两个操作控制在一个事务中
START TRANSACTION;

UPDATE account SET balance = balance - 200 WHERE id = 1;
UPDATE account SET balance = balance + 200 WHERE id = 2;

-- 手动回滚：刚才执行的操作全部取消
ROLLBACK;
-- 手动提交
COMMIT;
-- 在回滚和提交之前，数据库里的数据都是操作的缓存中的数据，而不是数据库里的真实数据

-- 查看默认的事务隔离级别 MySQL默认的是repeatable read
SELECT @@transaction_isolation;

SET SESSION TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED;
SET SESSION TRANSACTION ISOLATION LEVEL REPEATABLE READ;
SET SESSION TRANSACTION ISOLATION LEVEL SERIALIZABLE;