# [SQLITE](http://www.runoob.com/sqlite/sqlite-where-clause.html)

### sqlite parameters
```
sqlite> .help
.auth ON|OFF           Show authorizer callbacks
.backup ?DB? FILE      Backup DB (default "main") to FILE
.bail on|off           Stop after hitting an error.  Default OFF
.binary on|off         Turn binary output on or off.  Default OFF
.changes on|off        Show number of rows changed by SQL
.clone NEWDB           Clone data into NEWDB from the existing database
.databases             List names and files of attached databases
.dbinfo ?DB?           Show status information about the database
.dump ?TABLE? ...      Dump the database in an SQL text format
                         If TABLE specified, only dump tables matching
                         LIKE pattern TABLE.
.echo on|off           Turn command echo on or off
.eqp on|off|full       Enable or disable automatic EXPLAIN QUERY PLAN
.exit                  Exit this program
.explain ?on|off|auto? Turn EXPLAIN output mode on or off or to automatic
.fullschema ?--indent? Show schema and the content of sqlite_stat tables
.headers on|off        Turn display of headers on or off
.help                  Show this message
.import FILE TABLE     Import data from FILE into TABLE
.indexes ?TABLE?       Show names of all indexes
                         If TABLE specified, only show indexes for tables
                         matching LIKE pattern TABLE.
.limit ?LIMIT? ?VAL?   Display or change the value of an SQLITE_LIMIT
.load FILE ?ENTRY?     Load an extension library
.log FILE|off          Turn logging on or off.  FILE can be stderr/stdout
.mode MODE ?TABLE?     Set output mode where MODE is one of:
                         ascii    Columns/rows delimited by 0x1F and 0x1E
                         csv      Comma-separated values
                         column   Left-aligned columns.  (See .width)
                         html     HTML <table> code
                         insert   SQL insert statements for TABLE
                         line     One value per line
                         list     Values delimited by .separator strings
                         tabs     Tab-separated values
                         tcl      TCL list elements
.nullvalue STRING      Use STRING in place of NULL values
.once FILENAME         Output for the next SQL command only to FILENAME
.open ?FILENAME?       Close existing database and reopen FILENAME
.output ?FILENAME?     Send output to FILENAME or stdout
.print STRING...       Print literal STRING
.prompt MAIN CONTINUE  Replace the standard prompts
.quit                  Exit this program
.read FILENAME         Execute SQL in FILENAME
.restore ?DB? FILE     Restore content of DB (default "main") from FILE
.save FILE             Write in-memory database into FILE
.scanstats on|off      Turn sqlite3_stmt_scanstatus() metrics on or off
.schema ?PATTERN?      Show the CREATE statements matching PATTERN
                          Add --indent for pretty-printing
.separator COL ?ROW?   Change the column separator and optionally the row
                         separator for both the output mode and .import
.shell CMD ARGS...     Run CMD ARGS... in a system shell
.show                  Show the current values for various settings
.stats ?on|off?        Show stats or turn stats on or off
.system CMD ARGS...    Run CMD ARGS... in a system shell
.tables ?TABLE?        List names of tables
                         If TABLE specified, only list tables matching
                         LIKE pattern TABLE.
.timeout MS            Try opening locked tables for MS milliseconds
.timer on|off          Turn SQL timer on or off
.trace FILE|off        Output each SQL statement as it is run
.vfsinfo ?AUX?         Information about the top-level VFS
.vfslist               List all available VFSes
.vfsname ?AUX?         Print the name of the VFS stack
.width NUM1 NUM2 ...   Set column widths for "column" mode
                         Negative values right-justify

```


### 查看数据库
```
$ sqlite3 ath.db
SQLite version 3.13.0 2016-05-18 10:57:30
Enter ".help" for usage hints.
sqlite> .database
seq  name             file                                                      
---  ---------------  ----------------------------------------------------------
0    main             /home/wzk/database/geneontology/sqlite_test/ath.db 
sqlite> .table
Diseases              GeneGos               GoSlims             
GeneDiseases          GenePathways          Gos                 
GeneEnsemblGeneIds    GeneRefSeqProteinIds  Orthologs           
GeneEntrezGeneIds     GeneUniprotkbAcs      Pathways            
GeneGoSlims           Genes               
sqlite> .schema GenePathways
CREATE TABLE GenePathways
(
    gid TEXT,
    pid INTEGER,
    PRIMARY KEY (gid, pid)
);

```

### 查看概况
```
sqlite> .schema Diseases
CREATE TABLE Diseases
(
    did INTEGER PRIMARY KEY,
    db TEXT,
    id TEXT,
    name TEXT
);

s
```



### 删除表
```
DROP TABLE database_name.table_name;
```

