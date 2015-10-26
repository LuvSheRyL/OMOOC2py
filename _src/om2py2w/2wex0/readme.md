# GUI 日记本

> [Tkinter什么鬼](https://docs.python.org/2.7/library/tkinter.html?highlight=tkinter)

> [《Practical Programming in Tcl and Tk》](http://www.beedub.com/book/ "Practical Programming in Tcl and Tk")
> [关于Tk中pack的理解](http://my.oschina.net/annieduoduo/blog/71400) 
> 
> + 其实就是一个自适应的窗口容器
> + [TkDocs-最全资料](http://www.tkdocs.com/tutorial/index.html "TkDocs")
>
> [Tkinter pack_layout布局案例](http://my.oschina.net/ScottYang/blog/57192 "Tkinter pack_layout")
> 
> [Python Tkinter Frame](http://www.tutorialspoint.com/python/tk_frame.htm "Python Tkinter Frame")
> 
> [Layout management in Tkinter](http://zetcode.com/gui/tkinter/layout/ "Layout management in Tkinter")
> 
> [An Introduction to Tkinter (Work in Progress)](http://effbot.org/tkinterbook/)
> 
> [The Tkinter Scrollbar Widget](http://effbot.org/tkinterbook/scrollbar.htm )
	 
> + **get()** Gets the current slider position.Offset 0.0 means that the slider is in its topmost (or leftmost) position, and offset 1.0 means that it is in its bottommost (or rightmost) position.

## V1.0 基本功能实现
+ 打开文件
+ 保存文件
+ 关闭窗口
+ 关于（messagebox实现）

代码是参考一个小例子修改过来的，它是用menu执行，我修改为按钮的方式，
参考案例Menu方式实现效果
![](http://i11.tietuku.com/107950c226186fed.jpg)
我修改后的实现效果，界面粗暴，权当学习。
![](http://i11.tietuku.com/fc474516d6ac8840.jpg)
附V1.0 我的源代码
```
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
      self.t=Tk()    #创建顶层窗口t（master）
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

```
## V1.0 BUG
+ 新窗口中输入中文字符→保存为新文件.txt→再次打开该文件，正常
+ 直接打开其他中文字符的文件，输出乱码。
 - 参考[Python字符编码详解](http://www.cnblogs.com/huxi/archive/2010/12/05/1897271.html)
 - [官方资料Standard Encodings](https://docs.python.org/2/library/codecs.html#standard-encodings)
