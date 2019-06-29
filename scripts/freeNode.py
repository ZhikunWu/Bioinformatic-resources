#!/usr/bin/env python
from __future__ import division
import subprocess
import argparse
import collections
import operator


#usage: python ~/github/NanoHub/src/NanoHub/freeNode.py

def free_nodes_for_cluster():
    NodeAvailable = collections.defaultdict()
    NodeUse = collections.defaultdict()
    output = subprocess.Popen(['pestat'],stdout=subprocess.PIPE,shell=True).communicate()
    nodes = str(output[0]).lstrip("b'").rstrip("'").split("\\n")[:-1]
    for node in nodes:
        stat = node.split("\\t")
        stats = [s.strip() for s in stat]
        ### stats:
        ### ["cu01", 'free', '0.38*', '128495', '24', '160495', '17108', '3/3', '1', '[85814:NONE*]']
        node = stats[0]
        ### state: "free", "excl"
        state = stats[1]
        memTotal = stats[3]
        memUse = stats[6]
        memTotal = int(memTotal)
        memUse = int(memUse)
        usedCPU = stats[2]
        ### get avaiable ratio for memory for node
        freeRatio = (memTotal - memUse) / memTotal
        if state == "free":
            NodeAvailable[node] = freeRatio
            NodeUse[node] = usedCPU

    ### get most available node
    sortedMem = sorted(NodeAvailable.items(), key=operator.itemgetter(1), reverse=True)
    for n in sortedMem:
        node, menRatio = n
        used = NodeUse[node]
        print("%s\t%f\t%s" % (node, menRatio, used))

if __name__ == "__main__":
    free_nodes_for_cluster()


