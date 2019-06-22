## docker image

### get the image

general command
```
$ docker pull [选项] [Docker Registry 地址[:端口号]/] 仓库名[:标签]
```

example:
```
$ docker pull osallou/cnvnator
Using default tag: latest
latest: Pulling from osallou/cnvnator
a3ed95caeb02: Pull complete 
9b343ff87a70: Pull complete 
c75dd1a8e97b: Pull complete 
13fa7e1e7b27: Pull complete 
b3b28c8dec41: Pull complete 
d27fb5ede187: Pull complete 
e88e9753b5ec: Pull complete 
5988d35880d4: Pull complete 
55c7abf96fc0: Pull complete 
370427ba472c: Pull complete 
adeb8ec60d13: Pull complete 
Digest: sha256:8f03a4c80cb1a1c88fe562361565cbf337ca9114baa1a00940accf2a69806ad0
Status: Downloaded newer image for osallou/cnvnator:latest

```

Docker 镜像仓库地址：地址的格式一般是 <域名/IP>[:端口号]。默认地址是 Docker Hub。


仓库名:

* osallou: user name 
* cnvnator: software name
* latest: tag name

### docker image 

```
$ docker image --help

Usage:  docker image COMMAND

Manage images

Options:
      --help   Print usage

Commands:
  build       Build an image from a Dockerfile
  history     Show the history of an image
  import      Import the contents from a tarball to create a filesystem image
  inspect     Display detailed information on one or more images
  load        Load an image from a tar archive or STDIN
  ls          List images
  prune       Remove unused images
  pull        Pull an image or a repository from a registry
  push        Push an image or a repository to a registry
  rm          Remove one or more images
  save        Save one or more images to a tar archive (streamed to STDOUT by default)
  tag         Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE

Run 'docker image COMMAND --help' for more information on a command.

```



### list the images
```
$ docker image ls
REPOSITORY             TAG                 IMAGE ID            CREATED             SIZE
nginx                  latest              ae513a47849c        7 months ago        109MB
ubuntu                 latest              452a96d81c30        7 months ago        79.6MB
genevera/docker-pigz   latest              860ff7912c63        7 months ago        4.17MB
wwliao/cnvnator        latest              7e928b3e6784        13 months ago       1.43GB
qiime2/core            2017.7              e6eca03649a6        16 months ago       5.19GB
hello-world            latest              1815c82652c0        17 months ago       1.84kB
rmats                  turbo01             ccdc1edfcdc8        19 months ago       600MB
osallou/cnvnator       latest              90fba991edb8        3 years ago         1.1GB

```


### get the id, repository and tag
```
$ docker image ls --format "{{.ID}}\t{{.Repository}}\t{{.Tag}}"
ae513a47849c    nginx   latest
452a96d81c30    ubuntu  latest
860ff7912c63    genevera/docker-pigz    latest
7e928b3e6784    wwliao/cnvnator latest
e6eca03649a6    qiime2/core 2017.7
1815c82652c0    hello-world latest
ccdc1edfcdc8    rmats   turbo01
90fba991edb8    osallou/cnvnator    latest

```

### get details of image
```
$ docker image ls --digests
REPOSITORY             TAG                 DIGEST                                                                    IMAGE ID            CREATED             SIZE
nginx                  latest              sha256:0fb320e2a1b1620b4905facb3447e3d84ad36da0b2c8aa8fe3a5a81d1187b884   ae513a47849c        7 months ago        109MB
ubuntu                 latest              sha256:c8c275751219dadad8fa56b3ac41ca6cb22219ff117ca98fe82b42f24e1ba64e   452a96d81c30        7 months ago        79.6MB
genevera/docker-pigz   latest              sha256:fd81c17eafd3d7bdb361aa86f2ed6261d3afa8feecd5ccc1731726c4ae7ba86b   860ff7912c63        7 months ago        4.17MB
wwliao/cnvnator        latest              sha256:0d4f88cedc4160b5246f77bd120d816dc6dba08e51c93653591c4b4fefbc9133   7e928b3e6784        13 months ago       1.43GB
qiime2/core            2017.7              sha256:65e608ef22aa4083ea5dd90acce8ee8185d567ae19e37f63531b408cdfc18888   e6eca03649a6        16 months ago       5.19GB
hello-world            latest              sha256:f3b3b28a45160805bb16542c9531888519430e9e6d6ffc09d72261b0d26ff74f   1815c82652c0        17 months ago       1.84kB
rmats                  turbo01             <none>                                                                    ccdc1edfcdc8        19 months ago       600MB
osallou/cnvnator       latest              sha256:8f03a4c80cb1a1c88fe562361565cbf337ca9114baa1a00940accf2a69806ad0   90fba991edb8        3 years ago         1.1GB
```


