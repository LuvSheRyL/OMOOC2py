# 网络版日志

## 功能

### 需求如下:

+ 每次运行时合理的打印出过往的所有笔记
+ 一次接收输入一行笔记
+ 在服务端保存为文件:
+ 在所有访问的客户端可以获得历史笔记
+ 支持多个客户端同时进行笔记记录

#### 备选的:

+ 如果有余力!-)
+ 请尝试思考,是否能保存笔记的客户端来源?
+ 并在合适的情景中输出?
+ 进一步的,能根据客户端不同,要求输出不同客户端提交的笔记嘛


_ _ _

+ 首先先明确如何进行网络开发?
+ 什么是 UDP 协议?
+ 用 Python 完成一对最简单的 DUP 服务器/客户端



OK 各个击破，==什么是网络编程开发？==
网络编程开发就得开始解释Python中的socket库，具体用法可参考官方doc,官方解释：
	
	socket DESCRIPTION
    This module provides socket operations and some related functions.
    On Unix, it supports IP (Internet Protocol) and Unix domain sockets.
    On other systems, it only supports IP. Functions specific for a
    socket are available as methods of the socket object.

好比在我们打电话，对方号码就是IP地址，分机号就是端口port，socket就是电话交换机的功能了。==**每对**==socket必须包括源端IP/PORT，目的端IP/PORT.
当我们（客户端1）要给一个妹子(客户端2)的打电话时，我们需要请求服务器（妹纸她妈）上的--socket(),
用法如下：==socket.socket()== , 联系上她妈这条线有两种方式，一种通过TCP（Transmission Control Protocol 传输控制协议）协议，一种通过UDP(User Datagram Protocol用户数据报协议)协议。

	

	|  socket([family[, type[, proto]]]) -> socket object
	|
	|  Open a socket of the given type.  The family argument specifies the
	|  address family; it defaults to AF_INET.  The type argument specifies
	|  whether this is a stream (SOCK_STREAM, this is the default)
	|  or datagram (SOCK_DGRAM) socket.  The protocol argument defaults to 0,
	|  specifying the default protocol.  Keyword arguments are accepted.
	|
	|  A socket object represents one endpoint of a network connection.

