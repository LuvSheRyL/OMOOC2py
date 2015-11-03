# -*- coding: utf-8 -*-
import socket
import sys,codecs
reload(sys)
sys.setdefaultencoding('GB2312') #在CMD中运行编码为GB2312，在Python中应修改为UTF-8

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
ip_address = (UDP_IP,UDP_PORT)




sock = socket.socket(socket.AF_INET, # Internet地址族
                     socket.SOCK_DGRAM) # UDP协议

while 1:
    MESSAGE =  raw_input("请输入:") #一次只能一行内容
    
    if MESSAGE == 'open':
     print "正在打开日志……" 
     sock.sendto(MESSAGE,ip_address)
     sock.recv(1024)
        
    if MESSAGE == 'save':     
     print "日志已保存……"
     
    else:
     sock.sendto(MESSAGE,ip_address)
     print "UDP target IP:", UDP_IP
     print "UDP target port:", UDP_PORT
     print "已发送信息:", MESSAGE