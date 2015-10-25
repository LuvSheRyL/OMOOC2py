# 杭州Py C2T2面基总结

>	2015年10月25日 @Allface
>	haidao **助教**
>	小赖
>	robo_one
>	ted
> 	感谢ted提供录音，链接: [2wd0C2T2Hangzhou.MP3](https://www.fangcloud.com/share/c0453bf794c861235a7dc43a71) 密码: openmind
    
## 关于中文编码

+ 背景
	+ Win 7 32位系统
	+ Notepad++ 作为代码编辑器
	+ CMD.exe作为py运行平台
+ 问题
	+ 代码中存在中文的情况下，CMD平台输出乱码
		+ 如图
		+ ![](http://i13.tietuku.com/fe63c8a19c05cf37.jpg)
+ 解释
	+ `# _*_ coding: utf-8 _*_` 语句用于文件声明需要该文件使用的为utf-8格式
	+ `print "2015年10月25日"` print语句是要将输出的内容传送给操作系统，操作系统会根据系统的编码对输入字节进行编码。此处print语句中的中文使用的是utf-8编码的字符串流，但是win cmd.exe使用的是GBK中文解码，这些经过utf-8解码后形成utf-8格式字符串流再经过CMD的GBK解释一番，所对应的就是`2015骞?0鏈?5鏃`。
	+ 因此，为了让cmd输出显示正常，需要将其`print "2015年10月25日"` 中的`“2015年10月25日”`转换成系统统一编码，比如`print u"2015年10月25日"`，其中u表示unicode编码，（而不是将`2015年10月25日`通过声明处的utf-8编码）
	+ 经过unicode编码解释过后的`2015年10月25日`字符串，在各系统内部会将该unicode对象字符串按照本地默认编码解释并输出。
	+ 演示如下
	![](http://i11.tietuku.com/d0ea6b1910bf5eab.jpg)
    + 备注：Python默认编码为ASCII码，CMD默认为GBK编码，记事本为GB2312编码
    	+ ![](http://i11.tietuku.com/bd26a886ced44baa.jpg)
    	+ 如上图`print u"2015年10月25日"`中文以经过unicode编码输出，并通过系统CMD的GBK文件解释，输出正常。`b = 'b 二〇一五年十月二十五日'`中文以utf-8格式编码，再通过系统CMD-gbk解码，自然错乱。如上图中`a_utf_8 = a.encode('utf-8')`语句的编码从Unicode→UTF-8→GBK(CMD编码)的转换，因此出现乱码。
    	+ 修改`a_utf_8 = a.encode('utf-8')`为`a_utf_8 = a.encode('GBK')`即可解决
    	+ ![](http://i11.tietuku.com/715646d5b26b03d2.jpg)

+ 小结
	+ 学会定位问题
		+ 一次先解决一个问题
		+ 逐个关闭
	+ 学会拆解问题
	+ 学会关键词的问题检索，多试试不同关键词

## 关于GIt分支

+ git checkout使用
+ github中new pull request的分支合并

## 关于Python QT与TK
+ tk适用于做些小工具
+ Qt偏向产品开发


## 关于ipython Notebook 新玩法

+ Win环境中可在目标目录下右键直接Git here
+ 然后再git bash环境中`ipython notebook`启动
+ 使用ipython notebook编写作者思维的blog文件
+ ![](http://i13.tietuku.com/43a296b854e9a54a.jpg)
+ ![](http://i13.tietuku.com/37201b6530d85770.jpg)

## 关于日记本第二周的开发建议
+ 核心功能与其他功能独立，避免函数的耦合，保持核心函数的独立性
+ 尝试掌握tk调用系统程序接口进行不同文件格式的执行

# 总结
+ 感谢助教、各位新朋友的无私分享，虽然不是科班出身，但是每人都是非常努力，学习编程：任何时候都不会晚！
+ 带着问题去讨论，面基前仔细梳理自己遇到的问题，减少沟通上的成本
+ 从0到1的接触Python过程中，一定让自己进入心里状态，沉浸进去，不要怕麻烦觉得搜索了很多冷门的知识点，这都是未来的福音
+ 未完待续
