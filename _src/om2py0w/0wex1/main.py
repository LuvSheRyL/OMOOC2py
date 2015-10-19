# 2015-10-18 22:21:58
# version 1.0
# Author:robo_one
# Function:this script is a diary editor
# read,write,open,print
#encoding=utf-8  


from sys import argv

#diary_write, diary_read, diary_name = argv

import datetime

now = datetime.datetime.now()

otherStyleTime = now.strftime("%Y-%m-%d %H:%M:%S")


def diary_write ():
	while Ture:
		print "%r\r\n " % otherStyleTime
		txt = raw_input(otherStyleTime)
		if len(txt) < 2 :
			print ("Too short txt")
		elif len(txt) > 2 :
			
		return txt
				break
diary_write()

