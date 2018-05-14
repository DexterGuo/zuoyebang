#!/usr/local/bin/python
import sys

strLastTID = ""
arrLines = []

def get_result(arrLines):
	strResult = None
	#print "*********"
	#print arrLines
	#print "---------"
	strTID = arrLines[0].strip('\n').replace("\x01", "\t").split('\t')[0]
	arrSID = []
	for strLine in arrLines:
		arrFields = strLine.strip('\n').replace("\x01", "\t").split('\t')
		arrSID.append(arrFields[1])
	#print "tid", strTID
	#print "arrSID", arrSID
		
	strResult = "%s\t%d"%(strTID, len(arrLines))
	return strResult


while True:
	strLine = sys.stdin.readline()
	if strLine == "":
		break
	arrFields = strLine.strip('\n').replace("\x01", "\t").split('\t')
	strCurrentTID = arrFields[0]
	if strLastTID == "":
		strLastTID = strCurrentTID

	if strLastTID != strCurrentTID:
		strOutput = get_result(arrLines)
		if strOutput != None:
			sys.stdout.write(strOutput+"\n")

		strLastTID = strCurrentTID
		arrLines = []
		arrLines.append(strLine)
	else:
		arrLines.append(strLine)

if len(arrLines) > 0:
	strOutput = get_result(arrLines)
	if strOutput != None:
		sys.stdout.write(strOutput+"\n")