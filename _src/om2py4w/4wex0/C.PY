# -*- coding: utf-8 -*-
import socket
import sys,codecs
reload(sys)
sys.setdefaultencoding('GB2312') #在CMD中运行编码为GB2312，在Python中应修改为UTF-8

UDP_IP = "127.0.0.1"
UDP_PORT = 9527
ip_address = (UDP_IP,UDP_PORT)


def main():
    sock = socket.socket(socket.AF_INET, # Internet地址族
                     socket.SOCK_DGRAM) # UDP协议
                     
    print '''
    欢迎来到*** %s的日记本--********
    输入‘r’---载入历史记录
    
    '''%UDP_IP
    MESSAGE =  raw_input("写点什么呢:") #一次只能一行内容
    
    if MESSAGE == 'r':
        print "正在打开日志……" 
        sock.sendto(MESSAGE,ip_address)
        print sock.recv(1024)
   
    else:
     sock.sendto(MESSAGE,ip_address)
     print "UDP target IP:", UDP_IP
     print "UDP target port:", UDP_PORT
     print "已发送信息:", MESSAGE
                     
while 1:
    main()