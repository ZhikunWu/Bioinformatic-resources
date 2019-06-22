## [BaiduPCS-Go](https://github.com/iikira/BaiduPCS-Go): 百度网盘客户端 - Go语言编写

### [BaiduPCS-Go | 百度网盘命令行工具](https://www.jianshu.com/p/c37a124a0f55)

### download and install
download the software
```
$ wget https://github.com/iikira/BaiduPCS-Go/releases/download/v3.5.6/BaiduPCS-Go-v3.5.6-linux-amd64.zip
```

The files:
```
$ tree /home/wzk/software/BaiduPCS-Go-v3.5.6-linux-amd64
/home/wzk/software/BaiduPCS-Go-v3.5.6-linux-amd64
├── BaiduPCS-Go
├── download
└── README.md
```

### login
```
$ ./BaiduPCS-Go 
提示: 方向键上下可切换历史命令.
提示: Ctrl + A / E 跳转命令 首 / 尾.
提示: 输入 help 获取帮助.
BaiduPCS-Go > login
请输入百度用户名(手机号/邮箱/用户名), 回车键提交 > ***********
请输入密码(输入的密码无回显, 确认输入完成, 回车提交即可) > 

需要验证手机或邮箱才能登录
选择一种验证方式
1: 手机: 155******93
2: 邮箱: 未找到邮箱地址

请输入验证方式 (1 或 2) > 1
消息: 验证码已发送至你的手机 155******93

请输入接收到的验证码 > 097333
百度帐号登录成功: zkwu88
```

### use information
```
BaiduPCS-Go:A_script zkwu88$ quota
用户名: zkwu88, 总空间: 1.006836TB, 已用空间: 252.131187GB, 比率: 24.455013%
```

### meta
```
BaiduPCS-Go:A_script zkwu88$ meta

  类型            目录                 
  目录路径        /A_script            
  目录名称        A_script             
  app_id          250528               
  fs_id           204680254091228      
  创建日期        2019-01-07 20:08:01  
  修改日期        2019-01-07 20:08:14  
  是否含有子目录  true
```

### upload files
```
BaiduPCS-Go:/ zkwu88$ cd A_script/
改变工作目录: /A_script

BaiduPCS-Go:A_script zkwu88$ l

当前目录: /A_script
----
  #   文件大小         修改日期               文件(目录)         
  0            -  2019-01-08 21:34:29  docker/                   
  1      34.88KB  2019-01-07 20:09:15  deblur_workflow.py        
  2      15.31KB  2019-01-08 10:27:43  detect_DA_features.R      
  3      11.13KB  2019-01-08 21:33:12  phobius.pl                
  4       8.31KB  2019-01-08 21:33:12  run_signalp.py                 
     总: 66.86KB                       文件总数: 4, 目录总数: 1  
----
BaiduPCS-Go:A_script zkwu88$ upload /home/wzk/github/zkwu/kc16SRNA/src/kc16SRNA/UniqSeqSize.py A_script/
[1] 加入上传队列: /home/wzk/github/zkwu/kc16SRNA/src/kc16SRNA/UniqSeqSize.py
[1] 准备上传: /home/wzk/github/zkwu/kc16SRNA/src/kc16SRNA/UniqSeqSize.py
[1] 秒传失败, 开始上传文件...

[1] ↑ 1.31KB/1.31KB 1.31KB/s in 1s ............
[1] 上传文件成功, 保存到网盘路径: /A_script/A_script/UniqSeqSize.py

全部上传完毕, 总大小: 1.308594KB
```

The last parameter **A_script** is the target directory


### help document

