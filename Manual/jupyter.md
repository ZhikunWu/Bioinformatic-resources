

1 生成Jupyter Notebook配置文件

```shell
jupyter notebook --generate-config

#Writing default config to: ~/.jupyter/jupyter_notebook_config.py

```

2 设置Jupyter Notebook密码


```
$ python
Python 3.6.7 | packaged by conda-forge | (default, Feb 28 2019, 09:07:38) 
[GCC 7.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from IPython.lib import passwd
>>> passwd()
Enter password: 
Verify password: 
'sha1:27b3c5ecf84b:1cca4ab52c6331675d8df2793b97432a4c55a7c7'
```



```shell
jupyter notebook password
```

3 修改jupyter_notebook_config.py

``` shell
vim ~/.jupyter/jupyter_notebook_config.py
```

```
c.NotebookApp.ip = '*' #所有绑定服务器的IP都能访问
c.NotebookApp.port = 9999 #将端口设置为自己喜欢的吧，默认是8888
c.NotebookApp.open_browser = False #我们并不想在服务器上直接打开Jupyter Notebook，所以设置成False
```

4. 启动Jupyter Notebook服务器,并让其在后台运行

``` shell
jupyter notebook &
```

config file: .jupyter/jupyter_notebook_config.py
```
c=get_config()
c.NotebookApp.ip= '202.116.105.17'
c.NotebookApp.password = u'sha1:27b3c5ecf84b:1cca4ab52c6331675d8df2793b97432a4c55a7c7'
c.NotebookApp.open_browser = False
c.NotebookApp.port =8787
c.IPKernelApp.pylab = 'inline'
c.NotebookApp.allow_remote_access = True
c.NotebookApp.notebook_dir = "/home/wuzhikun/notebok"
c.NotebookApp.certfile = u'/home/wuzhikun/.jupyter/mycert.pem'
```


