#!/bin/env python
# coding=utf-8

'''A simple sentence to describe the function of this module.

Add detailed description here if need.

Eample:
    # python ./sample.py -t
    # ...
'''
# 导入Tk GUI模块
from Tkinter import *
from os.path import exists
from ScrolledText import *
import tkMessageBox
from tkFileDialog import *
import fileinput
import time

# Can be 'Prototype', 'Development', 'Product'
__status__ = 'Development'
__author__ = 'robo_one <robo_one@foxmail.com>'

# Add your code here
# Delete the description when you start coding.
			
class diary(Frame):
	def diary_widgets(self):
		self.open = Button(self)
		self.open["text"] = "打开文件"
		self.open["fq"] = "Blue"
		self.open["command"] = self.diary_read_print
		self.open.pack({"side":"left"})
	
	self.st=ScrolledText(self.f,background="white")
	self.st.pack(side=LEFT,fill=BOTH,expand=1)
	
	def diary_read_print(self):
	 p1=END
	 oname=askopenfilename(filetypes=[("Python file","*.*")])
	  if oname:
		for line in fileinput.input(oname):
			self.st.insert(p1,line)
	   self.t.title(oname)
	
root = Tk()
app = diary(master=root)
app.mainloop()
root.destory()
	
	

if __name__ == '__main__':
    main()

# vim: set expandtab smarttab shiftwidth=4 tabstop=4: