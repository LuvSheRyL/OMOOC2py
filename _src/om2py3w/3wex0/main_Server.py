# -*- coding: utf-8 -*-

import socket
import sys,codecs
import datetime

reload(sys)
sys.setdefaultencoding('GB2312') #������win-cmd����

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind(('', UDP_PORT))        #''��ʾ������������IP��ַ
data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes

diary =  addr[0] + ".txt"  #��IP��ַ.txt ��ʽ����,����diary_txt��Ϊȫ�ֱ���

def diary_open(diary):    
   diary_o = open('diary.txt','a')
   diary_content = diary_o.read()
   sock.sendto(diary_content,addr)
   diary_o.close()
   print "��־�Ѵ�"
   return history
    
def diary_save(history,diary):
    now = datetime.datetime.now()
    otherStyleTime = now.strftime("%Y-%m-%d %H:%M:%S") #�ο���һ�ܴ���
    diary_s=open('diary.txt','a')
    diary_s.write(otherStyleTime+":"+diary_s.read()+"\n")
    
    diary_s.close()
    


while 1:

    print "�Ѷ�:", data, "����-->", addr[0]
    print "��־������" + diary
    
    if data == "open":
        diary_open(diary)
     
    if data == 'save':
        print "�ѱ���"
        diary_save(data,diary)


