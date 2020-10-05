### [install bioperl](http://bioperl.org/INSTALL.html)
### [bioperl howto](http://bioperl.org/howtos/BioGraphics_HOWTO.html)

### install Bio::SearchIO
```
$ perl -MCPAN -e shell
cpan[1]> install Bio::SearchIO

```




## [BIOPERL INSTALLATION](http://bioperl.org/INSTALL.html)
## [Linux上安装Perl模块的两种方法](http://www.cnblogs.com/zhangchaoyang/articles/2610573.html)

### Install or upgrade **Module::Build**, and make it your preferred installer
```
perl -MCPAN -e shell
cpan>install Module::Build
cpan>o conf prefer_installer MB
cpan>o conf commit
```

### install packaegs
```
cpan>d /bioperl/

 ....

 Distribution    C/CJ/CJFIELDS/BioPerl-1.007001.tar.gz
 Distribution    C/CJ/CJFIELDS/BioPerl-1.007001.tar.gz
 Distribution    C/CJ/CJFIELDS/BioPerl-1.007001.tar.gz

cpan>install C/CJ/CJFIELDS/BioPerl-1.007001.tar.gz
cpan>force install C/CJ/CJFIELDS/BioPerl-1.007001.tar.gz
```


### install from github
```
git clone https://github.com/bioperl/bioperl-live.git
cd bioperl-live
perl Build.PL
./Build test
./Build install
```

### install package in your home directory 
If you lack permission to install Perl modules into the standard system directories you can install them in your home directory using local::lib. The instructions for first installing local::lib are found here:

https://metacpan.org/pod/local::lib

Once local::lib is installed you can install BioPerl using a command like this:
```
perl -MCPAN -Mlocal::lib -e 'CPAN::install(C/CJ/CJFIELDS/BioPerl-1.6.924.tar.gz)'
```

The BioPerl test system is located in the t/ directory and is automatically run whenever you execute the ./Build test command.

The tests have been organized into groups based upon the specific task or class the module being tested belongs to. If you want to investigate the behavior of a specific test such as the Seq test you would type:
```
./Build test --test_files t/Seq/Seq.t --verbose
```

The --test_files argument can be used multiple times to try a set of test scripts in one go. The --verbose arguement outputs the detailed test results, instead of just the summary you see during ./Build test.

The --test-files argument can also work as a glob. For instance, to run tests on all SearchIO modules, use the following:
```
./Build test --test_files t/SearchIO* --verbose
```


