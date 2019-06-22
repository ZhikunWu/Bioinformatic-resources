##mysql 的安装 ******************(亲测可行) (From Fuchang Zhang)
cd /home/zhoulab/zclong/software/

wget https://cdn.mysql.com//Downloads/MySQL-5.6/mysql-5.6.38.tar.gz

tar -zvxf mysql-5.6.38.tar.gz

install_path=/home/zhoulab/zclong/software/mysql-5.6.38

cd $install_path

mkdir build

cd build

cmake .. -DCMAKE_INSTALL_PREFIX=$install_path -DMYSQL_DATADIR=$install_path/data -DMYSQL_UNIX_ADDR=$install_path/mysql.sock -DDEFAULT_CHARSET=utf8 -DDEFAULT_COLLATION=utf8_general_ci -DMYSQL_TCP_PORT=8701 -DWITH_INNOBASE_STORAGE_ENGINE=1 -DENABLED_LOCAL_INFILE=1 -DDOWNLOAD_BOOST=1 -DWITH_BOOST=$install_path

################################################################################
##如果中间报错，是因为没有下载 boost库，把它下载到$install_path中
cd $install_path
wget http://sourceforge.net/projects/boost/files/boost/1.59.0/boost_1_59_0.tar.gz
cd $install_path/downloaded/mysql-5.7.20

mkdir build
cd build
##然后再编译
cmake -DCMAKE_INSTALL_PREFIX=$install_path -DMYSQL_DATADIR=$install_path/data -DMYSQL_UNIX_ADDR=$install_path/mysql.sock -DDEFAULT_CHARSET=utf8 -DDEFAULT_COLLATION=utf8_general_ci -DMYSQL_TCP_PORT=8701 -DWITH_INNOBASE_STORAGE_ENGINE=1 -DENABLED_LOCAL_INFILE=1 -DDOWNLOAD_BOOST=1 -DWITH_BOOST=$install_path
################################################################################

##紧接着
make
make install
################################################################################
##如果报错，则  ******************(亲测可行)
tar xvf mysql-5.6.38.tar.gz

cd mysql-5.6.38

mkdir build

cd build

install_path=/home/zhoulab/zclong/software/mysql-5.6.38/

cmake .. -DCMAKE_INSTALL_PREFIX=$install_path -DMYSQL_TCP_PORT=3306 -DEXTRA_CHARSETS=complex -DWITH_SSL=system -DWITH_EMBEDDED_SERVER=1 -DENABLED_LOCAL_INFILE=1 -DWITH_PARTITION_STORAGE_ENGINE=1 -DWITH_INNOBASE_STORAGE_ENGINE=1 -DWITH_MYISAMMRG_STORAGE_ENGINE=1 -DENABLE_DTRACE=OFF -DMYSQL_UNIX_ADDR=$install_path/mysql.sock

make

make install
################################################################################
##如果报错，则(这个还没有测试过)
tar xvf mysql-5.6.38.tar.gz

cd mysql-5.6.38

cmake . -DCMAKE_INSTALL_PREFIX=/usr/local/mysql -DMYSQL_DATADIR=/usr/local/mysql/data -DSYSCONFDIR=/etc -DWITH_INNOBASE_STORAGE_ENGINE=1 -DWITH_ARCHIVE_STORAGE_ENGINE=1 -DWITH_BLACKHOLE_STORAGE_ENGINE=1 -DWITH_PARTITION_STORAGE_ENGINE=1 -DWITH_PERFSCHEMA_STORAGE_ENGINE=1 -DWITHOUT_EXAMPLE_STORAGE_ENGINE=1 -DWITHOUT_FEDERATED_STORAGE_ENGINE=1 -DDEFAULT_CHARSET=utf8 -DDEFAULT_COLLATION=utf8_general_ci -DWITH_EXTRA_CHARSETS=all -DENABLED_LOCAL_INFILE=1 -DWITH_READLINE=1 -DMYSQL_UNIX_ADDR=/usr/local/mysql/mysql.sock -DMYSQL_TCP_PORT=3306 -DMYSQL_USER=mysql -DCOMPILATION_COMMENT="lq-edition" -DENABLE_DTRACE=0 -DOPTIMIZER_TRACE=1 -DWITH_DEBUG=1

################################################################################
##另外 ******************(亲测可行)
tar xvf mysql-5.6.38.tar.gz

cd mysql-5.6.38

mkdir build

cd build

