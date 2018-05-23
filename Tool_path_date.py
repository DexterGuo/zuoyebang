#! /usr/local/bin/python
# -*- coding:utf-8 -*-
#

import sys
import datetime
import os
import shutil
import logging

def get_last_date():
    # https://blog.csdn.net/evillist/article/details/50522505
    yesterday = datetime.date.today()-datetime.timedelta(days=1)
    return yesterday.strftime('%Y%m%d')

def mkdir_new_path(pathname="./out/"):
    logging.info("start working")
    date = get_last_date()
    if pathname[-1] != "/":
        pathname += "/"
    pathname += date+"/"
    exists = os.path.exists(pathname)
    if exists:
        shutil.rmtree(pathname, True)
    try:
        os.mkdir(pathname)
    except:
        logging.error("Failed mkdir %s"% pathname)
    try:
        os.mkdir(os.path.join(pathname, "subdata/"))
        os.mkdir(os.path.join(pathname, "isSmall/"))
        os.mkdir(os.path.join(pathname, "hashed/"))
        os.mkdir(os.path.join(pathname, "tidpv/"))
    except:
        logging.error("Failed mkdir under %s"% pathname)
    logging.info("end working")
    return pathname

def get_uda_data(pathname="./data/"):
    logging.info("start working get_uda_data")
    if not os.path.exists(pathname):
        logging.error("must give a right uda data dir")
        exit(0)
    datapath = ""
    date = get_last_date()
    for root, dirs, files in os.walk(pathname):
        if date in dirs:
            datapath = root
            break
    datapath = os.path.join(datapath, date)
    if not datapath:
        logging.error("are you sure there has yesterday's uda data in %s"%pathname)
        exit(0)
    for root, dirs, files in os.walk(datapath):
        break
    if len(files) != 1:
        logging.error("please check the the dir %s"%datapath)
        exit(0)
    datapath = os.path.join(datapath, files[0])
    logging.info("end working get_uda_data")
    return datapath

if __name__ == "__main__":
    date = get_last_date()
    print("yesterday is : " + date)
    pathname = "./tmp"
    newpathname = mkdir_new_path(pathname)
    print(newpathname)
    datapath = get_uda_data()
    print(datapath)

