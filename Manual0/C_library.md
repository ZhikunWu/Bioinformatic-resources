

### install [libcurl](https://packages.ubuntu.com/xenial/curl)
```
dpkg -i  curl_7.47.0-1ubuntu2.2_amd64.deb
```
or

```
wget https://curl.haxx.se/download/curl-7.55.1.tar.gz
tar -zxf curl-7.55.1.tar.gz
cd curl-7.55.1/
./configure --prefix=/home/wzk/anaconda3/envs/RMeta
make && make install
```
