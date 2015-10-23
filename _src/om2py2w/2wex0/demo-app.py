#!/usr/bin/env python
#-*- encoding:utf-8 -*-

from Tkinter import *
class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()


# create the application
myapp = App()

#
# here are method calls to the window manager class
#
myapp.master.title("中文My Do-Nothing Application")
myapp.master.maxsize(1000, 1000)

# start the program
myapp.mainloop()