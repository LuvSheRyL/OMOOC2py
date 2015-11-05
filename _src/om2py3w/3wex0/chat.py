#!/usr/bin/python
# -*- coding: utf8 -*-
# "http://www.oschina.net/code/snippet_1244912_45434"
  
import os
import json
import urllib2
  
  
class Chat(object):
    key = "d2b79c5d4352cfa18a5bf4c70f711f0a"    # turing123网站
    apiurl = "http://www.tuling123.com/openapi/api?"
  
    def init(self):
        os.system("cls") #windows cmd 清屏
<<<<<<< HEAD
        print u"尽情调教把!"
        print "--"*30
  
    def get(self):
        print "> ",
        info = raw_input()
        if info == 'q' or info == 'exit' or info == "quit":
            print "- Goodbye"
=======
        print u"哥哥~尽情调教把!"
        print "--"*30
  
    def get(self,info):   #增加info变量用于接收外部内容
        self.info = info  #声明
        print "> ",
        #info = raw_input()  关闭此命令，接收远端信息
        if info == 'q' or info == 'exit' or info == "quit":
            print "- Goodbye AI"
>>>>>>> 6f468913b017a98f5585e0aec53196fc0a0f7b6b
            return
        self.send(info)
  
    def send(self, info):
        url = self.apiurl + 'key=' + self.key + '&' + 'info=' + info
        re = urllib2.urlopen(url).read()
        re_dict = json.loads(re)
        text = re_dict['text']
        print '- ', text
<<<<<<< HEAD
        self.get()
  
  
if __name__ == "__main__":
    chat = Chat()
    chat.init()
    chat.get()
=======
        self.get(info)
  
'''
if __name__ == "__main__":
    chat = Chat()
    chat.init()
    chat.get()
'''
>>>>>>> 6f468913b017a98f5585e0aec53196fc0a0f7b6b
