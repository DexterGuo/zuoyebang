#!/usr/local/bin/python

import sys
import json
import logging
import logging.config
import time

log_filename = "tk_logging_guo.log"
logging.basicConfig(level=logging.DEBUG, filename = log_filename,
    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filemode='a')

while True:
    strLine = sys.stdin.readline()
    #print(strLine)
    if strLine == "":
        break
    arrFields = strLine.strip('\n').replace("\x01", "\t").split('\t')
    if len(arrFields) == 3: #sid, pid, ext
        try:
            ext_all = arrFields[2]
            ext_all = json.loads(ext_all)["ocrResult"]
            ext_ocr = json.loads(ext_all)["ret"]
            ext_str = ""
            for ext_info in ext_ocr:
                ext_str += "@" + ext_info["word"].encode("UTF-8")
            if ext_str:
                ext_str = ext_str[1:]
            sys.stdout.write("%s\t%s\t%s\n"%(arrFields[0], arrFields[1], ext_str))
        except:
            err_str = "error-guo-"+strLine
            logging.error(err_str)
            