### delete dangling image

```
$ docker image ls --filter dangling=true
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
```

no dangling image 

If it has dangling image, run this command to delete it:
```
$ docker image prune
WARNING! This will remove all dangling images.
Are you sure you want to continue? [y/N] y
Total reclaimed space: 0B

```


### list images after one certain image

#### list all images
```
$ docker image ls -a
REPOSITORY             TAG                 IMAGE ID            CREATED             SIZE
nginx                  latest              ae513a47849c        7 months ago        109MB
ubuntu                 latest              452a96d81c30        7 months ago        79.6MB
genevera/docker-pigz   latest              860ff7912c63        7 months ago        4.17MB
wwliao/cnvnator        latest              7e928b3e6784        13 months ago       1.43GB
qiime2/core            2017.7              e6eca03649a6        16 months ago       5.19GB
hello-world            latest              1815c82652c0        17 months ago       1.84kB
rmats                  turbo01             ccdc1edfcdc8        19 months ago       600MB
osallou/cnvnator       latest              90fba991edb8        3 years ago         1.1GB

```

#### list images after ubuntu
```
$ docker image ls --filter since=ubuntu:latest
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
nginx               latest              ae513a47849c        7 months ago        109MB

```

## run docker image

### parameters of running

```
$ docker run --help

Usage:  docker run [OPTIONS] IMAGE [COMMAND] [ARG...]

Run a command in a new container

Options:
      --add-host list                  Add a custom host-to-IP mapping (host:ip)
  -a, --attach list                    Attach to STDIN, STDOUT or STDERR
      --blkio-weight uint16            Block IO (relative weight), between 10 and 1000, or 0 to
                                       disable (default 0)
      --blkio-weight-device list       Block IO weight (relative device weight) (default [])
      --cap-add list                   Add Linux capabilities
      --cap-drop list                  Drop Linux capabilities
      --cgroup-parent string           Optional parent cgroup for the container
      --cidfile string                 Write the container ID to the file
      --cpu-period int                 Limit CPU CFS (Completely Fair Scheduler) period
      --cpu-quota int                  Limit CPU CFS (Completely Fair Scheduler) quota
      --cpu-rt-period int              Limit CPU real-time period in microseconds
      --cpu-rt-runtime int             Limit CPU real-time runtime in microseconds
  -c, --cpu-shares int                 CPU shares (relative weight)
      --cpus decimal                   Number of CPUs
      --cpuset-cpus string             CPUs in which to allow execution (0-3, 0,1)
      --cpuset-mems string             MEMs in which to allow execution (0-3, 0,1)
  -d, --detach                         Run container in background and print container ID
      --detach-keys string             Override the key sequence for detaching a container
      --device list                    Add a host device to the container
      --device-cgroup-rule list        Add a rule to the cgroup allowed devices list
      --device-read-bps list           Limit read rate (bytes per second) from a device (default [])
      --device-read-iops list          Limit read rate (IO per second) from a device (default [])
      --device-write-bps list          Limit write rate (bytes per second) to a device (default [])
      --device-write-iops list         Limit write rate (IO per second) to a device (default [])
      --disable-content-trust          Skip image verification (default true)
      --dns list                       Set custom DNS servers
      --dns-option list                Set DNS options
      --dns-search list                Set custom DNS search domains
      --entrypoint string              Overwrite the default ENTRYPOINT of the image
  -e, --env list                       Set environment variables
      --env-file list                  Read in a file of environment variables
      --expose list                    Expose a port or a range of ports
      --group-add list                 Add additional groups to join
      --health-cmd string              Command to run to check health
      --health-interval duration       Time between running the check (ms|s|m|h) (default 0s)
      --health-retries int             Consecutive failures needed to report unhealthy
      --health-start-period duration   Start period for the container to initialize before
                                       starting health-retries countdown (ms|s|m|h) (default 0s)
      --health-timeout duration        Maximum time to allow one check to run (ms|s|m|h) (default 0s)
      --help                           Print usage
  -h, --hostname string                Container host name
      --init                           Run an init inside the container that forwards signals
                                       and reaps processes
  -i, --interactive                    Keep STDIN open even if not attached
      --ip string                      IPv4 address (e.g., 172.30.100.104)
      --ip6 string                     IPv6 address (e.g., 2001:db8::33)
      --ipc string                     IPC namespace to use
      --isolation string               Container isolation technology
      --kernel-memory bytes            Kernel memory limit
  -l, --label list                     Set meta data on a container
      --label-file list                Read in a line delimited file of labels
      --link list                      Add link to another container
      --link-local-ip list             Container IPv4/IPv6 link-local addresses
      --log-driver string              Logging driver for the container
      --log-opt list                   Log driver options
      --mac-address string             Container MAC address (e.g., 92:d0:c6:0a:29:33)
  -m, --memory bytes                   Memory limit
      --memory-reservation bytes       Memory soft limit
      --memory-swap bytes              Swap limit equal to memory plus swap: '-1' to enable
                                       unlimited swap
      --memory-swappiness int          Tune container memory swappiness (0 to 100) (default -1)
      --mount mount                    Attach a filesystem mount to the container
      --name string                    Assign a name to the container
      --network string                 Connect a container to a network (default "default")
      --network-alias list             Add network-scoped alias for the container
      --no-healthcheck                 Disable any container-specified HEALTHCHECK
      --oom-kill-disable               Disable OOM Killer
      --oom-score-adj int              Tune host's OOM preferences (-1000 to 1000)
      --pid string                     PID namespace to use
      --pids-limit int                 Tune container pids limit (set -1 for unlimited)
      --privileged                     Give extended privileges to this container
  -p, --publish list                   Publish a container's port(s) to the host
  -P, --publish-all                    Publish all exposed ports to random ports
      --read-only                      Mount the container's root filesystem as read only
      --restart string                 Restart policy to apply when a container exits (default "no")
      --rm                             Automatically remove the container when it exits
      --runtime string                 Runtime to use for this container
      --security-opt list              Security Options
      --shm-size bytes                 Size of /dev/shm
      --sig-proxy                      Proxy received signals to the process (default true)
      --stop-signal string             Signal to stop a container (default "SIGTERM")
      --stop-timeout int               Timeout (in seconds) to stop a container
      --storage-opt list               Storage driver options for the container
      --sysctl map                     Sysctl options (default map[])
      --tmpfs list                     Mount a tmpfs directory
  -t, --tty                            Allocate a pseudo-TTY
      --ulimit ulimit                  Ulimit options (default [])
  -u, --user string                    Username or UID (format: <name|uid>[:<group|gid>])
      --userns string                  User namespace to use
      --uts string                     UTS namespace to use
  -v, --volume list                    Bind mount a volume
      --volume-driver string           Optional volume driver for the container
      --volumes-from list              Mount volumes from the specified container(s)
  -w, --workdir string                 Working directory inside the container

```

