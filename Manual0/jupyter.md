
## jupyter server

### install jupyter (python 3 environment)
```bash
$ conda install -c conda-forge jupyter
```

### jupyter config file
```bash
$ jupyter notebook --generate-config
Writing default config to: /home/wzk/.jupyter/jupyter_notebook_config.py

$  jupyter notebook password
Enter password: 
Verify password: 
[NotebookPasswordApp] Wrote hashed password to /home/wzk/.jupyter/jupyter_notebook_config.json

```

edit in /home/wzk/.jupyter/jupyter_notebook_config.py
```
c.NotebookApp.ip = '*' #所有绑定服务器的IP都能访问
c.NotebookApp.port = 9999 #将端口设置为自己喜欢的吧，默认是8888
c.NotebookApp.open_browser = False #我们并不想在服务器上直接打开Jupyter Notebook，所以设置成False
```

run jupyter in background
```
$  jupyter notebook &
[1] 131328

$ [I 08:04:31.581 NotebookApp] Writing notebook server cookie secret to /run/user/1007/jupyter/notebook_cookie_secret
[W 08:04:32.202 NotebookApp] WARNING: The notebook server is listening on all IP addresses and not using encryption. This is not recommended.
[I 08:04:32.261 NotebookApp] Serving notebooks from local directory: /home/wzk/metagenome_data/prokka/salmon
[I 08:04:32.261 NotebookApp] 0 active kernels 
[I 08:04:32.261 NotebookApp] The Jupyter Notebook is running at: http://[all ip addresses on your system]:0/
[I 08:04:32.261 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
```