install_path=/home/zhoulab/zclong/software/mysql-5.6.38/

cmake ..  -DCMAKE_INSTALL_PREFIX=$install_path -DMYSQL_TCP_PORT=3306 -DMYSQL_DATADIR=$install_path/data -DMYSQL_UNIX_ADDR=$install_path/mysql.sock -DDEFAULT_COLLATION=utf8_general_ci
################################################################################








##之后
mysql_root=$install_path

cd $mysql_root

cp support-files/my-default.cnf my.cnf

scripts/mysql_install_db --defaults-file=$mysql_root/my.cnf

bin/mysqladmin --defaults-file=./my.cnf variables




blast2GO安装
http://blog.163.com/henry_by/blog/static/572653582012017104116734/


http://blog.csdn.net/birdben/article/details/51712495

http://blog.163.com/henry_by/blog/static/572653582012017104116734/

http://blog.csdn.net/u010526125/article/details/70990737

https://jingyan.baidu.com/article/a378c9609eb652b3282830fd.html

https://dev.mysql.com/downloads/mysql/

http://blog.shenwei.me/local-blast2go-installation/  ####***
http://www.360doc.com/content/15/1210/16/29531974_519384736.shtml   ####***

wget https://cdn.mysql.com//Downloads/MySQL-5.7/mysql-5.7.20.tar.gz

wget https://cdn.mysql.com//Downloads/MySQL-5.7/mysql-5.7.20-linux-glibc2.12-x86_64.tar.gz

################################################
ViennaRNA安装
./configure prefix=/home/soft/ViennaRNA-2.3.3 -datadir=/home/soft/ViennaRNA-2.3.3
make 
make install







################################################
##mysql初始化
/home/soft/mysql/bin/mysqld --initialize --user=zfc --basedir=/home/soft/mysql --datadir=/home/soft/mysql/data --socket=/tmp/mysql.sock
##（这一步会产生一个root的临时密码，请记住。后面要修改它）


/home/soft/mysql/bin/mysqld --basedir=/home/soft/mysql --datadir=/home/soft/mysql/data --plugin-dir=/home/soft/mysql/lib/plugin --skip-grant-tables --skip-networking --log-error=Dell-04.err --pid-file=Dell-04.pid --socket=/tmp/mysql.sock --daemonize
或者
/home/soft/mysql/bin/mysqld --defaults-file=./my.cnf --daemonize


/home/ops/mysql/bin/mysql -uroot -p XXXX             （XXXX就是初始化给出的那个初始密码）
set password=password('your new password')  ##假设我把它设置为dell-2017

##假设你要停止mysql的服务（我一般就是直接杀死那个上面这个进程/home/soft/mysql/bin/mysqld --defaults-file=./my.cnf --daemonize）
/home/ops/mysql/bin/mysqladmin -S mysql.sock -u root -p shutdown

my.cnf里面的内容
[mysqld]
basedir=/home/soft/mysql
datadir=/home/soft/mysql/data
log-error=/home/soft/mysql/mysql
socket=/tmp/mysql.sock
port=3306
################################################

##关于BLAST2GO的数据库
wget ftp://ftp.ncbi.nlm.nih.gov/gene/DATA/gene_info.gz
wget ftp://ftp.ncbi.nlm.nih.gov/gene/DATA/gene2accession.gz
wget ftp://ftp.pir.georgetown.edu/databases/idmapping/idmapping.tb.gz
wget http://archive.geneontology.org/latest-full/go_monthly-assocdb-data.gz
wget https://www.blast2go.com/images/b2g_support/local_b2g_db.zip
wget https://www.blast2go.com/data/blast2go/b2g4pipe_v2.5.zip
#wget https://www.blast2go.com/downloads/software/blast2go/latest/4_1/Blast2GO_unix_4_1_x64.zip
得到以下文件，都把它们解压，放在/home/soft/B2G_DB之下（b2g4pipe_v2.5.zip可以放在其它地方）
b2g4pipe_v2.5.zip
gene_info.gz
local_b2g_db.zip
Blast2GO_unix_4_1_x64.zip（这个可以不要，目前还不知道干嘛用的）
go_monthly-assocdb-data.gz
gene2accession.gz
idmapping.tb.gz


##关于NR数据库
for((i=1; i<=78; i++))
do
if [ $i -le 9 ]; then
	nohup wget ftp://ftp.ncbi.nih.gov/blast/db/nr.0$i.tar.gz &
