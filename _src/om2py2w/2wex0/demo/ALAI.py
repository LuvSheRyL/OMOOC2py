# coding=utf-8
from Tkinter import *

class Write_app:
	def __init__(self,root):
		frame = Frame(root)
		frame.pack()
		self.var = StringVar()
		self.entry = Entry(frame,text=self.var)
		self.entry.pack(side='left')
		Button(frame,text='enter',command=self.enter).pack(side='right')
	def enter(self):
		f = open('a.log','a+')
		f.write(self.var.get()+'\n')
		print self.var.get()
		f.close()
		self.var.set('')

class Print_app:
	def __init__(self,root):
		frame = Frame(root)
		frame.pack()
		self.message = Message(frame,text='')
		self.message.pack(side='right')
		Button(frame,text='show',command=self.show).pack(side='left')
	def show(self):
		f = open('a.log','r')
		text = f.read()
		self.message.config(text=text)
		f.close()

if __name__ == "__main__":
	root = Tk()
	app = Write_app(root)
	app2 = Print_app(root)
	root.mainloop()