#### run example
```
$ docker run -it ubuntu bash
root@1b0ca9f315ab:/# ls
bin  boot  dev  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
```

* -i: interactive
* -t: terminator


## system of docker

### parameters
```
$ docker system --help

Usage:  docker system COMMAND

Manage Docker

Options:
      --help   Print usage

Commands:
  df          Show docker disk usage
  events      Get real time events from the server
  info        Display system-wide information
  prune       Remove unused data

Run 'docker system COMMAND --help' for more information on a command.

```

### spece of image, container and colume
```
$ docker system df
TYPE                TOTAL               ACTIVE              SIZE                RECLAIMABLE
Images              8                   8                   8.507GB             0B (0%)
Containers          38                  0                   173.5kB             173.5kB (100%)
Local Volumes       27                  27                  0B                  0B

```


## delete image

#### parameters
```
$ docker image rm --help

Usage:  docker image rm [OPTIONS] IMAGE [IMAGE...]

Remove one or more images

Aliases:
  rm, rmi, remove

Options:
  -f, --force      Force removal of the image
      --help       Print usage
      --no-prune   Do not delete untagged parents

```

### example of removing image


```
$ docker image rm ubuntu
Error response from daemon: conflict: unable to remove repository reference "ubuntu" (must force) - container b2bde846429e is using its referenced image 452a96d81c30

```

Some images may be not removed if it is used by other repository.

Then we can **force** remove the image

```
$ docker image rm --force ubuntu
Untagged: ubuntu:latest
Untagged: ubuntu@sha256:c8c275751219dadad8fa56b3ac41ca6cb22219ff117ca98fe82b42f24e1ba64e
Deleted: sha256:452a96d81c30a1e426bc250428263ac9ca3f47c9bf086f876d11cb39cf57aeec

```


### delete all repositories with name of redis 
```
$ docker image rm $(docker image ls -q redis)
```

### delete all images since one certain image

```
$ docker image rm $(docker image ls -q -f before=mongo:3.2)
```