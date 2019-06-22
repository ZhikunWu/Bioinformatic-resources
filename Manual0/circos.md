
## Circos

This tutorial was released by [alexcoppe](https://github.com/alexcoppe/bio-dockers)

### install [circos of docker](https://hub.docker.com/r/alexcoppe/circos/)
```
$ docker pull alexcoppe/circos

Using default tag: latest
latest: Pulling from alexcoppe/circos
ff3a5c916c92: Pull complete 
f5f57bd3c134: Pull complete 
ebac6d43a07e: Pull complete 
Digest: sha256:aa6b9bb0431a93a67da75a18bd4c20317b4bda2fa65d6730c1fde6d05b0346d6
Status: Downloaded newer image for alexcoppe/circos:latest
```

### download test data
```
$ wget http://circos.ca/distribution/circos-0.69-3.tgz
$ tar xzvf circos-0.69-3.tgz
```

### Copy the data and the etc directory from the CIRCOS distribution to the current directory:

```
$ cp -R  circos-0.69-3/example/data .
$ cp -R  circos-0.69-3/example/etc .
```

### Copy the CIRCOS configuration file to your current directory:
```
$ cp  circos-0.69-3/example/etc/circos.conf .
```

### Run the docker container:
```
$ docker run --rm -it -v $(pwd):/data alexcoppe/circos -conf /data/circos.conf -outputdir /data
```

### dockerfile of circos
```
FROM alpine

ENV version 0.69-6

ADD http://circos.ca/distribution/circos-${version}.tgz /tmp/

RUN mkdir /opt && cd /opt/ \
&& tar xzvf /tmp/circos-${version}.tgz \
&& mv circos-${version} circos \
&& apk add --update --no-cache perl gd jpeg freetype \
&& apk add --update --no-cache --virtual=deps make gd-dev jpeg-dev freetype-dev apkbuild-cpan gcc musl-dev perl-dev \
&& wget -O - http://cpanmin.us | perl - --self-upgrade \
&& cpanm Math::Bezier Math::Round Readonly::Tiny Readonly Config::General Params::Validate Font::TTF::Font Regexp::Common Math::VecStat Text::Format SVG Clone List::MoreUtils \
&& cpanm -force GD Number::Format \
&& cpanm Statistics::Basic Set::IntSpan \
&& cpanm -force Try::Tiny \
&& rm -rf /var/cache/apk/* /tmp/circos-${version}.tgz \
&& apk del deps


CMD ["-help"]
ENTRYPOINT ["/opt/circos/bin/circos"]

```