### Insert 语句
```
INSERT INTO TABLE_NAME [(column1, column2, column3,...columnN)]  
VALUES (value1, value2, value3,...valueN);
```
在这里，column1, column2,...columnN 是要插入数据的表中的列的名称。
如果要为表中的所有列添加值，您也可以不需要在 SQLite 查询中指定列名称。但要确保值的顺序与列在表中的顺序一致。SQLite 的 INSERT INTO 语法如下：
```
INSERT INTO TABLE_NAME VALUES (value1,value2,value3,...valueN);
```


### 使用一个表来填充另一个表
通过在一个有一组字段的表上使用 select 语句，填充数据到另一个表中。下面是语法：
```
INSERT INTO first_table_name [(column1, column2, ... columnN)] 
   SELECT column1, column2, ...columnN 
   FROM second_table_name
   [WHERE condition];
```

### Select 语句
```
SELECT column1, column2, columnN FROM table_name;
```
在这里，column1, column2...是表的字段，他们的值即是您要获取的。如果您想获取所有可用的字段，那么可以使用下面的语法：
```
SELECT * FROM table_name;
```
下面是一个实例，使用 SELECT 语句获取并显示所有这些记录。在这里，前三个命令被用来设置正确格式化的输出。
```
sqlite>.header on
sqlite>.mode column
sqlite> SELECT * FROM COMPANY;
```

### 设置输出列的宽度
有时，由于要显示的列的默认宽度导致 .mode column，这种情况下，输出被截断。此时，您可以使用 .width num, num.... 命令设置显示列的宽度，如下所示：
```
sqlite>.width 10, 20, 10
sqlite>SELECT * FROM COMPANY;
```

### Schema 信息
因为所有的点命令只在 SQLite 提示符中可用，所以当您进行带有 SQLite 的编程时，您要使用下面的带有 sqlite_master 表的 SELECT 语句来列出所有在数据库中创建的表：
```
sqlite> SELECT tbl_name FROM sqlite_master WHERE type = 'table';
```
您可以列出关于 COMPANY 表的完整信息，如下所示：
```
sqlite> SELECT sql FROM sqlite_master WHERE type = 'table' AND tbl_name = 'COMPANY';
```


### SQLite 比较运算符
```
运算符 描述  实例
==  检查两个操作数的值是否相等，如果相等则条件为真。    (a == b) 不为真。
=   检查两个操作数的值是否相等，如果相等则条件为真。    (a = b) 不为真。
!=  检查两个操作数的值是否相等，如果不相等则条件为真。   (a != b) 为真。
<>  检查两个操作数的值是否相等，如果不相等则条件为真。   (a <> b) 为真。
>   检查左操作数的值是否大于右操作数的值，如果是则条件为真。    (a > b) 不为真。
<   检查左操作数的值是否小于右操作数的值，如果是则条件为真。    (a < b) 为真。
>=  检查左操作数的值是否大于等于右操作数的值，如果是则条件为真。  (a >= b) 不为真。
<=  检查左操作数的值是否小于等于右操作数的值，如果是则条件为真。  (a <= b) 为真。
!<  检查左操作数的值是否不小于右操作数的值，如果是则条件为真。   (a !< b) 为假。
!>  检查左操作数的值是否不大于右操作数的值，如果是则条件为真。   (a !> b) 为真。
```

### SQLite 逻辑运算符
```

运算符 描述
AND AND 运算符允许在一个 SQL 语句的 WHERE 子句中的多个条件的存在。
BETWEEN BETWEEN 运算符用于在给定最小值和最大值范围内的一系列值中搜索值。
EXISTS  EXISTS 运算符用于在满足一定条件的指定表中搜索行的存在。
IN  IN 运算符用于把某个值与一系列指定列表的值进行比较。
NOT IN  IN 运算符的对立面，用于把某个值与不在一系列指定列表的值进行比较。
LIKE    LIKE 运算符用于把某个值与使用通配符运算符的相似值进行比较。
GLOB    GLOB 运算符用于把某个值与使用通配符运算符的相似值进行比较。GLOB 与 LIKE 不同之处在于，它是大小写敏感的。
NOT NOT 运算符是所用的逻辑运算符的对立面。比如 NOT EXISTS、NOT BETWEEN、NOT IN，等等。它是否定运算符。
OR  OR 运算符用于结合一个 SQL 语句的 WHERE 子句中的多个条件。
IS NULL NULL 运算符用于把某个值与 NULL 值进行比较。
IS  IS 运算符与 = 相似。
IS NOT  IS NOT 运算符与 != 相似。
||  连接两个不同的字符串，得到一个新的字符串。
UNIQUE  UNIQUE 运算符搜索指定表中的每一行，确保唯一性（无重复）。
```

