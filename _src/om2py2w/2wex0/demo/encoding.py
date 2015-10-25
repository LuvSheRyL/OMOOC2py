#!/usr/bin/env python
#-*- encoding:utf-8 -*-

# 读取utf-8编码格式的文本文件        
# 这里Python解释器读取的是utf-8编码的字节流,然后再按指定的编码方式解释这些字节流
# 这样就比较好理解乱码的原因


#coding=utf-8                 
# When Python reads the encoding it tries to interpret the file as utf-8        
# 告诉Python解释器编译时采用哪种编码方式
# 如未设置编码方式,且解释器可识别文件(如utf-8编码格式的文件有的(与编辑器有关)带有BOM,可供解释器识别)编码方式则采用文件编码方式,反之采用终端默认编码方式


import sys
# reload(sys)
# 指定终端默认编码方式
# sys.setdefaultencoding('utf8')
# 获取终端默认编码方式
# sys.getdefaultencoding()


import codecs
def ConvertCN(s):
	if s[:3] == codecs.BOM_UTF8:
		s = s[3:]

	# 若系统默认编码方式为acsii且未修改默认编码方式        
	# s.encode('gbk')：s(文件编码格式)--(.decode('ascii'))-->unicode--(.encode('gbk'))-->s(gbk编码格式) （这个过程由终端完成，未指定编码方式时将采用终端默认编码方式）
	# 兼容关系：ASCII --> ISO-8859-1 --> UNICODE(UTF-8,UTF-16,UTF-32) --> UCS(UCS2[与UNICODE兼容],UCS4), ASCII --> GB2312 --> GBK --> GB18030
	# 因utf-8向下兼容ascii ascii不向上兼容utf-8,对此处s(utf-8编码格式)进行ascii解码成unicode时可能发生错误
	return s.decode('utf-8')


def PrintFile(filename):
         f = file(filename,'r')
         for f_line in f.readlines():
                  print ConvertCN(f_line)
         f.close()

if __name__ == "__main__":
                
         print "OperCodingFile.txt"
                
         # Python输出的是字节流 打印由终端处理
         # print 在终端显示如何是由终端决定的
         """
         它大致讲解下python中的print原理：        
         When Python executes a print statement,        
         it simply passes the output to the operating system (using fwrite() or something like it),        
         and some other program is responsible for actually displaying that output on the screen.        
         For example, on Windows, it might be the Windows console subsystem that displays the result.        
         Or if you're using Windows and running Python on a Unix box somewhere else,        
         your Windows SSH client is actually responsible for displaying the data.        
         If you are running Python in an xterm on Unix, then xterm and your X server handle the display.        
         To print data reliably, you must know the encoding that this display program expects.        
         简单地说，python中的print直接把字符串传递给操作系统，所以你需要把str解码成与操作系统一致的格式。
         Windows使用CP936(几乎与gbk相同)，所以这里可以使用gbk。
         """
                
         print ConvertCN("\n****** 按任意键退出！*******")         
                
         sys.stdin.readline()