# -*- coding: utf-8 -*-
# �ռǱ��ͻ���,CMD����Python C.PY 

import socket
import sys,codecs
reload(sys)
sys.setdefaultencoding('UTF-8') #��CMD�����б���ΪGB2312����Python��Ӧ�޸�ΪUTF-8

UDP_IP = "localhost"
UDP_PORT = 8080
ip_address = (UDP_IP,UDP_PORT)


def main():
    sock = socket.socket(socket.AF_INET, # Internet��ַ��
                     socket.SOCK_DGRAM) # UDPЭ��
                     
    print '''
    ��ӭ����*** %s���ռǱ�--********
    ���롮r��---������ʷ��¼
    
    '''%UDP_IP
    MESSAGE =  raw_input("д��ʲô��:") #һ��ֻ��һ������
    
    if MESSAGE == 'r':
        print "���ڴ���־����" 
        sock.sendto(MESSAGE,ip_address)
        print sock.recv(1024)
   
    else:
     sock.sendto(MESSAGE,ip_address)
     print "UDP target IP:", UDP_IP
     print "UDP target port:", UDP_PORT
     print "�ѷ�����Ϣ:", MESSAGE
                     
if __name__ == '__main__':
    main()