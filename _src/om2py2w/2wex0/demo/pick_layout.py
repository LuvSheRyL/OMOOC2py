#-*- coding:UTF-8 -*-
__author__ = 'Torxie'
 
import Tkinter
from Tkinter import *
 
class MainFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
 
    def initUI(self):
        self.parent.title('Test_FrameSize')
        self.pack(fill=BOTH, expand=1, padx=1, pady=2)
        #        Label(self, text='hello').pack()
        # TODO : 最好是让它在外面pack
        # TODO : 说明了--每个控件是占据了一块大小，其所占区域受--其他控件的影响
        # pack中使用了side属性的时候，则按照x轴方向排列---其受其他控件影响的是Y轴（即可用fill=Y，填充）
        # pack中么有使用side属性的时候，则按照y轴方向排列---其受其他控件影响的是X轴（即可用fill=X，填充）
        # 如果想控制控件在其所在区域的对其，使用的是anchor
        # Label中的width和height单位是字符大小
        # 一直是在一行里面 -- 超出了窗口大小，则需调整大小方能看到（被隐藏了）
        FirstFrame(self, 'blue').pack(side='left')
        FirstFrame(self, 'red').pack(side='left')
        FirstFrame(self, 'green').pack(side='right')
        FirstFrame(self, 'white').pack(side='left')
        FirstFrame(self, 'red').pack(side='left')
        FirstFrame(self, 'red').pack(side='left', anchor='s', fill=X)
        FirstFrame(self, 'red').pack(side='left')
        FirstFrame(self, 'black').pack(side='left')
        # end
        # 不在同一行了（飞上去了）
        FirstFrame(self, 'black').pack(anchor='nw')  # pack（就是一块大面板）--用anchor来分布其位置在XY上的方位
        FirstFrame(self, 'black').pack(fill=BOTH)
        FirstFrame(self, 'black').pack()
        FirstFrame(self, 'black').pack()
        FirstFrame(self, 'black').pack()
        FirstFrame(self, 'black').pack()
        FirstFrame(self, 'black').pack()
        FirstFrame(self, 'black').pack()
 
        # 不在同一行了（飞下一行）
        FirstFrame(self, 'blue').pack(side='left')
        FirstFrame(self, 'blue').pack(side='left')
        FirstFrame(self, 'blue').pack(side='left')
        FirstFrame(self, 'blue').pack(side='left')
        FirstFrame(self, 'blue').pack(side='right')
        FirstFrame(self, 'blue').pack(side='right')
        FirstFrame(self, 'blue').pack(side='right')
        FirstFrame(self, 'blue').pack(side='right')
 
class FirstFrame(Frame):
    def __init__(self, parent, bgColor):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI(bgColor)
 
    def initUI(self, bgColor):
        self.config( borderwidth=2, bg=bgColor)
        Label(self, text='hello', width=5,height=2).pack(anchor='nw')
 
def main():
    root = Tk()
    root.geometry('300x300')
    app = MainFrame(root)
    root.mainloop()
 
if __name__ == '__main__':
    main()