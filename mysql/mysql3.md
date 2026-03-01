## 三、Mysql数据类型
# （1）Strings
CHAR	    String (0 - 255)
VARCHAR	    String (0 - 255)
TINYTEXT	String (0 - 255)
TEXT	    String (0 - 65535)
BLOB	    String (0 - 65535)
MEDIUMTEXT	String (0 - 16777215)
MEDIUMBLOB	String (0 - 16777215)
LONGTEXT	String (0 - 429496­7295)
LONGBLOB	String (0 - 429496­7295)
ENUM	    One of preset options
SET	        Selection of preset options
# （2）Date&time
DATE	    yyyy-MM-dd
TIME	    hh:mm:ss
DATETIME	yyyy-MM-dd hh:mm:ss
TIMESTAMP	yyyy-MM-dd hh:mm:ss
YEAR	    yyyy
# （3）Numeric
TINYINT x	Integer (-128 to 127)
SMALLINT x	Integer (-32768 to 32767)
MEDIUMINT x	Integer (-8388608 to 8388607)
INT x	    Integer (-2147­483648 to 214748­3647)
BIGINT x	Integer (-9223­372­036­854­775808 to 922337­203­685­477­5807)
FLOAT	    Decimal (precise to 23 digits)
DOUBLE	    Decimal (24 to 53 digits)
DECIMAL	    "­DOU­BLE­" stored as string
