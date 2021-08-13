from tkinter import *

def add1():
	a = float(inp1.get())
	b = float(inp2.get())
	s = f'{a:.2f}+{b:.2f}={a+b:.2f}'+'\n'
	txt.insert(END,s)
	inp1.delete(0,END)
	inp2.delete(0,END)
	
def subtract2(x,y):
	a = float(x)
	b = float(y)
	s = f'{a:.2f}-{b:.2f}={a-b:.2f}'+'\n'
	txt.insert(END,s)
	inp1.delete(0,END)
	inp2.delete(0,END)

def multiply3():
	a = float(inp1.get())
	b = float(inp2.get())
	s = f'{a:.2f}*{b:.2f}={a*b:.4f}'+'\n'
	txt.insert(END,s)
	inp1.delete(0,END)
	inp2.delete(0,END)
	
def divide4(x,y):
	a = float(x)
	b = float(y)
	s = f'{a:.2f}/{b:.2f}={a/b:.4f}'+'\n'
	txt.insert(END,s)
	inp1.delete(0,END)
	inp2.delete(0,END)

root = Tk()
root.geometry('460x240')
root.title("简单四则运算")

lb = Label(root, text = "请输入两个数，并选择一种计算方法。")
lb.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.1)

inp1 = Entry(root)
inp1.place(relx = 0.1, rely = 0.2, relwidth = 0.3, relheight = 0.1)
inp2 = Entry(root)
inp2.place(relx = 0.6, rely = 0.2, relwidth = 0.3, relheight = 0.1)

btn1 = Button(root, text = '加法', command = add1)
btn1.place(relx = 0.1, rely = 0.4, relwidth = 0.3, relheight = 0.1)
btn2 = Button(root, text = '减法', command = lambda:subtract2(inp1.get(), inp2.get()))
btn2.place(relx = 0.6, rely = 0.4, relwidth = 0.3, relheight = 0.1)
btn3 = Button(root, text = '乘法', command = multiply3)
btn3.place(relx = 0.1, rely = 0.5, relwidth = 0.3, relheight = 0.1)
btn4 = Button(root, text = '除法', command = lambda:divide4(inp1.get(), inp2.get()))
btn4.place(relx = 0.6, rely = 0.5, relwidth = 0.3, relheight = 0.1)

txt = Text(root)
txt.place(rely = 0.7, relheight = 0.3)

root.mainloop()