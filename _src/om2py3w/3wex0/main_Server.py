# -*- coding: utf-8 -*-

import socket
import sys,codecs
import datetime

reload(sys)
sys.setdefaultencoding('GB2312') #适用于win-cmd运行

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind(('', UDP_PORT))        #''表示接收域内所以IP地址
data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes

diary =  addr[0] + ".txt"  #以IP地址.txt 格式保存,并将diary_txt作为全局变量

def diary_open(diary):    
   diary_o = open('diary.txt','a')
   diary_content = diary_o.read()
   sock.sendto(diary_content,addr)
   diary_o.close()
   print "日志已打开"
   return history
    
def diary_save(history,diary):
    now = datetime.datetime.now()
    otherStyleTime = now.strftime("%Y-%m-%d %H:%M:%S") #参考第一周代码
    diary_s=open('diary.txt','a')
    diary_s.write(otherStyleTime+":"+diary_s.read()+"\n")
    
    diary_s.close()
    


while 1:

    print "已读:", data, "来自-->", addr[0]
    print "日志保存在" + diary
    
    if data == "open":
        diary_open(diary)
     
    if data == 'save':
        print "已保存"
        diary_save(data,diary)


