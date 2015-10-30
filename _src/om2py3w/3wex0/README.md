# 网络版日志
## 功能

  需求如下:

+ 每次运行时合理的打印出过往的所有笔记
+ 一次接收输入一行笔记
+ 在服务端保存为文件:
+ 在所有访问的客户端可以获得历史笔记
+ 支持多个客户端同时进行笔记记录

备选的:

+ 如果有余力!-)
+ 请尝试思考,是否能保存笔记的客户端来源?
+ 并在合适的情景中输出?
+ 进一步的,能根据客户端不同,要求输出不同客户端提交的笔记嘛

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





参考资料
> [Python Udp Communication](https://wiki.python.org/moin/UdpCommunication)
> 
> [Python_socket](https://docs.python.org/2.7/library/socket.html)
> 
> [《Python socket编程_haodi_新浪博客》](http://blog.sina.com.cn/s/blog_523491650100hikg.html)