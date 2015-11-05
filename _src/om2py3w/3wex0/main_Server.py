# -*- coding: utf-8 -*-

import socket
import sys,codecs
import datetime
from chat import *

reload(sys)
sys.setdefaultencoding('GB2312') #������win-cmd����

UDP_IP = "127.0.0.1"
UDP_PORT = 9527


def ai_chat(data):
    chat = Chat()
    info = data
    chat.send(info)
    chat.init()
    chat.get()
    
    


    
def save(data,diary):
    now = datetime.datetime.now()
    otherStyleTime = now.strftime("%Y-%m-%d %H:%M:%S") #�ο���һ�ܴ���
    s = open(diary,'a')
    s.write(otherStyleTime+":"+data+ "\n")
    s.close()
    print "��־�ѱ�����%s" %diary

#�ο���һ�ܴ���    
def main():
    sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
    sock.bind(('', UDP_PORT))        #''��ʾ������������IP��ַ
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    diary =  addr[0] + ".txt"  #��IP��ַ.txt ��ʽ����,����diary_txt��Ϊȫ�ֱ���
    print "*** %s���ռǱ�--��������********\n" %addr[0]

    #if data == 'ai' or data == 'AI':
    ai_chat(data)
'''    
    if data=='r' or data=='R':
        print "Loading..."
        #open_diary(diary)
        o = open(diary,'r')
        content = o.read()
        #print type(content)
        sock.sendto(content,addr)
        o.close()
        print  "��־�ѷ�����%s" %addr[0]
    else:
        print "�Ѷ�:", data, "����-->", addr[0]
        save(data,diary)
        
'''        


while 1:
    main()



