# -*- coding: utf-8 -*-
#日记本客户端,CMD运行Python S.PY
#先启动S.PY，在运行C.PY

import socket
import sys,codecs
import datetime

reload(sys)
sys.setdefaultencoding('GB2312') #适用于win-cmd运行

UDP_IP = "127.0.0.1"
UDP_PORT = 8080


#def open_diary(diary):    


    
def save(data,diary):
    now = datetime.datetime.now()
    otherStyleTime = now.strftime("%Y-%m-%d %H:%M:%S") #参考第一周代码
    s = open(diary,'a')
    s.write(otherStyleTime+":"+data+ "\n")
    s.close()
    print "日志已保存至%s" %diary

#参考第一周代码    
def main():
    sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
    sock.bind(('', UDP_PORT))        #''表示接收域内所以IP地址
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    diary =  addr[0] + ".txt"  #以IP地址.txt 格式保存,并将diary_txt作为全局变量
    print "*** %s的日记本--服务器端********\n" %addr[0]


    
    if data=='r' or data=='R':
        print "Loading..."
        #open_diary(diary)
        o = open(diary,'r')
        content = o.read()
        #print type(content)
        sock.sendto(content,addr)
        o.close()
        print  "日志已发送至%s" %addr[0]
    else:
        print "已读:", data, "来自-->", addr[0]
        save(data,diary)


while 1:
    main()