# -*- utf-8 -*-
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

            err_str = "error-guo-"+strLine
            logging.error(err_str)
            
