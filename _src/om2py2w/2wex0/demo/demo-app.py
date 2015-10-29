# coding=utf-8
import Tkinter as tk

root = tk.Tk()
tk.Label(root,text="Hello World").pack()

var = tk.StringVar(value="Hi, what's up")

text_input = tk.Entry(root,textvariable=var)
text_input.pack()

def print_content():
    print var.get()
#    var.set('')
tk.Button(root,text="print",command=print_content).pack()
root.bind('<Return>',lambda event:print_content())

text_output = tk.Message(root,textvariable=var) # 将textvariable设为var
text_output.pack()

root.mainloop()