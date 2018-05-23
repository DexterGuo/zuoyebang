#!/usr/local/bin/python
# -*- coding:utf-8 -*-
# http://python.jobbole.com/86822/


import sys
import os
import time
import json
from multiprocessing import Process
import logging

from requests import requests

def multi_Process(datafile, outpath, threadNum, is_small=98):
    logging.info("start working")
    if not outpath:
        if outpath[-1] != "/":
            outpath += "/"
    if not os.path.exists(datafile):
        logging.error("uda data file isn't existed")
        exit(0)
    wcNum = len(open(datafile,"r").readlines())
    subFileLen = wcNum/threadNum
    out_subdata = os.path.join(outpath, "subdata/")
    try:
        split_file = "split %s -l %d %ssmall_"%(datafile, subFileLen, out_subdata)
        os.system(split_file)
    except Exception, e:
        logging.error("Failed in split subfile: %s",e)
    files = os.listdir(out_subdata)
    # multi-Process
    start_time = time.time()
    out_issmall = os.path.join(outpath, "isSmall/")
    if not os.path.exists(out_issmall):
        try:
            os.mkdir(out_issmall)
        except Exception,e:
            logging.error(e)
    processes = []
    for f in files:
        filename = os.path.join(out_subdata, f)
        pro = Process(target=requests, args=(filename, out_issmall, is_small))
        processes.append(pro)
        pro.start()
    e = processes.__len__()
    while True:
        for th in processes:
            if not th.is_alive():
                e -= 1
        if e <= 0:
            break
    used_time = time.time() - start_time
    
    logging.info("end working")
    return used_time
