#!/usr/bin/env python
#coding:utf-8

import socket,sys
reload(sys)
sys.setdefaultencoding('GB2312') #������win-cmd����

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto("HANDSHAKE_54857", ('127.0.0.1', 1234))
print "��ã���ӭʹ�ü�����±�����������ʷ��־��"
print s.recv(1024)


while True:

    data = raw_input("������д��ʲô��")
    if data == 'quit':
        print "�ټ���"
        s.close()
        break
    elif data == "history":
        s.sendto(data, ('127.0.0.1', 1234))
        print s.recv(1024)
    else:
        s.sendto(data, ('127.0.0.1', 1234))