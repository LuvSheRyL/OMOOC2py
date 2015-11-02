# -*- coding: utf-8 -*-
import socket
import sys,codecs
reload(sys)
sys.setdefaultencoding('GB2312')

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
def diary_open():    #已IP地址.txt 格式保存
    diary_text = 


def server_con():
    sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
    sock.bind(('', UDP_PORT))        #''表示接收域内所以IP地址
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print "已读:", data, "来自", addr
    if data == "open" or "OPEN":
     print "正在打开日志……" 
        
    elif data == "save" or "SAVE":
     print "日志已保存……"
        
        

       

while 1:
    server_con()

    
