# -*-coding:utf-8 -*-

import sys
import os
from collections import Counter
import logging
#import numpy as np

def hash_files_to_Mfiles(issmall_path, hashed_path, Mfile, is_small=98):
    logging.info("start working")
    logging.info("issmall_path: %s"%issmall_path)
    logging.info("hashed_path: %s"%hashed_path)
    files = os.listdir(issmall_path)
    files_98 = [f for f in files if f.startswith(str(is_small))]
    if len(files_98) == 0:
        logging.error("can't get the requests' result in the path %s"%issmall_path)
        exit(0)
    outfiles = []
    for i in range(Mfile):
        filename = hashed_path + "hash_" + str(i+1)
        outfiles.append(open(filename, "w"))
    for f98 in files_98:
        filename = os.path.join(issmall_path, f98)
        while not os.path.getsize(filename):
            continue
        fp = open(filename, "r")
        for line in fp.readlines():
            tid = line.strip("\n").split("\t")[1]
            tid_hash = hash(tid)%Mfile
            tid += "\n"
            outfiles[tid_hash].write(tid)
        fp.close()
    for outf in outfiles:
        outf.close()
    logging.info("end working")
    return 0 

def get_tid_pv(inpath, outpath, Mfile, topN=3000):
    logging.info("start working")
    while True:
        files = os.listdir(inpath)
        if len(files) == Mfile:
            break
    for f in files:
        filename = os.path.join(inpath, f)
        while not os.path.getsize(filename):
            continue
        tidpv = "tidpv_"+f
        tid_pv_name = os.path.join(outpath, tidpv)
        tids = []
        for tid in  open(filename, "r").readlines():
            tids.append(tid.strip("\n"))
        # tids = zip(*np.unique(tids, return_counts=True))
        # tids = sorted(tids, key=lambda x:x[1], reverse=True)
        tids = sorted(tids)
        dict_tids = Counter(tids)
        tids = sorted(dict_tids.items(), key=lambda x:x[1], reverse=True)

        lenN = min(len(tids), topN)
        topn = 1
        fout = open(tid_pv_name, "w")
        for tid,num in tids:
            if topn>lenN:
                break
            info = str(tid) + "\t" + str(num) + "\n"
            fout.write(info)
        fout.close()
    logging.info("end working")
    return 0

if __name__ == "__main__":
    tid_pv_path = "./out/20180522/tidpv/"
    hashed_path = "./out/20180522/hashed/"
    Mfile = 10
    is_small = 98
    topN = 300
    issmall_path = "./out/20180522/isSmall/"
    hash_files_to_Mfiles(issmall_path, hashed_path, Mfile, is_small)
    # get_tid_pv(hashed_path, tid_pv_path, topN)
