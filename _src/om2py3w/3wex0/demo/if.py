# -*- coding: utf-8 -*-

import sys,time
import socket

reload(sys)
sys.setdefaultencoding('GB2312') #适用于win-cmd运行

msg = raw_input(u"请输入") 

while True:
 if msg == 'a':
  print "a--"
  s=open('a.txt','a')
  b = raw_input("-->")
  s.write(b+"\n")
  s.close()
  sys.exit()

 elif msg == 'b':
  print "b--"
  
 else:
  print "over"
 
