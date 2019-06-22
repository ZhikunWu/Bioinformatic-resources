### reg pattern for digit

```python
string[0].isdigit()

import re
re.search('^\s*[0-9]',"0abc")

strg[:1] in '0123456789'
```


### sort a dictionary by value

```
import operator
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_x = sorted(x.items(), key=operator.itemgetter(1))
```


And for those wishing to sort on keys instead of values:

```
import operator
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_x = sorted(x.items(), key=operator.itemgetter(0))

```


In Python3 since unpacking is not allowed [1] we can use

```
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_by_value = sorted(x.items(), key=lambda kv: kv[1])
```




### [Fisher's exact test](https://en.wikipedia.org/wiki/Fisher%27s_exact_test)

```
n = a + b + c +d
p_value = (a+b)! (c+d)! (a+c)! (b+d)! / a! b! c! d! n!
```


```
def fisher_test(m1, n1, m2, n2, **kargs):
    alternative = kargs.get('alternative', 'greater')
    cmd = 'fisher.test(matrix(c(%d, %d, %d, %d), nc = 2), alternative = "%s")' \
          % (m1, n1 - m1, m2, n2 - m2, alternative)
    return robjects.r(cmd)[0][0]
```


```

def stats_fisher_exact(obs):
    """
    argv:
        [[368, 132], [10562, 13480]]
    return:
        2.41127716957e-40
    """
    #gene_numbre: 24042
    # obs = [[368, 132], [10562, 13480]]
    oddsratio, pvalue= stats.fisher_exact(obs)
    print(pvalue)
```


### How to tell if string starts with a number?

```python
string[0].isdigit()

import re
re.search('^\s*[0-9]',"0abc")

strg[:1] in '0123456789'
```


## dict (amino acid and nucleotide acid)
```
    table = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
        }
        
```

## subprocess
```python
import subprocess

output = subprocess.Popen(['ls','-l'],stdout=subprocess.PIPE,shell=True).communicate()
print output[0]


return_code, output = commands.getstatusoutput('ls -l')
```

## get file size
```python
import os

def getFileSize(filePath, size=0):
    for root, dirs, files in os.walk(filePath):
        for f in files:
            size += os.path.getsize(os.path.join(root, f))
            print(f)
    return size

print(getFileSize("."))
```

## git int, up or down
```python
import math
math.ceil(2.3)
math.floor(2.6)
round(2.6)

```


## format
```python
#!/usr/bin/python
sub1 = "python string!"
sub2 = "an arg"

a = "i am a %s" % sub1
b = "i am a {0}".format(sub1)

c = "with %(kwarg)s!" % {'kwarg':sub2}
d = "with {kwarg}!".format(kwarg=sub2)

print a    # "i am a python string!"
print b    # "i am a python string!"
print c    # "with an arg!"
print d    # "with an arg!"
```

Something that the modulo operator ( % ) can't do
```
tu = (12,45,22222,103,6)
print '{0} {2} {1} {2} {3} {2} {4} {2}'.format(*tu)

```
result
```
12 22222 45 22222 103 22222 6 22222
```


### format()
being a function, can be used as an argument in other functions:
```python
li = [12,45,78,784,2,69,1254,4785,984]
print map('the number is {}'.format,li)   

print

from datetime import datetime,timedelta

once_upon_a_time = datetime(2010, 7, 1, 12, 0, 0)
delta = timedelta(days=13, hours=8,  minutes=20)

gen =(once_upon_a_time +x*delta for x in xrange(20))

print '\n'.join(map('{:%Y-%m-%d %H:%M:%S}'.format, gen))
```

results in
```
['the number is 12', 'the number is 45', 'the number is 78', 'the number is 784', 'the number is 2', 'the number is 69', 'the number is 1254', 'the number is 4785', 'the number is 984']

2010-07-01 12:00:00
2010-07-14 20:20:00
2010-07-28 04:40:00
2010-08-10 13:00:00
2010-08-23 21:20:00
2010-09-06 05:40:00
2010-09-19 14:00:00
2010-10-02 22:20:00
2010-10-16 06:40:00
2010-10-29 15:00:00
2010-11-11 23:20:00
2010-11-25 07:40:00
2010-12-08 16:00:00
2010-12-22 00:20:00
2011-01-04 08:40:00
2011-01-17 17:00:00
2011-01-31 01:20:00
2011-02-13 09:40:00
2011-02-26 18:00:00
2011-03-12 02:20:00
```


