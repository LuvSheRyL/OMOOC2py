# -*- coding: utf-8 -*-

'''A simple sentence to describe the function of this module.

Add detailed description here if need.

Eample:
    # python ./sample.py -t
    # ...
'''
# 导入Tk GUI模块
from Tkinter import *
from ScrolledText import *
import tkMessageBox
from tkFileDialog import *
import fileinput
import time

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

t1 = []
root=None

# Add your code here
# Delete the description when you start coding.


              
  
class diary(Frame):

 def __init__(self,rt):
 
    if rt == None:
        self.t=Tk()    #创建顶层窗口t
    else:
        self.t=Toplevel(rt) #使用toplevel窗口模式
    self.t.title("窗口- %d"%len(t1))
    Frame.__init__(self,rt)
    self.pack(fill=BOTH, expand=1)

    
    self.open = Button(self)
    self.open["text"] = "打开文件"
    self.open["fg"] = "Blue"
    self.open["command"] = self.diary_open
    self.open.pack({"side":"left"})
   
    self.save = Button(self)
    self.save["text"] = "保存"
    self.save["fg"] = "green"
    self.save["command"] = self.savefile
    self.save.pack({"side":"left"})
    
    self.quit = Button(self)
    self.quit["text"] = "关闭"
    self.quit["fg"] = "red"
    self.quit["command"] = self.close
    self.quit.pack({"side":"bottom"})
    
    self.f=Frame(self,width=512)
    self.f.pack(expand=1,fill=BOTH)
   
    self.st=ScrolledText(self.f,background="white")
    self.st.pack(side=LEFT,fill=BOTH,expand=1)

#定义打开文件函数    
 def diary_open(self):
    p1=END
    oname=askopenfilename(filetypes=[("file","*.txt*")])
    if oname:
        for line in fileinput.input(oname):
         self.st.insert(p1,line)
    self.t.title(oname)
 
 def savefile(self):
  sname=asksaveasfilename()
  if sname:
   ofp=open(sname,"w")
   ofp.write(self.st.get(1.0,END))
   ofp.flush()  #刷新
   ofp.close()
   self.t.title(sname + u"已保存")
  
 def close(self):
  self.t.destroy() #注意此处销毁当前窗口
  print "close"

 
 def about():
    tkMessageBox.showinfo("小小记事本","V1.0\n"
  "创建于2015年10月26日\n"
  "作者：robo_one")

  
  
def neweditor():
 global root
 t1.append(diary(root))
  
if __name__=="__main__":
 root=None
 t1.append(diary(root))
 root=t1[0].t
root.mainloop()
