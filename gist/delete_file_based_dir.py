#!/usr/bin/env python
import os
import sys


def is_dir(directory):
    if not os.path.isdir(directory):
        print("Please check whether %s is a directory." % directory)
        sys.exit(1)
    if not directory.endswith("/"):
        directory += "/"
    return directory


def delete_dir_files(query_dir, target_dir):
    """
    argv:
    query_dir (temp1), target_dir (temp2)

    $ tree temp*
    temp1
    ├── qq
    └── ww
    temp2
    ├── ee
    ├── qq
    └── ww
    
    delete_dir_files("temp1", "temp2")

    retrun:
    $ tree temp*
    temp1
    ├── qq
    └── ww
    temp2
    └── ee
    """
    Querys = {}
    query_dir = is_dir(query_dir)
    files = os.listdir(query_dir)
    for f in files:
        Querys[f] = 1
    target_dir = is_dir(target_dir)
    tfiles = os.listdir(target_dir)
    for t in tfiles:
        if t in Querys:
            tt = target_dir + t
            cmd = "rm %s" % tt
            os.system(cmd)