下面的 SELECT 语句列出了 AGE 大于等于 25 且工资大于等于 65000.00 的所有记录：
```
sqlite> SELECT * FROM COMPANY WHERE AGE >= 25 AND SALARY >= 65000;
```

下面的 SELECT 语句列出了 AGE 不为 NULL 的所有记录，结果显示所有的记录，意味着没有一个记录的 AGE 等于 NULL：
```
sqlite>  SELECT * FROM COMPANY WHERE AGE IS NOT NULL;
```

下面的 SELECT 语句列出了 NAME 以 'Ki' 开始的所有记录，'Ki' 之后的字符不做限制：
```
sqlite> SELECT * FROM COMPANY WHERE NAME LIKE 'Ki%';
```

下面的 SELECT 语句列出了 NAME 以 'Ki' 开始的所有记录，'Ki' 之后的字符不做限制：
```
sqlite> SELECT * FROM COMPANY WHERE NAME GLOB 'Ki*';
```

下面的 SELECT 语句列出了 AGE 的值为 25 或 27 的所有记录：
```
sqlite> SELECT * FROM COMPANY WHERE AGE IN ( 25, 27 );
```

下面的 SELECT 语句列出了 AGE 的值既不是 25 也不是 27 的所有记录：
```
sqlite> SELECT * FROM COMPANY WHERE AGE NOT IN ( 25, 27 );
```

下面的 SELECT 语句列出了 AGE 的值在 25 与 27 之间的所有记录：
```
sqlite> SELECT * FROM COMPANY WHERE AGE BETWEEN 25 AND 27;
```

下面的 SELECT 语句使用 SQL 子查询，子查询查找 SALARY > 65000 的带有 AGE 字段的所有记录，后边的 WHERE 子句与 EXISTS 运算符一起使用，列出了外查询中的 AGE 存在于子查询返回的结果中的所有记录：
```
sqlite> SELECT AGE FROM COMPANY 
        WHERE EXISTS (SELECT AGE FROM COMPANY WHERE SALARY > 65000);
```

下面的 SELECT 语句使用 SQL 子查询，子查询查找 SALARY > 65000 的带有 AGE 字段的所有记录，后边的 WHERE 子句与 > 运算符一起使用，列出了外查询中的 AGE 大于子查询返回的结果中的年龄的所有记录：
```
sqlite> SELECT * FROM COMPANY 
        WHERE AGE > (SELECT AGE FROM COMPANY WHERE SALARY > 65000);
```


### SQLite 表达式
#### SQLite - 布尔表达式
SQLite 的布尔表达式在匹配单个值的基础上获取数据。语法如下：
```
SELECT column1, column2, columnN 
FROM table_name 
WHERE SINGLE VALUE MATCHTING EXPRESSION;
```

下面的实例演示了 SQLite 布尔表达式的用法：
```
sqlite> SELECT * FROM COMPANY WHERE SALARY = 10000;
```

#### SQLite - 数值表达式
这些表达式用来执行查询中的任何数学运算。语法如下：
```
SELECT numerical_expression as  OPERATION_NAME
[FROM table_name WHERE CONDITION] ;
```

在这里，numerical_expression 用于数学表达式或任何公式。下面的实例演示了 SQLite 数值表达式的用法：
```
sqlite> SELECT (15 + 6) AS ADDITION
ADDITION = 21
```

有几个内置的函数，比如 avg()、sum()、count()，等等，执行被称为对一个表或一个特定的表列的汇总数据计算。
```
sqlite> SELECT COUNT(*) AS "RECORDS" FROM COMPANY; 
RECORDS = 7
```

#### SQLite - 日期表达式
日期表达式返回当前系统日期和时间值，这些表达式将被用于各种数据操作。
```
sqlite>  SELECT CURRENT_TIMESTAMP;
CURRENT_TIMESTAMP = 2013-03-17 10:43:35
```


### create index
```
 本例会创建一个简单的索引，名为 "personsindex"，在 persons表的 id列:
create index personsindex on persons(id asc);

如果您希望以降序索引某个列中的值，您可以在列名称之后添加保留字 desc:
create index personsindex on persons(id desc);

假如您希望索引不止一个列，您可以在括号中列出这些列的名称，用逗号隔开:
create index personsindex on persons(id, name);

.indices testtable
查看索引

```

### delete index
```
drop index  if exists personindex
```

### reindex 
重建索引用于删除已经存在的索引，同时基于其原有的规则重建该索引。这里需要说明的是，如果在REINDEX语句后面没有给出数据库名，那么当前连接下所有Attached数据库中所有索引都会被重建。如果指定了数据库名和表名，那么该表中的所有索引都会被重建，如果只是指定索引名，那么当前数据库的指定索引被重建。
```
reindex;
reindex testtable;
```