else
	nohup wget ftp://ftp.ncbi.nih.gov/blast/db/nr.$i.tar.gz &
fi
done


##导入b2g有关数据库（其中b2g_db.sql在local_b2g_db.zip解压的数据库里面就有）
dbhost=localhost
dbuser=root
dbpass=dell-2017
dbname=b2gdb
dbport=3306 

mysql -u $dbuser -p   (进入数据库，接下来在mysql中创建b2gdb这样一个数据库，提示输入密码，密码就是dell-2017)
create database b2gdb;
exit

mysql -h$dbhost -u$dbuser -p$dbpass $dbname < /home/soft/B2G_DB/local_b2g_db/b2gdb.sql
##提示
有时候会有这样的报错
ERROR 1101 (42000) at line 9: BLOB, TEXT, GEOMETRY or JSON column 'description' can't have a default value
这是由于MYSQL5.x是不允许BLOB/TEXT类型的字段拥有默认值的，且在windows下是默认以
'strict mode'工作的，所以在创建table的时候，可能会有错误提示：
"can't have a default value"，可以通过将my.ini中
sql-mode="STRICT_TRANS_TABLES,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION"
这一行前面加#注释掉解决。



##给用户blast2go使用b2gdb的权限，登录时使用的密码为blast4it
mysql -h$dbhost -u$dbuser -p$dbpass -e "GRANT ALL ON b2gdb.* TO 'blast2go'@'localhost' IDENTIFIED BY 'blast4it';"
mysql -h$dbhost -u$dbuser -p$dbpass -e "FLUSH PRIVILEGES;"
#########
如果要让一个用户无需密码就登录，得先给他设置登录的密码，然后再修改为空。一次性给他空密码会报错。
mysql -h$dbhost -u$dbuser -p$dbpass -e "GRANT ALL ON b2gdb.* TO 'zhangfuchang'@'localhost' IDENTIFIED BY 'mima_haha';"
mysql -h$dbhost -u$dbuser -p$dbpass -e "FLUSH PRIVILEGES;"
mysql -h$dbhost -u$dbuser -p$dbpass -e "GRANT ALL ON b2gdb.* TO 'zhangfuchang'@'localhost' IDENTIFIED BY '';"
mysql -h$dbhost -u$dbuser -p$dbpass -e "FLUSH PRIVILEGES;"
#########

mysql -h$dbhost -u$dbuser -p$dbpass $dbname < /home/soft/B2G_DB/go_monthly-assocdb-data

mysql -h$dbhost -u$dbuser -p$dbpass $dbname -e "LOAD DATA LOCAL INFILE '/home/soft/B2G_DB/gene2accession' INTO TABLE gene2accession FIELDS TERMINATED BY '\t' LINES TERMINATED BY '\n';"

mysql -h$dbhost -u$dbuser -p$dbpass $dbname -e "LOAD DATA LOCAL INFILE '/home/soft/B2G_DB/gene_info' INTO TABLE gene_info FIELDS TERMINATED BY '\t' LINES TERMINATED BY '\n';"

##这个mysql-connector-java-5.0.8-bin.jar在/home/soft/B2G_DB/local_b2g_db里面
cd /home/soft/b2g4pipe/local_b2g_db
java -cp .:/home/soft/B2G_DB/local_b2g_db/mysql-connector-java-5.0.8-bin.jar: ImportIdMapping /home/soft/B2G_DB/idmapping.tb localhost b2gdb $dbuser $dbpass


##最后运行blast2go流程里面的东西
先把b2g4pipe_v2.5.zip解压，假设解压后的目录为 /home/soft/b2g4pipe
cd /home/soft/b2g4pipe
修改b2gPipe.properties文件中b2gdb信息：
// GO and B2G Data Access Basic
Dbacces.dbname=b2gdb
Dbacces.dbhost=localhost:3306
Dbacces.dbuser=root
Dbacces.dbpasswd=dell-2017

java -Xmx1024M -cp /home/soft/b2g4pipe/blast2go.jar:/home/soft/b2g4pipe/ext/*  es.blast2go.prog.B2GAnnotPipe -in /home/zfc/align.xml -out anno -prop /home/soft/b2g4pipe/b2gPipe.properties -v -annot -dat -img -ips ipsr -annex -goslim -wiki /home/soft/b2g4pipe/html_template.html


/home/soft/blastall/bin/blastall -p blastx -i test.fa -d /home/soft/nr/nr -e 1e-6 -m 7 -o align.xml