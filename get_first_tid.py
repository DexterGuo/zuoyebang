#!/usr/local/bin/python

import sys

while True:
	strLine = sys.stdin.readline()
	if strLine == "":
		break
	arrFields = strLine.strip('\n').replace("\x01", "\t").split('\t')
	if len(arrFields) == 5: #cuid, sid, createTime, resultnum, resultcontent
		arrTIDs = arrFields[4].strip('[]').split(',')
		if len(arrTIDs) > 0 and arrTIDs[0] != "":
			sys.stdout.write("%s\t%s\n"%(arrTIDs[0], arrFields[1]))
