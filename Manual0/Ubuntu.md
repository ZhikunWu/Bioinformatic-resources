## 在Ubuntu 14.04 64bit上安装百度云Linux客户端BCloud

百度云是一个不错的网盘，Bcloud 是一个 Linux 下超赞的客户端, 官网
```
github：
https://github.com/LiuLang/bcloud-packages
和kwplayer是同一个作者.
安装步骤：
直接下载 bcloud-x.x.x.deb这个包, 然后双击deb包就能安装了.下面是我在Ubuntu 14.04 64bit上的安装截图
```


## 下载磁力链接

```
sudo apt-get install ktorrent

下载磁力链接：

1. 打开ktorrent->Open URL

2. 复制磁力链接地址， 粘贴到地址栏里即可。

下载torrent：

1. 打开ktorrent->Open，选择torrent文件即可。
```



```
sudo apt-get install amule
```

下载迅雷链接：
```
迅雷下载协议是经过加密的,如：
thunder://QUFlZDJrOi8vfGZpbGV8JUU4JUExJThDJUU1JUIwJUI4JUU4JUI1JUIwJUU4JTgyJTg5LlRoZS5XYWxraW5nLkRlYWQuUzA2RTAxLiVFNCVCOCVBRCVFOCU4QiVCMSV
FNSVBRCU5NyVFNSVCOSU5NS5IRFRWcmlwLjEwMjR4NTc2Lm1wNHw2NDg3NTg1MDl8ZjIyZmI2OTRjMDQ0ZmYyNjU0MjhhNTEzNWVhYzhiOTB8aD12eXFsNHFjNHpmYmx0e
WNqdW1rcnNibDJza2JscTJsZnwvWlo=
直接在Linux下面是没有办法下载的。

在终端下用echo url | base64 -d 来解密，并显示地址，如（URL去掉头和尾）：

echo QUFlZDJrOi8vfGZpbGV8JUU4JUExJThDJUU1JUIwJUI4JUU4JUI1JUIwJUU4JTgyJTg5LlRoZS5XYWxraW5nLkRlYWQuUzA2RTAxLiVFNCVCOCVBRCVFOCU4QiVCMSVFN
SVBRCU5NyVFNSVCOSU5NS5IRFRWcmlwLjEwMjR4NTc2Lm1wNHw2NDg3NTg1MDl8ZjIyZmI2OTRjMDQ0ZmYyNjU0MjhhNTEzNWVhYzhiOTB8aD12eXFsNHFjNHpmYmx0eW
NqdW1rcnNibDJza2JscTJsZnwvWlo= | base64 -d

显示结果是：AAed2k://|file|%E8%A1%8C%E5%B0%B8%E8%B5%B0%E8%82%89.The.Walking.Dead.S06E01.%E4%B8%AD%E8%8B%B1%E5%AD%97%E5%B9%95.HDTVrip.1024x576.mp4|648758509|f22fb694c044ff265428a5135eac8b90|h=vyql4qc4zfbltycjumkrsbl2skblq2lf|/ZZ

所以解密后的地址是：ed2k://|file|%E8%A1%8C%E5%B0%B8%E8%B5%B0%E8%82%89.The.Walking.Dead.S06E01.%E4%B8%AD%E8%8B%B1%E5%AD%97%E5%B9%95.HDTVrip.1024x576.mp4|648758509|f22fb694c044ff265428a5135eac8b90|h=vyql4qc4zfbltycjumkrsbl2skblq2lf|/

复制解密后的地址，粘贴到amule里即可。

```