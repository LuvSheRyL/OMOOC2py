# -*- coding: utf-8 -*-
import socket
import sys,codecs
reload(sys)
sys.setdefaultencoding('GB2312') #��CMD�����б���ΪGB2312����Python��Ӧ�޸�ΪUTF-8

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
ip_address = (UDP_IP,UDP_PORT)




sock = socket.socket(socket.AF_INET, # Internet��ַ��
                     socket.SOCK_DGRAM) # UDPЭ��

while 1:
    MESSAGE =  raw_input("������:") #һ��ֻ��һ������
    
    if MESSAGE == 'open':
     print "���ڴ���־����" 
     sock.sendto(MESSAGE,ip_address)
     sock.recv(1024)
        
    if MESSAGE == 'save':     
     print "��־�ѱ��桭��"
     
    else:
     sock.sendto(MESSAGE,ip_address)
     print "UDP target IP:", UDP_IP
     print "UDP target port:", UDP_PORT
     print "�ѷ�����Ϣ:", MESSAGE