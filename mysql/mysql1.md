## 一、入门
# (1)介绍
MySQL 为关系型数据库(Relational Database Management System)，一个关系型数据库由一个或数个表格组成，如下所示的一个表格
    name ▼ 键            ▼ 列(col)
┌┈┈┈┈┬┈┈┈┈┈┈┈┈┬┈┈┈┈┈┈┬┈┈┈┈┈┈┈┐
┆ id ┆ name   ┆ uid  ┆ level ┆  ◀ 表头header
├┈┈┈┈┼┈┈┈┈┈┈┈┈┤┈┈┈┈┈┈┤┈┈┈┈┈┈┈┤
┆  1 ┆ mysql  ┆ 0    ┆ 3     ┆
├┈┈┈┈┼┈┈┈┈┈┈┈┈┤┈┈┈┈┈┈┤┈┈┈┈┈┈┈┤
┆  2 ┆ redis  ┆ 12   ┆ 1     ┆  ◀ 行 row
└┈┈┈┈┴┈┈┈┈┈┈┈┈┴┈┈┈┈┈┈┴┈┈┈┈┈┈┈┘
    redis ▲ 值
表头(header) 每一列的名称
列(col) 具有相同数据类型的数据的集合
值(value) 行的具体信息，每个值与该列数据类型相同
键(key) 用来识别某个特定的人/物的方法，有唯一性
# (2) 登录Mysql
* 默认用户名<root>，-p 是密码，
* ⚠️参数后面不需要空格
mysql -h 127.0.0.1 -u <用户名> -p<密码>
mysql -D 数据库名 -h 主机名 -u 用户名 -p
mysql -h <host> -P <端口号> -u <user> -p [db_name]
mysql -h <host> -u <user> -p [db_name]
# （3）查看MYSQL信息
mysql> status;：显示当前mysql的version的各种信息
mysql> select version(); ：显示当前mysql的version信息
mysql> show global variables like 'port';：# 查看 MySQL 端口号
# （4）退出mysql
mysql> exit ：退出 quit; 或 \q; 一样的效果
# （5）常用的
（5.1）数据库 Database
CREATE DATABASE db ;	创建数据库
SHOW DATABASES;	列出数据库
USE db;	切换到数据库
CONNECT db ;	切换到数据库
DROP DATABASE db;	删除数据库
（5.2）表 Table
SHOW TABLES;	列出当前数据库的表
SHOW FIELDS FROM t;	表的列表字段
DESC t;	显示表格结构
SHOW CREATE TABLE t;	显示创建表sql
TRUNCATE TABLE t;	删除表中的所有数据
DROP TABLE t;	删除表格
（5.3）Proccess
show processlist;	列出进程
kill pid;	杀死进程
# （6）备份
备份特定表：
mysqldump -u user -p db_name table1 table2 > tables_backup.sql
备份多个数据库：
mysqldump -u user -p --databases db1 db2 > multi_backup.sql
备份所有数据库：
mysqldump -u user -p --all-databases > all_backup.sql
备份时压缩：
mysqldump -u user -p db_name | gzip > db_backup.sql.gz
导出不带架构的数据库：
mysqldump -u user -p db_name --no-data=true --add-drop-table=false > db.sql
仅导出数据：
mysqldump -u user -p --no-create-info db_name > only_data.sql
仅导出结构：
mysqldump -u user -p --no-data db_name > only_schema.sql
导出时忽略某些表：
mysqldump -u user -p db_name --ignore-table=db_name.table1 --ignore-table=db_name.table2 > partial.sql
# （7）恢复备份
恢复单个数据库备份：
mysql -u user -p db_name < db_backup.sql
恢复多个数据库（带 --databases 选项备份的）：
mysql -u user -p < multi_backup.sql
恢复所有数据库（使用 --all-databases 备份的）：
mysql -u user -p < all_backup.sql
从 gzip 压缩的备份恢复：
gunzip < db_backup.sql.gz | mysql -u user -p db_name
或：
zcat db_backup.sql.gz | mysql -u user -p db_name
恢复单张表（从 mysqldump 单表导出文件）：
mysql -u user -p db_name < table1_backup.sql
先创建数据库再导入（如果备份中不包含 CREATE DATABASE）：
mysql -u user -p -e "CREATE DATABASE IF NOT EXISTS db_name;"
mysql -u user -p db_name < db_backup.sql
恢复指定字符集（防止乱码）：
mysql --default-character-set=utf8mb4 -u user -p db_name < db_backup.sql
恢复时跳过某些错误（如重复键）：
mysql -u user -p --force db_name < db_backup.sql
恢复到远程主机数据库：
mysql -h remote_host -u user -p db_name < db_backup.sql
# （8）错误处理（Error Handing）
SHOW ERRORS;	显示最近的错误
SHOW WARNINGS;	显示最近的警告
SHOW COUNT(*) ERRORS;	显示错误数量
SHOW COUNT(*) WARNINGS;	显示警告数量
EXPLAIN SELECT ...;	分析查询执行计划
SHOW ENGINE INNODB STATUS;	查看 InnoDB 状态和死锁信息
SHOW PROFILE;	显示语句的资源消耗（需开启 profiling）
SHOW PROFILES;	显示所有已记录的 profiling 数据
SHOW PROCESSLIST;	查看当前线程，排查长时间运行或阻塞的语句
SHOW STATUS LIKE 'Last_error%';	查看上次语句执行的错误信息
SHOW VARIABLES LIKE 'log_%';	查看错误日志相关配置
SHOW BINARY LOGS;	查看二进制日志，排查事务或复制异常
SHOW SLAVE STATUS\G	查看主从复制错误（用于主从复制场景）
SHOW MASTER STATUS;	查看主库状态，辅助分析复制问题