```
BaiduPCS-Go:A_script zkwu88$ help
----
  BaiduPCS-Go - 百度网盘客户端 for linux/amd64

USAGE:
  BaiduPCS-Go [global options] command [command options] [arguments...]

VERSION:
  v3.5.6

DESCRIPTION:
  BaiduPCS-Go 使用Go语言编写的百度网盘命令行客户端, 为操作百度网盘, 提供实用功能.
  具体功能, 参见 COMMANDS 列表

  特色:
    网盘内列出文件和目录, 支持通配符匹配路径;
    下载网盘内文件, 支持网盘内目录 (文件夹) 下载, 支持多个文件或目录下载, 支持断点续传和高并发高速下载.

  ---------------------------------------------------
  前往 https://github.com/iikira/BaiduPCS-Go 以获取更多帮助信息!
  前往 https://github.com/iikira/BaiduPCS-Go/releases 以获取程序更新信息!
  ---------------------------------------------------

  交流反馈:
    提交Issue: https://github.com/iikira/BaiduPCS-Go/issues
    邮箱: i@mail.iikira.com

AUTHOR:
  iikira/BaiduPCS-Go: https://github.com/iikira/BaiduPCS-Go

COMMANDS:
    tool     工具箱
    help, h  Shows a list of commands or help for one command
  其他:
    bg           管理后台任务
    clear, cls   清空控制台
    env          显示程序环境变量
    run          执行系统命令
    sumfile, sf  获取本地文件的秒传信息
    update       检测程序更新
    web          启用 web 客户端 (测试中)
  百度帐号:
    login    登录百度账号
    loglist  列出帐号列表
    logout   退出百度帐号
    su       切换百度帐号
    who      获取当前帐号
  百度网盘:
    cd                      切换工作目录
    cp                      拷贝文件/目录
    createsuperfile, csf    手动分片上传—合并分片文件
    download, d             下载文件/目录
    export, ep              导出文件/目录
    locate, lt              获取下载直链
    ls, l, ll               列出目录
    meta                    获取单个文件/目录的元信息
    mkdir                   创建目录
    mv                      移动/重命名文件/目录
    offlinedl, clouddl, od  离线下载
    pwd                     输出工作目录
    quota                   获取网盘配额
    rapidupload, ru         手动秒传文件
    rm                      删除文件/目录
    search, s               搜索文件
    share                   分享文件/目录
    tree, t                 列出目录的树形图
    upload, u               上传文件/目录
  配置:
    config  显示和修改程序配置项

GLOBAL OPTIONS:
  --verbose      启用调试 [$BAIDUPCS_GO_VERBOSE]
  --help, -h     show help
  --version, -v  print the version

COPYRIGHT:
  (c) 2016-2018 iikira.

```

### config information
```
BaiduPCS-Go:A_script zkwu88$ config
----
运行 BaiduPCS-Go config set 可进行设置配置

当前配置:
        名称                      值                   建议值                              描述                          
  appid              266719                                        百度 PCS 应用ID                                       
  enable_https       false                              true       启用 https                                            
  user_agent         netdisk;8.3.1;android-android                 浏览器标识                                            
  cache_size         30000                          1024 ~ 262144  下载缓存, 如果硬盘占用高或下载速度慢, 请尝试调大此值  
  max_parallel       100                              50 ~ 500     下载最大并发量                                        
  max_download_load  1                                  1 ~ 5      同时进行下载文件的最大数量                            
  savedir            /home/wzk/Downloads                           下载文件的储存目录 
```

parameters:
```
BaiduPCS-Go:A_script zkwu88$ config set
----
  BaiduPCS-Go config set - 修改程序配置项

USAGE:
  BaiduPCS-Go config set [arguments...]

DESCRIPTION:
  
  例子:
    BaiduPCS-Go config set -appid=260149
    BaiduPCS-Go config set -enable_https=false
    BaiduPCS-Go config set -user_agent="netdisk;1.0"
    BaiduPCS-Go config set -cache_size 16384 -max_parallel 200 -savedir D:/download

OPTIONS:
  --appid value              百度 PCS 应用ID (default: 0)
  --enable_https             启用 https
  --user_agent value         浏览器标识
  --max_parallel value       上传/下载网络连接的最大并发量 (default: 0)
  --cache_size value         下载缓存 (default: 0)
  --max_download_load value  同时进行下载文件的最大数量 (default: 0)
  --savedir value            下载文件的储存目录

```

#### set the max parallel values
```
BaiduPCS-Go:A_script zkwu88$ config set -max_parallel 50
        名称                      值                   建议值                              描述                          
  appid              266719                                        百度 PCS 应用ID                                       
  enable_https       false                              true       启用 https                                            
  user_agent         netdisk;8.3.1;android-android                 浏览器标识                                            
  cache_size         30000                          1024 ~ 262144  下载缓存, 如果硬盘占用高或下载速度慢, 请尝试调大此值  
  max_parallel       50                               50 ~ 500     下载最大并发量                                        
  max_download_load  1                                  1 ~ 5      同时进行下载文件的最大数量                            
  savedir            /home/wzk/Downloads                           下载文件的储存目录                                    

保存配置成功!

```

