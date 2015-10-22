# 日记本

----------
基本需求

+ 一次接收输入一行日记
+ 保存为本地文件
+ 再次运行系统时,能打印出过往的所有日记

----------
补充需求

+ 如何令 _src/om2py0w/0wex1/main.py 可以一直运行,等待我们的输入?
+ 或是接受其它命令?
+ 怎么退出脚本?

----------
再补充

+ 先不管数据结构, 就原样保存到文件(比如txt格式的)中吧!
+ 文本怎么实现换行?
+ 是否要加日期?
+ 中文用什么编码?

----------
Over

+ 那么,最后一个功能就能串联起来成为一个 mini 软件了!
+ 每次运行 _src/om2py0w/0wex1/main.py 时
+ 怎么自动将过往的日志都打印出来?
+ 细节:
	- 如何找到日志文件?
	- 如何打开日志文件?
	- 如何读取文件内容?
	- 如何输出日志?
	- ...
	- 中文输出 OK 嘛?


----------
背景

+ Win 7 32位
+ Python 2.7
+ 环境变量已添加Python
+ Notepad++文件→打开所在文件夹→命令行执行
+ 命令行输入：main.py diary.txt

##参考链接

>file命令使用参考：[python files io](http://www.tutorialspoint.com/python/python_files_io.htm)

>read,write命令使用参考：[LPTHW-ex20](http://old.sebug.net/paper/books/LearnPythonTheHardWay/ex20.html)

>调用系统时间命令参考：[python操作日期和时间的方法](http://www.jb51.net/article/47957.htm)

>中文编码调用参考：[中文编码调用](http://ju.outofmemory.cn/entry/26092)

>Python程序输出到文件中：[Python程序输出到文件中](http://www.cnblogs.com/sysuoyj/archive/2012/03/14/2395868.html)

>[一张图看懂Python](http://www.pythontab.com/statics/js/ueditor/php/upload1/20150422/14296978024588.png)

##思路
既然是记事本的功能，抽丝拨茧，先做最简单的需求功能，再逐步完善优化。

主程序执行，文本提示操作

如果命令为下述之一，即执行，否则报错提示。

w命令判断→打开文件→写文本→关闭

r命令判断→打开文件→读文本→关闭

返回主程序，循环。

## 载入外部命令
    from sys import argv
	script , input_file = argv
## 读取当前时间
	import datetime
	now = datetime.datetime.now()
	otherStyleTime = now.strftime("%Y-%m-%d %H:%M:%S")



读取时间的方法有很多种，具体可参考上面的链接。
本程序选其中之一，并以特定格式内容输出。

## 读取文件

    current_file = open(input_file, 'a')
	diary_read = open(input_file,'r')
		print "Loading..."
		print diary_read.read()
		diary_read.close()

### 读函数 方法二
	
    #read diary
	#def diary_read(f):
	#	print "Your file %r:" % input_file
	#	f.seek(0,0)
	#	print current_file.read()
	#	current_file.close()

该函数在被调用时有些问题，目前被我屏蔽中。。。

## 写文件
    def diary_write(f):
		line = raw_input("-->")
		current_file.write("--- %r --- \n" % otherStyleTime)
		current_file.write(line)
		current_file.write("\n")
	
		print "Save,we'll close it **** "
		current_file.close()

容易忽略的问题
 
+ 函数的结尾记住要加： ` def diary_write(f):`
+ otherStyleTime命令的调用必须先定义它 

## 主函数
    def diary_main():
	current_file = open(input_file, 'a')
	print "***Press 'w' or 'W' write diary.********\n"
	print "***Press 'r' or 'R' read all diary.*****\n"
	a = raw_input("W OR R?")
	if a=='w' or a=='W':
		diary_write(current_file)
	elif a=='r' or a=='R':
		diary_read = open(input_file,'r')
		print "Loading..."
		print diary_read.read()
		diary_read.close()
	else:
		print "Error,plz input w or r?"
		
## 循环执行
    while 1:
		diary_main()


##运行效果
![](http://i11.tietuku.com/f49e0ba7a9a5e792.jpg)

![](http://i11.tietuku.com/499b936f35e87678.jpg)

![](http://i11.tietuku.com/d3d190852f12298a.jpg)

![](http://i11.tietuku.com/c8ae5818a07394b4.jpg)

## BUG
+ 在不退出程序的前提下， 再次运行w，写日记， 程序报错。。。~~~~(>_<)~~~~ 
+ 日期的‘   ’如何消除掉。。。

![](http://i11.tietuku.com/5680fd4224cf054b.jpg)

## 迭代第一次

感谢[faketooth](https://github.com/faketooth)建议
	
+ 	`current_file.write("--- %r --- \n" % otherStyleTime)`
修改成`current_file.write("--- %s --- \n" % otherStyleTime)` 仅输出字符串信息。
+	检查代码中.close的位置，每OPEN一次后就要求close()一次。

###BUG 2

1. 时间调用模块，只在第一次main.py执行时候有效
2. 无论后续多少循环都无法载入当前时间；

![](http://i11.tietuku.com/15e593aefcdeec81.jpg)

修改diary_write函数，调整时间调用语句至diary_write函数中

	`def diary_write(f):
	now = datetime.datetime.now()
	otherStyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
	current_file = open(input_file, 'a+')
	line = raw_input("-->")
	current_file.write("--- %s --- \n" % otherStyleTime)
	current_file.write(line)
	current_file.write("\n")
	print "Save,we'll save it **** "
	current_file.close()`

所以bug解决之。。
<<<<<<< HEAD
![](http://i11.tietuku.com/68c362feb5f597c1.jpg)
=======

![](http://i11.tietuku.com/68c362feb5f597c1.jpg)

## 优秀作品分享
   [交互日记系统](https://wp-lai.gitbooks.io/learn-python/content/2nDev/diary.html#代码)
