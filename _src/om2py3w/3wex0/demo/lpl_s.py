#!/usr/bin/env python
#coding:utf-8
#Author:liangpeili

#����socketģ���datetimeģ��
import socket
import datetime,sys
reload(sys)
sys.setdefaultencoding('GB2312') #������win-cmd����


#���庯���������ǰѻ�ȡ��������ӵ��ļ�������ʱ���ǩ��
def write(content,dairy):
    dairy_c=open(dairy,"a")
    now=datetime.datetime.now()
    curr=now.strftime("%Y-%m-%d %H:%M:%S")
    dairy_c.write(curr+":"+content+"\n")
    dairy_c.close()   

#���庯���������Ƕ�ȡ�û�����ʷ��¼
def read(dairy):
    dairy_r=open(dairy,"a")
    content = dairy_r.read()
    dairy_r.close()
    return content 

#����һ��socket����
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#�󶨶˿�
s.bind(('',1234))

print 'Bind UDP on 1234...'
while True:
    #��������
    data, addr = s.recvfrom(1024)
    print "Received from %s:%s" %addr
    dairy = "%s.txt" % addr[0]
    # ������ʷ��¼���û�
    if data == 'history' or data == 'HANDSHAKE_54857':
        data1 = read(dairy)
        s.sendto(data1, addr)
    #�������history���Ͱ��û��������¼���ļ�
    else:
        write(data,dairy)