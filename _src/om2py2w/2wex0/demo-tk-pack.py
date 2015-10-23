#-*- encoding:utf-8 -*-

# create_text
from Tkinter import *

root = Tk()

# root的为80x80
root.geometry('80x80+0+0')
print (root.pack_slaves())
for i in range(5):
    Label(root,text = 'pack' + str(i)).pack()

print (root.pack_slaves())
root.mainloop()