# 2015-10-20 15:51:50
# version 1.0
# Author:robo_one
# Function:this script is a diary editor
# read,write,open,print
# -*- coding: utf-8 -*-


from sys import argv
script , input_file = argv

current_file = open(input_file, 'a')

# import sys data,time
import datetime
now = datetime.datetime.now()
otherStyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
#read diary
def diary_read(f):
	print "Your file %r:" % input_file
	f.seek(0,0)
	print current_file.read()
	current_file.close()

# function write
def diary_write(f):
	line = raw_input("-->")
	current_file.write("Time %r  \r\n" % otherStyleTime)
	current_file.write(line)
	current_file.write("\n")
	
	print "Save,we'll close it **** "
	current_file.close()

def diary_main():
	print "***Press 'w' or 'W' write diary.********\n"
	print "***Press 'r' or 'R' read all diary.*****\n"
	a = raw_input("?")
	if a=='w' or a=='W':
		diary_write(current_file)
	elif a=='r' or a=='R':
		diary_read(current_file)
	else:
		print "Error,plz input w or r?"
					

while 1:
	diary_main()
	