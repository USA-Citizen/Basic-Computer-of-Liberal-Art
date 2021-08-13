# 导入
from tkinter import *
from tkinter.ttk import Combobox # 只有Combobox控件在tkinter.ttk子模块中

# 函数四则
def calc(event): # 函数因为事件event“被选中”而执行，所以函数的参数要加上event
    if etr1.get() != '' and etr2.get() != '':
        a = float(etr1.get())
        b = float(etr2.get())
        if b != 0:
            dic = {0:a+b, 1:a-b, 2:a*b, 3:a/b}
            s = dic[combb.current()] # 组合框获得选项索引current()
            lb.config(text = '结果:'+str(s))
        else:
            dic = {0:a+b, 1:a-b, 2:a*b, 3:'0无法作为除数'}
            s = dic[combb.current()] # 组合框获得选项索引current()
            lb.config(text = '结果:'+str(s))

# 根窗体
root = Tk()
root.title('组合框四则')
root.geometry("320x240")

# 输入框
etr1 = Entry(root)
etr1.place(relx = 0.1, rely = 0.1, relwidth = 0.3, relheight = 0.1)
etr2 = Entry(root)
etr2.place(relx = 0.6, rely = 0.1, relwidth = 0.3, relheight = 0.1)

# 组合框
var = StringVar()
combb = Combobox(root, textvariable = var, values = ['加', '减', '乘', '除'])
combb.bind('<<ComboboxSelected>>', calc) # 组合框绑定被选中时执行的函数
combb.place(relx = 0.1, rely = 0.6, relwidth = 0.3)

# 标签
lb = Label(root, text = '结果：')
lb.place(relx = 0.6, rely = 0.6)

# 主循环
root.mainloop()