# -*- coding: utf-8 -*-

import socket
import sys,codecs
import datetime

reload(sys)
sys.setdefaultencoding('GB2312') #������win-cmd����

UDP_IP = "127.0.0.1"
UDP_PORT = 9527

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind(('', UDP_PORT))        #''��ʾ������������IP��ַ
data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes

diary =  addr[0] + ".txt"  #��IP��ַ.txt ��ʽ����,����diary_txt��Ϊȫ�ֱ���


def open_diary(diary):    
   o = open(diary,'a')
   content = o.read()
   sock.sendto(content,addr)
   o.close()
   print "��־�ѷ�����%s" %addr[0]

    
def save(data,diary):
    now = datetime.datetime.now()
    otherStyleTime = now.strftime("%Y-%m-%d %H:%M:%S") #�ο���һ�ܴ���
    s = open(diary,'a')
    s.write(otherStyleTime+":"+data+ "\n")
    s.close()
    print "��־�ѱ�����%s" %diary

#�ο���һ�ܴ���    
def main():
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    s=open(diary,'a') #�½�txt�ļ�


    if data=='r' or data=='R':
        print "Loading..."
        open_diary(diary)
    else:
        print "�Ѷ�:", data, "����-->", addr[0]
        save(data,diary)

while 1:
    print "*** %s���ռǱ�--��������********\n" %addr[0]
    main()



