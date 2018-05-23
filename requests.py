#!/usr/local/bin/python
# -*- coding:utf-8 -*-
# http://python.jobbole.com/86822/


import sys
import os
import urllib2
import urllib
import json
import random
import logging

from configure import IP_LIST as ip_list

def requests(datafile, outpath, is_small):
    # logging.info("start woking")
    pidNum = os.getpid()
    outname = outpath + str(is_small) + "_out_" + str(pidNum)
    fout = open(outname, 'w')
    fin = open(datafile, "r")
    for line in fin.readlines():
        tokens = line.strip("\n").split("\t")
        if len(tokens) != 3:
            fout.write( tokens[0]+"\tnull\n")
            continue
        query = tokens[2].replace("@", '-|||-')
        sid = tokens[0]
        pid = tokens[1]
        ip = random.choice(ip_list)
        url = 'http://' + ip + ':8990/seproxy/query?strWords='+urllib.quote(query)+'&sid='+str(sid)+'&isSmall='+str(is_small)+'&limit=10&offset=0'
        try:
            result =  urllib2.urlopen(url, timeout=10).read()
        except:
            fout.write( sid + "\tnull\n")
            continue
        try:
            result_json = json.loads(result)
        except:
            fout.write( sid + "\tnull\n")
            continue
        try:
            out_tid_info = ""
            proc_num = min(1, len(result_json['data']['Item']))
            if proc_num <= 0:
                fout.write( sid + "\tnull\n")
                continue
            temp_dict = {}
            for i in range(0, proc_num):
                rtid = int(result_json['data']['Item'][i]['tid'])
                out_tid_info += ",%d"%(rtid)
            fout.write( sid + "\t" + out_tid_info[1:] + "\n")
        except:
            fout.write(sid+"\tnull\n")
            # print sid + "\tnull"
            continue
    # logging.info("end woking")
    fin.close()
    fout.close()
