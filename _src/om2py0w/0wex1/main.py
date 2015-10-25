# -*- coding: utf-8 -*-
# 2015-10-21 14:17:58
# version 1.1
# Author:robo_one
# Function:this script is a diary editor
# read,write,open,print



from sys import argv
script , input_file = argv

import sys
reload(sys)
sys.setdefaultencoding('GB2312')

# import sys data,time
import datetime

#read diary
#def diary_read(f):
#	print "Your file %r:" % input_file
#	f.seek(0,0)
#	print current_file.read()
#	current_file.close()

# function write
def diary_write(f):
	now = datetime.datetime.now()
	otherStyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
	#current_file = open(input_file, 'a+')
	line = raw_input("-->")
	f.write(u"--- 时间%s --- \n" % otherStyleTime)
	f.write(line)
	f.write("\n")
	print "Save,we'll save it **** "
	f.close()

def diary_main():
	current_file = open(input_file, 'a+')
	print "***Press 'w' or 'W' write diary.********\n"
	print "***Press 'r' or 'R' read all diary.*****\n"
	a = raw_input("W OR R?")
	if a=='w' or a=='W':
		diary_write(current_file)
		
	elif a=='r' or a=='R':
		diary_read = open(input_file,'r')
		print "Loading..."
		print diary_read.read()
		diary_read.close()
	else:
		print "Error,plz input w or r?"
	
	
		

while 1:
	diary_main()
	