### 数据分析
和PostgreSQL非常相似，SQLite中的ANALYZE命令也同样用于分析数据表和索引中的数据，并将统计结果存放于SQLite的内部系统表中，以便于查询优化器可以根据分析后的统计数据选择最优的查询执行路径，从而提高整个查询的效率。见如下示例：
```
--如果在ANALYZE命令之后没有指定任何参数，则分析当前连接中所有Attached数据库中的表和索引。
sqlite> ANALYZE;
--如果指定数据库作为ANALYZE的参数，那么该数据库下的所有表和索引都将被分析并生成统计数据。
sqlite> ANALYZE main;
--如果指定了数据库中的某个表或索引为ANALYZE的参数，那么该表和其所有关联的索引都将被分析。
sqlite> ANALYZE main.testtable;
sqlite> ANALYZE main.testtable_idx2;
```


### 数据清理
和PostgreSQL中的VACUUM命令相比，他们的功能以及实现方式非常相似，不同的是PostgreSQL提供了更细的粒度，而SQLite只能将该命令作用于数据库，无法再精确到数据库中指定的数据表或者索引，然而这一点恰恰是PostgreSQL可以做到的。
    当某个数据库中的一个或多个数据表存在大量的插入、更新和删除等操作时，将会有大量的磁盘空间被已删除的数据所占用，在没有执行VACUUM命令之前，SQLite并没有将它们归还于操作系统。由于该类数据表中的数据存储非常分散，因此在查询时，无法得到更好的批量IO读取效果，从而影响了查询效率。
    在SQLite中，仅支持清理当前连接中的主数据库，而不能清理其它Attached数据库。VACUUM命令在完成数据清理时采用了和PostgreSQL相同的策略，即创建一个和当前数据库文件相同大小的新数据库文件，之后再将该数据库文件中的数据有组织的导入到新文件中，其中已经删除的数据块将不会被导入，在完成导入后，收缩新数据库文件的尺寸到适当的大小。该命令的执行非常简单，如：
```
sqlite> VACUUM;
```

SQL指令都是以分号（;）结尾的。如果遇到两个减号（--）则代表注解，sqlite3会略过去


```
.exit
.quit
.help
.database
.table (.tables)
.schema
```

### create table
```
create table contact(id integer primary key autoincrement, lastname varchar(20),firstname varchar(20), mobile varchar(30), telephone varchar(20), email  varchar(30), company varchar(50), department varchar(16),address varchar(80), id1 interger,id2 integer, updatetime datetime);
```

### insert record
```
insert into contact(lastname,firstname,mobile,telephone,updatetime) values('刘','畅','13910128132','010-81749136','2009-07-22');
```

### delete table
```
drop table contact;
```

### delete data from table 
```
deleta from contact;
```

### set the string of separating
```
.separator ","
.import ./contact.txt contact
```

### select record
```
select * from film order by year limit 10;
select * from film order by year desc limit 10;
select count(*) from film

```



### Export SQLite Database to a CSV file
```
>sqlite3 c:/sqlite/chinook.db
sqlite> .headers on
sqlite> .mode csv
sqlite> .output data.csv
sqlite> SELECT customerid,
   ...>        firstname,
   ...>        lastname,
   ...>        company
   ...>   FROM customers;
sqlite> .quit
```

```
>sqlite3 -header -csv c:/sqlite/chinook.db "select * from tracks;" > tracks.csv
```

```
>sqlite3 -header -csv c:/sqlite/chinook.db < query.sql > data.csv
```




### The SQLite Dump Command
```
>sqlite3 c:/sqlite/chinook.db
sqlite> .output c:/sqlite/chinook.sql
sqlite> .dump
sqlite> .exit

```

### Dump a specific table using the SQLite dump command
the following command saves the albums table to the albums.sql file
```
sqlite> .output c:/sqlite/albums.sql
sqlite> .dump albums
sqlite> .quit
```

### Dump tables structure only using schema command
```
sqlite> .output c:/sqlite/chinook_structure.sql
sqlite> .schema
sqlite> .quit
```

### Dump data of one or more tables into a file
First, set the mode to *insert* using the *.mode* command as follows:
```
sqlite> .mode insert
```
From now on, every SELECT statement will issue the result as the INSERT statements instead of pure text data.

Second, set the output to a text file instead of the default standard output. The following command sets the output file to the *data.sql* file.
```
sqlite> .output data.sql
```

Third, issue the SELECT statements to query data from a table that you want to dump. The following command returns data from the *artists* table.
```
sqlite> select * from artists;
```


### .sql to .db
```
sqlite> .read db.sql
```
or
```
cat db.sql | sqlite3 database.db
```
or
```
sqlite3 database.sqlite3 < db.sql
```

