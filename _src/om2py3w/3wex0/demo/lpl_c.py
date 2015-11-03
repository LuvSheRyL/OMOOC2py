#!/usr/bin/env python
#coding:utf-8

import socket,sys
reload(sys)
sys.setdefaultencoding('GB2312') #适用于win-cmd运行

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto("HANDSHAKE_54857", ('127.0.0.1', 1234))
print "你好，欢迎使用极简记事本。以下是历史日志："
print s.recv(1024)


while True:

    data = raw_input("今天想写点什么？")
    if data == 'quit':
        print "再见！"
        s.close()
        break
    elif data == "history":
        s.sendto(data, ('127.0.0.1', 1234))
        print s.recv(1024)
    else:
        s.sendto(data, ('127.0.0.1', 1234))