且先不管这协议细节，只要记住TCP比UDP传输靠谱，少量信息时UDP比TCP快，但是容易丢信息。具体差异参考[TCP/IP协议与UDP协议的区别](http://zhangjiangxing-gmail-com.iteye.com/blog/646880)

OK，回到我们[Python socket.socket()](https://docs.python.org/2.7/library/socket.html)环境中，仅需了解`socket.SOCK_STREAM`为TCP协议，`socket.SOCK_DGRAM`为UDP协议


### 客户端使用 

在Python中用法，库调用

```
	import socket
	s = socket.socket(socket.PF_INET, socket.SOCK_DGRAM)

```

搭好线后，开始“告知”她妈妈，自己的IP,PORT（电话号码，分机号）（端口(分机号)范围为0-65535”，但是公认端口建议不要选择，系统自己的，你懂的~
 - 公认的Port：0～1023
 - 注册的Port：1024～49151 
 - 动态的Port：49 152～65535

例如
```
	s.bind(("127.0.0.1", 5005))

```
当然你可以选择不这么做，让系统进程自动给你“分配”随机闲置的端口，及其根据该端口选择的源IP`s.bind(('', 0))`  参考[《 客户端 用不用 bind 的区别》](http://blog.chinaunix.net/uid-23193900-id-3199173.html)

准备工作完成后，开始“拨号”妹纸……的……她妈了（server）~~
```
	s.connect(("127.0.0.1", 5005))   #方便测试用本地主机地址

```
说些啥呢……

```
MESSAGE =  u"Hey Girl"    # 小伙子，你找shi呢~
s.sendto(MESSAGE, ("127.0.0.1", 5005)) # 表示她妈号码
```

勇气可嘉，你可以挂电话了~
```
s.close()
```
至此，小伙子这边的事情完成，剩下的看她妈的了~

### 服务器端使用
在新建一个Python文件作为服务器端
```
	import socket
	UDP_IP = "127.0.0.1"
	UDP_PORT = 5005

	sock = socket.socket(socket.AF_INET, # Internet，
                     socket.SOCK_DGRAM) # UDP协议
	sock.bind((UDP_IP, UDP_PORT))
	#AF_INET表示address family地址族,兼容IPv4,IPv6地址
	while True:
     data, addr = sock.recvfrom(1024) # 默认buffer size is 1024 bytes
     print "received message:", data  #完成这条命令后，小伙子心情一定是复杂的

```

## Version 1.0 连接

效果图
![](http://i13.tietuku.com/fa76b6ae8a200ba7.jpg)

1. 先运行服务器程序`Python main_server.py`
2. 再运行客户端程序`Python main_c.py`
3. 在客户端输入消息，回车发送

'''客户端代码
    
    # -*- coding: utf-8 -*-
    import socket
    import sys,codecs
    reload(sys)
    sys.setdefaultencoding('GB2312') #在CMD中运行编码为GB2312，在Python中应修改为UTF-8

    UDP_IP = "127.0.0.1"
    UDP_PORT = 5005
    MESSAGE =  raw_input("Plz input:")

    print "UDP target IP:", UDP_IP
    print "UDP target port:", UDP_PORT
    print "已发送信息:", MESSAGE

    sock = socket.socket(socket.AF_INET, # Internet地址族
                         socket.SOCK_DGRAM) # UDP协议
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
    sock.close()

'''
'''服务器端代码
    
    
    # -*- coding: utf-8 -*-
    import socket
    import sys,codecs
    reload(sys)
    sys.setdefaultencoding('GB2312')

    UDP_IP = "127.0.0.1"
    UDP_PORT = 5005

    def server_con():
        sock = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP
        sock.bind((UDP_IP, UDP_PORT))
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        print "已接收信息:", data, "来自", addr


    while True:
        server_con()

        


'''


## Version 2.0 

![](http://i12.tietuku.com/7b96d07691098890.png)

### 客户端代码
    # -*- coding: utf-8 -*-
    import socket
    import sys,codecs
    reload(sys)
    sys.setdefaultencoding('GB2312') #在CMD中运行编码为GB2312，在Python中应修改为UTF-8

    UDP_IP = "127.0.0.1"
    UDP_PORT = 9527
    ip_address = (UDP_IP,UDP_PORT)


    def main():
        sock = socket.socket(socket.AF_INET, # Internet地址族
                         socket.SOCK_DGRAM) # UDP协议
                         
        print '''
        欢迎来到*** %s的日记本--********
        输入‘r’---载入历史记录
        
        '''%UDP_IP
        MESSAGE =  raw_input("写点什么呢:") #一次只能一行内容
        
        if MESSAGE == 'r':
            print "正在打开日志……" 
            sock.sendto(MESSAGE,ip_address)
            print sock.recv(1024)
       
        else:
         sock.sendto(MESSAGE,ip_address)
         print "UDP target IP:", UDP_IP
         print "UDP target port:", UDP_PORT
         print "已发送信息:", MESSAGE
                         
    while 1:
        main()
		
		
### 使用说明

1. 先启动server端文件，等待
2. 启动客户端py文件，并输入信息
3. 输入r可读取历史记录

* * *
### 服务器端代码
    # -*- coding: utf-8 -*-

    import socket
    import sys,codecs
    import datetime

    reload(sys)
    sys.setdefaultencoding('GB2312') #适用于win-cmd运行

    UDP_IP = "127.0.0.1"
    UDP_PORT = 9527


    #def open_diary(diary):    


        
    def save(data,diary):
        now = datetime.datetime.now()
        otherStyleTime = now.strftime("%Y-%m-%d %H:%M:%S") #参考第一周代码
        s = open(diary,'a')
        s.write(otherStyleTime+":"+data+ "\n")
        s.close()
        print "日志已保存至%s" %diary

    #参考第一周代码    
    def main():
        sock = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP
        sock.bind(('', UDP_PORT))        #''表示接收域内所以IP地址
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        diary =  addr[0] + ".txt"  #以IP地址.txt 格式保存,并将diary_txt作为全局变量
        print "*** %s的日记本--服务器端********\n" %addr[0]


        
        if data=='r' or data=='R':
            print "Loading..."
            #open_diary(diary)
            o = open(diary,'r')
            content = o.read()
            #print type(content)
            sock.sendto(content,addr)
            o.close()
            print  "日志已发送至%s" %addr[0]
        else:
            print "已读:", data, "来自-->", addr[0]
            save(data,diary)


    while 1:
        main()




## Version 3.0 将日志修改为机器人聊天工具

代码完善中

----------

## 知识点
1. Socket.listen
  + listen里有个参数backlog是指定tcpsever可以同时接受多少个客服端的连接申请，当超过此数时server将拒绝客户端的连接申请，给出socket.error: [Errno 10061]错误。
	
    socket.socket.listen = listen(...) unbound socket._socketobject method
    listen(backlog)
	Enable a server to accept connections.  The backlog argument must be at
	least 0 (if it is lower, it is set to 0); it specifies the number of
	unaccepted connections that the system will allow before refusing new
	connections.

	backlog指定最多允许多少个客户连接到服务器。它的值至少为1。收到连接请求后，这些请求需要排队，如果队列满，就拒绝请求。
	
	backlog应该理解为阻塞队列的长度，总共与服务器连接的客户端一共有 backlog + 1 个。阻塞队列FIFO，当连接客户端结束后阻塞队列里的第一个客服端与服务器连接成功。

2. 外部Python文件class调用





参考资料
> [Python Udp Communication](https://wiki.python.org/moin/UdpCommunication)
> 
> [Python_socket](https://docs.python.org/2.7/library/socket.html)
> 
> [《Python socket编程_haodi_新浪博客》](http://blog.sina.com.cn/s/blog_523491650100hikg.html)

> [Socket Programming HOWTO](https://docs.python.org/2/howto/sockets.html)
> 
> [机器人API接入](http://www.tuling123.com/html/doc/api.html#jiekou)