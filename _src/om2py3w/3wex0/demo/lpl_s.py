#!/usr/bin/env python
#coding:utf-8
#Author:liangpeili

#导入socket模块和datetime模块
import socket
import datetime,sys
reload(sys)
sys.setdefaultencoding('GB2312') #适用于win-cmd运行


#定义函数，作用是把获取的内容添加到文件，并打时间标签。
def write(content,dairy):
    dairy_c=open(dairy,"a")
    now=datetime.datetime.now()
    curr=now.strftime("%Y-%m-%d %H:%M:%S")
    dairy_c.write(curr+":"+content+"\n")
    dairy_c.close()   

#定义函数，作用是读取用户的历史记录
def read(dairy):
    dairy_r=open(dairy,"a")
    content = dairy_r.read()
    dairy_r.close()
    return content 

#创建一个socket对象
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#绑定端口
s.bind(('',1234))

print 'Bind UDP on 1234...'
while True:
    #接收数据
    data, addr = s.recvfrom(1024)
    print "Received from %s:%s" %addr
    dairy = "%s.txt" % addr[0]
    # 返回历史记录给用户
    if data == 'history' or data == 'HANDSHAKE_54857':
        data1 = read(dairy)
        s.sendto(data1, addr)
    #如果不是history，就把用户的输入记录到文件
    else:
        write(data,dairy)