## 四、函数
# （1）聚合函数
SUM()	计算一列值的总和
AVG()	计算一列值的平均值
COUNT()	计算行数，可选择性地忽略NULL值
MAX()	找出一列的最大值
MIN()	找出一列的最小值
GROUP_CONCAT()	将一组值连接成单一字符串，可指定分隔符，常用于分组。
# （2）数字函数
ABS(x)	返回数值的绝对值	ABS(-5)	5
ROUND(x,y)	四舍五入到指定的小数位数，y为小数位数，默认为0	ROUND(3.1415,2)	3.14
FLOOR(x)	向下取整至最接近的整数	FLOOR(3.7)	3
CEIL(x)	向上取整至最接近的整数	CEIL(3.3)	4
SQRT(x)	返回一个数的平方根	SQRT(16)	4
MOD(x,y)	返回x除以y的余数	MOD(10,3)	1
RAND([seed])	返回0到1之间的随机数，可选种子值	RAND() 或 RAND(123)	0.345...
# （3）日期和时间函数
NOW()	返回当前日期和时间
CURDATE()	返回当前日期
CURTIME()	返回当前时间
DATE_FORMAT()	格式化日期时间输出
DATEDIFF()	计算两个日期之间相差的天数
STR_TO_DATE()	将字符串转换为日期格式
# （4）字符串函数
CONCAT(s1,s2,...)	连接两个或更多字符串	CONCAT('Hello, ','World!')	'Hello, World!'
LOWER(str)	转换为小写	LOWER('HELLO')	'hello'
UPPER(str)	转换为大写	UPPER('world')	'WORLD'
TRIM(str)	去除字符串两端空格	TRIM(' Hello ')	'Hello'
LEFT(str,len)	提取字符串左侧的若干字符	LEFT('Hello', 3)	'Hel'
RIGHT(str,len)	提取字符串右侧的若干字符	RIGHT('Hello', 2)	'lo'
SUBSTR(str,pos,len)	提取字符串中的一部分	SUBSTR('Hello', 2, 3)	'ell'
REPLACE(str,from_str,to_str)	替换字符串中的部分文本	REPLACE('Hello', 'l', 'L')	'HeLLo'
# （5）高级函数
BIN(x)	返回 x 的二进制编码，x 为十进制数。	BIN(2)	10
BINARY(s)	将字符串 s 转换为二进制字符串。	BINARY 'RUNOOB'	'RUNOOB'（显示效果，实际存储为二进制）
CASE	复合条件函数，根据条件返回不同结果。	CASE WHEN 1 > 0 THEN '1 > 0' WHEN 2 > 0 THEN '2 > 0' ELSE '3 > 0' END	'1 > 0'
CAST(x AS type)	转换数据类型。	CAST('2017-08-29' AS DATE)	2017-08-29
COALESCE(expr1, expr2, ..., expr_n)	返回第一个非空表达式的值。	COALESCE(NULL, NULL, 'runoob.com', NULL, 'google.com')	'runoob.com'
CONNECTION_ID()	返回当前连接的唯一ID。	CONNECTION_ID()	4292835（示例值）
CONV(x, f1, f2)	将 f1 进制数转换为 f2 进制数。	CONV(15, 10, 2)	1111
CONVERT(s USING cs)	转换字符串 s 的字符集为 cs。	CHARSET(CONVERT('ABC' USING gbk))	gbk
CURRENT_USER()	返回当前用户。	CURRENT_USER()	guest@%
DATABASE()	返回当前数据库名。	DATABASE()	runoob
IF(expr, v1, v2)	条件表达式，expr 为真则 v1，否则 v2。	IF(1 > 0, '正确', '错误')	'正确'
IFNULL(v1, v2)	如果 v1 不为 NULL，则返回 v1，否则返回 v2。	IFNULL(NULL, 'Hello Word')	'Hello Word'
ISNULL(expression)	判断表达式是否为 NULL。	ISNULL(NULL)	1
LAST_INSERT_ID()	返回最近生成的 AUTO_INCREMENT 值。	LAST_INSERT_ID()	6（示例值）
NULLIF(expr1, expr2)	若 expr1 等于 expr2，则返回 NULL，否则返回 expr1。	NULLIF(25, 25)	NULL