# 日记本
+ 一次接收输入一行日记
+ 保存为本地文件
+ 再次运行系统时,能打印出过往的所有日记


----------


>file命令使用参考：[python files io](http://www.tutorialspoint.com/python/python_files_io.htm)

>read,write命令使用参考：[LPTHW-ex20](http://old.sebug.net/paper/books/LearnPythonTheHardWay/ex20.html)

>调用系统时间命令参考：[python操作日期和时间的方法](http://www.jb51.net/article/47957.htm)

>中文编码调用参考：[中文编码调用](http://ju.outofmemory.cn/entry/26092)

>Python程序输出到文件中：[Python程序输出到文件中](http://www.cnblogs.com/sysuoyj/archive/2012/03/14/2395868.html)

## 载入外部命令
'from sys import argv
script , input_file = argv'


## 读取文件

'current_file = open(input_file, 'a')'
'diary_read = open(input_file,'r')
		print "Loading..."
		print diary_read.read()
		diary_read.close()
'
