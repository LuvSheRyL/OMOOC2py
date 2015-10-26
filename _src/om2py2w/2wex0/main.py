# -*- coding: utf-8 -*-

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

    '''定义按钮'''
    '''Possible values are specified as compass directions:
    "n" (north, or top edge), "ne", (north-east, or top right corner), 
    "e", "se", "s", "sw", "w", "nw" or "center".
    Layout布局
    pack side :It can be top, bottom, left and right. The default is top
    color: color names (e.g. "red") or hex RGB codes (e.g. "#ff340a").
    anchor :Pack widget will be anchored to specific side if the width is less than space is assigned. The valid edges are n,e,w,s(东西南北)
    '''

    self.open = Button(self)
    self.open["text"] = "打开文件"
    self.open["fg"] = "Blue"
    self.open["command"] = self.diary_open_txt
    self.open.pack({"side":"left"})
    self.open.pack({"anchor":"n"})
   
    self.save = Button(self)
    self.save["text"] = "保存"
    self.save["fg"] = "#0fff0a" 
    self.save["command"] = self.savefile
    self.save.pack({"side":"left"})
    self.save.pack({"anchor":"n"})
    
    self.quit = Button(self)
    self.quit["text"] = "关闭"
    self.quit["fg"] = "red"
    self.quit["command"] = self.close
    self.quit.pack({"side":"left"})
    self.quit.pack({"anchor":"n"})

    self.guan_yu = Button(self)
    self.guan_yu["text"] = "关于"
    self.guan_yu["fg"] = "red"
    self.guan_yu["command"] = self.about1
    self.guan_yu.pack({"side":"left"})
    self.guan_yu.pack({"anchor":"s"})
    
    
    
    self.f=Frame(self,width=512)
    self.f.pack(expand=1,fill=BOTH)
   
    self.st=ScrolledText(self.f,background="white")
    self.st.pack(side=LEFT,fill=BOTH,expand=1)

#定义打开文件函数    
 def diary_open_txt(self):
    p1=END
    oname=askopenfilename(filetypes=[("文本文件","*.txt*")])
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

 def about1(self):
  tkMessageBox.showinfo("小小记事本","V1.0\n"
  "创建于2015年10月26日\n"
  "作者：robo_one")
  print u"关于"

  
  
def neweditor():
 global root
 t1.append(diary(root))
  
if __name__=="__main__":
 root=None
 t1.append(diary(root))
 root=t1[0].t
root.mainloop()
