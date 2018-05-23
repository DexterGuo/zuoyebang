# -*- coding:utf-8 -*-
# https://blog.csdn.net/minxihou/article/details/51857518

import sys
import os
import heapq
import logging

from Tool_path_date import get_last_date

def get_topN_from_Mfiles(pathname, outpath, Mfile, topN=3000):
    logging.info("start working")
    if pathname[-1] != "/":
        pathname += "/"
    if not os.path.exists(pathname):
        logging.info("%s isn't existed"%pathname)
        exit(0)
    while True:
        files = os.listdir(pathname)
        if len(files) == Mfile:
            break
    fps = []
    for f in files:
        filename = os.path.join(pathname, f)
        fps.append(open(filename, "r"))
    hq = []
    for i in range(Mfile):
        try:
            line = fps[i].readline().strip("\n").split("\t")
            info = (0-int(line[1]), line[0], i) #pv, tid, index
            heapq.heappush(hq, info)
        except:
            logging.error("wrong when create heapq")
            continue
    topNpvpath = os.path.join(outpath,"topNpv.tid")
    fpv = open(topNpvpath, "w")
    top = 1
    while len(hq)>0 and top <= topN:
        top += 1
        pv_, tid, index = heapq.heappop(hq)
        pv_info = "%s\t%d\n"%(tid, 0-pv_)
        fpv.write(pv_info)
        try:
            line = fps[index].readline().strip("\n").split("\t")
            info = (0-int(line[1]), line[0], i) #pv, tid, index
            heapq.heappush(hq, info)
        except:
            logging.error("wrong when push heapq")
            continue

    for fp in fps:
        fp.close()
    fpv.close()
    logging.info("end working")

    return 0

if __name__ == "__main__":
    topN = 300
    pathname = "./"
    if len(sys.argv) >= 4:
        print("you input too many parameters!")
        exit(0)
    elif len(sys.argv) == 1:
        print("you need to input the work path at least!")
        exit(0)
    if len(sys.argv) == 3:
        topN = int(sys.argv[2])
    pathname = sys.argv[1]

    res = get_topN_from_Mfiles(pathname, "./", topN)
    if res == 0:
        pass
    if res == 1:
        print("there is no file in %s"%pathname)
    
