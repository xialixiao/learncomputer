## 二、MYSQL示例
# （1）管理表格
创建一个包含三列的新表
CREATE TABLE t (
    id    INT,
    name  VARCHAR DEFAULT NOT NULL,
    price INT DEFAULT 0
    PRIMARY KEY(id)
);
从数据库中删除表：
DROP TABLE t ;
向表中添加新列：
ALTER TABLE t ADD column;
从表中删除列c：
ALTER TABLE t DROP COLUMN c ;
添加约束：
ALTER TABLE t ADD constraint;
删除约束：
ALTER TABLE t DROP constraint;
将表从t1重命名为t2：
ALTER TABLE t1 RENAME TO t2;
将列 c1 重命名为 c2：
ALTER TABLE t1 CHANGE c1 c2 datatype;
ALTER TABLE table_name RENAME COLUMN c1 TO c2;
将列c1的数据类型改为datatype：
ALTER TABLE t1 MODIFY c1 datatype;
删除表中的所有数据：
TRUNCATE TABLE t;
# （2）从表中查询数据
从表中查询列c1、c2中的数据：
SELECT c1, c2 FROM t
查询表中的所有行和列：
SELECT * FROM t
查询数据并使用条件筛选行：
SELECT c1, c2 FROM t
WHERE condition
查询表中的不同行：
SELECT DISTINCT c1 FROM t
WHERE condition
按升序或降序对结果集排序：
SELECT c1, c2 FROM t
ORDER BY c1 ASC [DESC]
跳过行的偏移并返回下n行：
SELECT c1, c2 FROM t
ORDER BY c1 
LIMIT n OFFSET offset
使用聚合函数对行进行分组：
SELECT c1, aggregate(c2)
FROM t
GROUP BY c1
使用HAVING子句筛选组：
SELECT c1, aggregate(c2)
FROM t
GROUP BY c1
HAVING condition
# （3）从多个表查询
内部连接 t1 和 t2：
SELECT c1, c2 
FROM t1
INNER JOIN t2 ON condition
左连接t1和t1：
SELECT c1, c2 
FROM t1
LEFT JOIN t2 ON condition
右连接t1和t2：
SELECT c1, c2 
FROM t1
RIGHT JOIN t2 ON condition
执行完全外部连接：
SELECT c1, c2 
FROM t1
FULL OUTER JOIN t2 ON condition
生成表中行的笛卡尔积：
SELECT c1, c2 
FROM t1
CROSS JOIN t2
执行交叉连接的另一种方法：
SELECT c1, c2 
FROM t1, t2
使用INNER Join子句将t1连接到自身：
SELECT c1, c2
FROM t1 A
INNER JOIN t1 B ON condition
使用SQL运算符，合并两个查询中的行：
SELECT c1, c2 FROM t1
UNION [ALL]
SELECT c1, c2 FROM t2
返回两个查询的交集：
SELECT c1, c2 FROM t1
INTERSECT
SELECT c1, c2 FROM t2
从另一个结果集中减去一个结果集：
SELECT c1, c2 FROM t1
MINUS
SELECT c1, c2 FROM t2
使用模式匹配%查询行_：
SELECT c1, c2 FROM t1
WHERE c1 [NOT] LIKE pattern
查询列表中的行：
SELECT c1, c2 FROM t
WHERE c1 [NOT] IN value_list
查询两个值之间的行：
SELECT c1, c2 FROM t
WHERE  c1 BETWEEN low AND high
检查表中的值是否为NULL：
SELECT c1, c2 FROM t
WHERE  c1 IS [NOT] NULL
# （7）使用sql约束
将c1和c2设置为主键：
CREATE TABLE t(
    c1 INT, c2 INT, c3 VARCHAR,
    PRIMARY KEY (c1,c2)
);
将c2列设置为外键：
CREATE TABLE t1(
    c1 INT PRIMARY KEY,  
    c2 INT,
    FOREIGN KEY (c2) REFERENCES t2(c2)
);
使c1和c2中的值唯一：
CREATE TABLE t(
    c1 INT, c1 INT,
    UNIQUE(c2,c3)
);
确保c1>0和c1>=c2中的值：
CREATE TABLE t(
  c1 INT, c2 INT,
  CHECK(c1> 0 AND c1 >= c2)
);
c2列中的设置值不为NULL：
CREATE TABLE t(
     c1 INT PRIMARY KEY,
     c2 VARCHAR NOT NULL
);
# （8）修改数据
在表格中插入一行：
INSERT INTO t(column_list)
VALUES(value_list);
在表格中插入多行：
INSERT INTO t(column_list)
VALUES (value_list), 
       (value_list), …;
将行从t2插入t1：
INSERT INTO t1(column_list)
SELECT column_list
FROM t2;
更新列c1中所有行的新值：
UPDATE t
SET c1 = new_value;
更新列c1、c2中与条件匹配的值：
UPDATE t
SET c1 = new_value, 
        c2 = new_value
WHERE condition;
删除表中的所有数据：
DELETE FROM t;
删除表中的行子集：
DELETE FROM t
WHERE condition;
# (9)管理视图
创建由c1和c2组成的新视图：
CREATE VIEW v(c1,c2) 
AS
SELECT c1, c2
FROM t;
使用选中选项创建新视图：
CREATE VIEW v(c1,c2) 
AS
SELECT c1, c2
FROM t;
WITH [CASCADED | LOCAL] CHECK OPTION;
创建递归视图：
CREATE RECURSIVE VIEW v 
AS
select-statement -- anchor part
UNION [ALL]
select-statement; -- recursive part
创建临时视图：
CREATE TEMPORARY VIEW v 
AS
SELECT c1, c2
FROM t;
删除视图：
DROP VIEW view_name;
# （10）管理触发器
创建或修改触发器：
CREATE OR MODIFY TRIGGER trigger_name
WHEN EVENT
ON table_name TRIGGER_TYPE
EXECUTE stored_procedure;
            WHEN
BEFORE	在事件发生前调用
AFTER	事件发生后调用
            EVENT
INSERT	为INSERT调用
UPDATE	调用UPDATE
DELETE	调用DELETE
            TRIGGER_TYPE
FOR EACH ROW	-
FOR EACH STATEMENT  -
# （11）管理索引
在t表的c1和c2上创建索引：
CREATE INDEX idx_name 
ON t(c1,c2);
在t表的c3、c4上创建唯一索引：
CREATE UNIQUE INDEX idx_name
ON t(c3,c4)
删除索引：
DROP INDEX idx_name ON t;