However, you can't use the new style .format() syntax here, not even in Python 3.3, which is a shame
```python
log.debug("some debug info: %(this)s and %(that)s", dict(this='Tom', that='Jerry'))
```

As of Python 3.6 you can substitute variables into strings by name:
```python
>>> origin = "London"
>>> destination = "Paris"
>>> f"from {origin} to {destination}"
>>> 
```
Note the f" prefix. If you try this in Python 3.5 or earlier, you'll get a `SyntaxError`.

As I discovered today, the old way of formatting strings via % doesn't support Decimal, Python's module for decimal fixed point and floating point arithmetic, out of the box.
```python
#!/usr/bin/env python3

from decimal import *

getcontext().prec = 50
d = Decimal('3.12375239e-24') # no magic number, I rather produced it by banging my head on my keyboard

print('%.50f' % d)
print('{0:.50f}'.format(d))
```
output:
```
0.00000000000000000000000312375239000000009907464850
0.00000000000000000000000312375239000000000000000000
```
There surely might be work-arounds but you still might consider using the format() method right away.

#### % gives better performance than format from my test.
python 2.7
```python
import timeit
print 'format:', timeit.timeit("'{}{}{}'.format(1, 1.23, 'hello')")
print '%:', timeit.timeit("'%s%s%s' % (1, 1.23, 'hello')")
```
resuts:
```
> format: 0.470329046249
> %: 0.357107877731
```

Python 3.5.2
```python
import timeit
print('format:', timeit.timeit("'{}{}{}'.format(1, 1.23, 'hello')"))
print('%:', timeit.timeit("'%s%s%s' % (1, 1.23, 'hello')"))
```
result
```
> format: 0.5864730989560485
> %: 0.013593495357781649
```
It looks in Python2, the difference is small whereas in Python3, % is much faster than format.




## time
```python
import time
localtime = time.asctime( time.localtime(time.time()) )
print localtime

print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()) 
```

#### python中时间日期格式化符号：
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00=59）
%S 秒（00-59）
%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身


## get calendar
```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import calendar

cal = calendar.month(2016, 1)
print "以下输出2016年1月份的日历:"
print cal;
```
output:
```
以下输出2016年1月份的日历:
    January 2016
Mo Tu We Th Fr Sa Su
             1  2  3
 4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28 29 30 31
```


## multiprocessing.Manager介绍和实例
Python中进程间共享数据，处理基本的queue，pipe和value+array外，还提供了更高层次的封装。使用multiprocessing.Manager可以简单地使用这些高级接口。
Manager()返回的manager对象控制了一个server进程，此进程包含的python对象可以被其他的进程通过proxies来访问。从而达到多进程间数据通信且安全。
Manager支持的类型有list,dict,Namespace,Lock,RLock,Semaphore,BoundedSemaphore,Condition,Event,Queue,Value和Array。
```python

import multiprocessing
import time
def worker(d, key, value):
    d[key] = value
if __name__ == '__main__':
    mgr = multiprocessing.Manager()
    d = mgr.dict()
    jobs = [ multiprocessing.Process(target=worker, args=(d, i, i*2))
             for i in range(10) 
             ]
    for j in jobs:
        j.start()
    for j in jobs:
        j.join()
    print ('Results:' )
    for key, value in enumerate(dict(d)):
        print("%s=%s" % (key, value))
        
# the output is :
# Results:
# 0=0
# 1=1
# 2=2
# 3=3
# 4=4
# 5=5
# 6=6
# 7=7
# 8=8
# 9=9
```