### exit 

运行命令 **quit** 或 **exit** 或 组合键 **Ctrl+C** 或 组合键 **Ctrl+D**




### manuals

* BaiduPCS-Go update 检测更新
* BaiduPCS-Go login  登入
* BaiduPCS-Go login -bduss=<BDUSS>  ## [登录百度帐号](https://github.com/iikira/BaiduPCS-Go/wiki/关于-获取百度-BDUSS)
* BaiduPCS-Go loglist 列出帐号列表
* BaiduPCS-Go who 获取当前帐号
* BaiduPCS-Go su <uid> 切换已登录的百度帐号
* BaiduPCS-Go logout 退出百度帐号
* BaiduPCS-Go quota 获取网盘配额
* BaiduPCS-Go cd <目录>  切换工作目录
* BaiduPCS-Go cd -l <目录> 切换工作目录后自动列出工作目录下的文件和目录
* BaiduPCS-Go pwd 输出工作目录
* BaiduPCS-Go ls <目录>  列出目录

  * -asc: 升序排序
  * -desc: 降序排序
  * -time: 根据时间排序
  * -name: 根据文件名排序
  * -size: 根据大小排序

* BaiduPCS-Go tree  列出目录树形图
* BaiduPCS-Go meta <文件/目录1> 获取文件/目录的元信息
* BaiduPCS-Go search [-path=<需要检索的目录>] [-r] <关键字> 搜索文件
* BaiduPCS-Go download 下载文件/目录

  * --test          测试下载, 此操作不会保存文件到本地
  * --ow            overwrite, 覆盖已存在的文件
  * --status        输出所有线程的工作状态
  * --save          将下载的文件直接保存到当前工作目录
  * --saveto value  将下载的文件直接保存到指定的目录
  * -x              为文件加上执行权限, (windows系统无效)
  * --share         以分享文件的方式获取下载链接来下载
  * --locate        以获取直链的方式来下载
  * -p value        指定下载线程数

* BaiduPCS-Go upload <本地文件/目录的路径1>  上传文件/目录

  * 上传默认采用分片上传的方式, 上传的文件将会保存到, <目标目录>.
  * 遇到同名文件将会自动覆盖!!
  * 当上传的文件名和网盘的目录名称相同时, 不会覆盖目录, 防止丢失数据.

* BaiduPCS-Go locate <文件1> 获取下载直链
* BaiduPCS-Go export 导出文件/目录
* BaiduPCS-Go mkdir <目录> 创建目录
* BaiduPCS-Go rm <网盘文件或目录的路径1> 删除文件/目录
* BaiduPCS-Go cp <文件/目录> <目标 文件/目录>  拷贝文件/目录
* BaiduPCS-Go mv <文件/目录1> <文件/目录2>  移动/重命名文件/目录
* BaiduPCS-Go share 分享文件/目录
* BaiduPCS-Go share set <文件/目录1> 设置分享文件/目录
* BaiduPCS-Go share list 列出已分享文件/目录
* BaiduPCS-Go share cancel <shareid_1>  取消分享文件/目录
* BaiduPCS-Go offlinedl/clouddl/od  离线下载
* BaiduPCS-Go offlinedl add -path=<离线下载文件保存的路径> 资源地址1  添加离线下载任务  (BaiduPCS-Go offlinedl add -path=/ http://baidu.com http://qq.com)
* BaiduPCS-Go offlinedl query 任务ID1  精确查询离线下载任务
* BaiduPCS-Go offlinedl list  查询离线下载任务列表
* BaiduPCS-Go offlinedl delete 任务ID1  删除离线下载任务
* BaiduPCS-Go offlinedl cancel 任务ID1 取消离线下载任务
* BaiduPCS-Go recycle list 列出回收站文件列表 (--page value  回收站文件列表页数 (default: 1))
* BaiduPCS-Go recycle restore <fs_id 1> 还原回收站文件或目录
* BaiduPCS-Go recycle delete [-all] <fs_id 1> 删除回收站文件或目录/清空回收站
* BaiduPCS-Go config 显示配置
* BaiduPCS-Go config set  设置配置
