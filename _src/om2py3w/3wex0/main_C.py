# -*- coding: utf-8 -*-
import socket
import sys,codecs
reload(sys)
sys.setdefaultencoding('GB2312') #��CMD�����б���ΪGB2312����Python��Ӧ�޸�ΪUTF-8

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
MESSAGE =  raw_input("Plz input:") #һ��ֻ��һ������

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "�ѷ�����Ϣ:", MESSAGE

sock = socket.socket(socket.AF_INET, # Internet��ַ��
                     socket.SOCK_DGRAM) # UDPЭ��
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
sock.close() #�Ͽ�����