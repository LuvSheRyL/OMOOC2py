# 平台搭建


[Windows OpenCV 2.3.1/Opencv2.4.6 + Python 2.7配置
](http://blog.csdn.net/mengyafei43/article/details/10338531)

下载 OpenCV 2.3.1 。文中下载了OpenCV-2.3.1-win-superpack (大概124MB,解压后1G多)。他不需编译，使用方便 [下载地址](http://nchc.dl.sourceforge.net/project/opencvlibrary/opencv-win/2.3.1/OpenCV-2.3.1-win-superpack.exe)

2. OpenCV-2.3.1-win-superpack.exe是自解压文件，直接运行。即可解压。默认解压到opencv文件夹里。
3.下载numpy。opencv的python版需要该模块。下载页面在这里 注意，下载和Python版本一致的numpy。
文中下载的是[numpy-1.6.1-win32-superpack-pythonxe](http://nchc.dl.sourceforge.net/project/numpy/NumPy/1.6.1/numpy-1.6.1-win32-superpack-python2.7.exe) 5.82M
4.运行numpy-1.6.1-win32-superpack-python2.7.exe
5.安装python2.7，默认安装在C:\Python27

好了，配置
opencv文件夹中，build->python->2.7 复制2.7下面的所有文件 到C:\Python27\Lib\site-packages 中
测试
打开opencv文件夹中的samples\python
双击drawing.py 如果没有问题应该看到彩色条纹。
注意 这里的其他样例 有可能一闪而过，什么都不显示。一种原因是哪个脚本需要参数，另一种是脚本中写图片文件路径错误，还有一种是urllib的问题，打开代码看看，应该比较容易理解。

致谢：本文参考了“windows下OpenCV 2.3.1 + Python 2.6 / 2.7配置 - 书记@学习笔记 - 博客频道 - CSDN.NET
http://blog.csdn.net/bh20077/article/details/6946046” ，可以说仅对原文稍微做了修改。
刚开始弄的时候，装了个python3.4,版本太高，opencv release的只有2.6和2.7的版本，按常理说应该可以兼容，但是python3和2+的语法有差异，索性都换成python2.7吧。版本高级，对自己好像也没有什么用。

**注意：**

1. 因为电脑之前安装过Anaconda，在运行第四步时候numpy默认至`C:\Anaconda\Lib\site-packages`
2. 从`C:\Anaconda\Lib\site-packages`找到numpy文件完整复制到`C:\Python27\Lib\site-packages`即可
3. python环境中`import numpy`无报错，ok~


