# -*- coding: utf-8 -*-
import socket
import sys,codecs
reload(sys)
sys.setdefaultencoding('GB2312')

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
def diary_open():    #��IP��ַ.txt ��ʽ����
    diary_text = 


def server_con():
    sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
    sock.bind(('', UDP_PORT))        #''��ʾ������������IP��ַ
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print "�Ѷ�:", data, "����", addr
    if data == "open" or "OPEN":
     print "���ڴ���־����" 
        
    elif data == "save" or "SAVE":
     print "��־�ѱ��桭��"
        
        

       

while 1:
    server_con()

    
