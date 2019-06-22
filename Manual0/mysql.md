
### mysql
```
conda install mysql-python
```


### install mysql
```
$ cat /etc/issue
Ubuntu 16.04.3 LTS \n \l
```

```
$ cd mysql-5.7.20/
$ cmake -D MYSQL_DATADIR=/home/wzk/MySQL/data -D SYSCONFDIR=/home/wzk/MySQL/etc -D CMAKE_INSTALL_PREFIX=/home/wzk/MySQL .
```

#### error
```
CMake Error: CMAKE_C_COMPILER not set, after EnableLanguage
CMake Error: CMAKE_CXX_COMPILER not set, after EnableLanguage
-- Configuring incomplete, errors occurred!
See also "/home/wzk/MySQL/mysql-5.7.20/CMakeFiles/CMakeOutput.log".
```

answer:
https://stackoverflow.com/questions/14807294/how-to-install-cmake-c-compiler-and-cxx-compiler/18964434



###  changing of the password should work in one line
```
/home/martin/mysql/bin/mysqladmin -h 127.0.0.1 -P 3666 -u root password 'mypass'
```


### [Installing MySQL without Root Access on Linux](http://www.bluecrownsoftware.com/article/271/Installing-MySQL-without-Root-Access-on-Linux)
1. Download tar.gz file distribution from mysql.com and explode to a directory.

2. From base MySQL directory run:

        ./scripts/mysql_install_db --datadir=[Base MySQL Directory]/data

People
3. From base MySQL directory create some scripts for the following commands to start/stop and access command line:

    Command to Start: 

        ./bin/mysqld --basedir=[Base MySQL Directory] --datadir=[Base MySQL Directory]/data --log-error=[Base MySQL Directory]/data/mysql.err --pid-file=[Base MySQL Directory]/mysql.pid --socket=[Base MySQL Directory]/thesock --port=3306 &

    Command to Stop:
 
        ./bin/mysqladmin --socket=[Base MySQL Directory]/thesock shutdown

    Command to Access MySQL database:
 
        ./bin/mysql --socket=[Base MySQL Directory]/thesock

4. Start loading your data.

### [mysqldump](https://dev.mysql.com/doc/refman/5.7/en/mysqldump.html)