### PYTHON THREADING模块学习JOIN()
join方法，如果一个线程或者一个函数在执行过程中要调用另外一个线程，并且待到其完成以后才能接着执行，那么在调用这个线程时可以使用被调用线程的join方法。
```python
import string, threading, time


def thread_main(a):
    global count, mutex
    # 获得线程名
    threadname = threading.currentThread().getName()



    for x in xrange(0, int(a)):
        # 取得锁
        mutex.acquire()
        count = count + 1
        # 释放锁
        mutex.release()
        print threadname, x, count
        time.sleep(1)



def main(num):
    global count, mutex
    threads = []



    count = 1
    # 创建一个锁
    mutex = threading.Lock()
    # 先创建线程对象
    for x in xrange(0, num):
        threads.append(threading.Thread(target=thread_main, args=(10,)))
    # 启动所有线程
    for t in threads:
        t.start()
    # 主线程中等待所有子线程退出
    for t in threads:
        t.join()  



if __name__ == '__main__':
    num = 4
    # 创建4个线程
    main(4)
###################################################################
#-*- encoding: gb2312 -*-
import threading
import time



class Test(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self._run_num = num



    def run(self):
        global count, mutex
        threadname = threading.currentThread().getName()



        for x in xrange(0, int(self._run_num)):
            mutex.acquire()
            count = count + 1
            mutex.release()
            print threadname, x, count
            time.sleep(1)



if __name__ == '__main__':
    global count, mutex
    threads = []
    num = 4
    count = 1
    # 创建锁
    mutex = threading.Lock()
    # 创建线程对象
    for x in xrange(0, num):
        threads.append(Test(10))
    # 启动线程
    for t in threads:
        t.start()
    # 等待子线程结束
    for t in threads:
        t.join()
```

在程序中，最后join()方法的调用就明白了，是主进程挨个调用子线程的join()方法。当四个线程都执行完毕后，主线程才会执行下面的代码，在这里也就是退出了。
相对应的在网上一起找到的另一个方法：
3.守护进程
setDaemon()

这个方法基本和join是相反的。当我们在程序运行中，执行一个主线程，如果主线程又创建一个子线程，主线程和子线程就分兵两路，分别运行，那么当主线程完成想退出时，会检验子线程是否完成。如果子线程未完成，则主线程会等待子线程完成后再退出。但是有时候我们需要的是，只要主线程完成了，不管子线程是否完成，都要和主线程一起退出，这时就可以用setDaemon方法啦


## map object is not subscriptable
In Python 3, map returns an iterable object of type map, and not a subscriptible list, which would allow you to write map[i]. To force a list result, write
```python
payIntList = list(map(int,payList))
```
However, in many cases, you can write out your code way nicer by not using indices. For example, with list comprehensions:
```python
payIntList = [pi + 1000 for pi in payList]
for pi in payIntList:
    print(pi)
```


## scipy.stats
### AttributeError: 'module' object has no attribute 'stats' 
```python
>>> from scipy import stats, optimize, interpolate


>>> import scipy
>>> scipy.stats
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'module' object has no attribute 'stats'
>>> scipy.optimize
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'module' object has no attribute 'optimize'

>>> import scipy.stats
>>> scipy.optimize
<module 'scipy.optimize' from 'C:\Python26\lib\site-packages\scipy\optimize\__init__.pyc'>
```


### List indexes of duplicate values in a list with Python
```python
a, seen, result = [1, 2, 3, 2, 1, 5, 6, 5, 5, 5], set(), []
for idx, item in enumerate(a):
    if item not in seen:
        seen.add(item)          # First time seeing the element
    else:
        result.append(idx)      # Already seen, add the index to the result
print result
# [3, 4, 7, 8, 9]
```
Edit: You can just use list comprehension in that function, like this

```python
def list_duplicates(seq):
    seen = set()
    seen_add = seen.add
    return [idx for idx,item in enumerate(seq) if item in seen or seen_add(item)]

print list_duplicates([1, 2, 3, 2, 1, 5, 6, 5, 5, 5])
# [3, 4, 7, 8, 9]
```


very usful
```python
>>> def duplicates(lst, item):
...   return [i for i, x in enumerate(lst) if x == item]
... 
>>> duplicates(List, "A")
[0, 2]
```
To get all duplicates, you can use the below method, but it is not very efficient. If efficiency is important you should consider Ignacio's solution instead.
```python
>>> dict((x, duplicates(List, x)) for x in set(List) if List.count(x) > 1)
{'A': [0, 2]}
```
